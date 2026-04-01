#!/usr/bin/env python3
import os
import subprocess
import sys
from datetime import datetime


def print_message(color, message):
    """Prints a formatted message to the console"""
    if color == "green":
        print(
            "\033[1;32m[+] \033[0;37m"
            + datetime.now().strftime("%H:%M:%S")
            + " - "
            + message
        )
    elif color == "blue":
        print(
            "\033[1;34m[i] \033[0;37m"
            + datetime.now().strftime("%H:%M:%S")
            + " - "
            + message
        )
    elif color == "yellow":
        print(
            "\033[0;33m[<] \033[0;37m"
            + datetime.now().strftime("%H:%M:%S")
            + " - "
            + message,
            end="",
        )
    elif color == "red":
        print(
            "\033[1;31m[-] \033[0;37m"
            + datetime.now().strftime("%H:%M:%S")
            + " - "
            + message
        )
    elif color == "error":
        print(
            "\033[1;31m[!] \033[0;37m"
            + datetime.now().strftime("%H:%M:%S")
            + " - "
            + message
        )
    else:
        print(
            "\033[0;41mInvalid Format\033[0;37m "
            + datetime.now().strftime("%H:%M:%S")
            + " "
            + message
        )


def elevate_privileges():
    """Gets sudo privileges and returns the current date"""
    result = subprocess.run(["sudo", "date"])
    print()
    return result.returncode


def take_ownership(directory):
    username = os.getenv("USER") or os.path.basename(os.path.expanduser("~"))
    subprocess.run(["sudo", "chown", username + ":" + username, directory])


def update_packages():
    """Do a general update of the system packages"""
    cmdseries = [
        ["sudo", "apt", "update"],
        ["sudo", "apt", "full-upgrade", "-y"],
        ["sudo", "apt", "autoremove", "-y"],
    ]
    for cmd in cmdseries:
        subprocess.run(cmd)


def install_package(package, apt_cache):
    """Installs a package using apt"""
    if not apt_cache[package].is_installed:
        print_message("green", "Installing " + package)
        subprocess.run(["sudo", "apt", "install", "-y", package])


def remove_package(package, apt_cache):
    """Removes a package using apt"""
    if apt_cache[package].is_installed:
        print_message("red", "Removing " + package)
        subprocess.run(["sudo", "apt", "remove", "-y", package])


def pip_package_install(pip_packages, installed_pip_packages):
    """Install python pip package"""
    for package in pip_packages:
        if package not in installed_pip_packages:
            print_message("green", "Installing pip package " + package)
            subprocess.run(["python3", "-m", "pip", "install", "--upgrade", package])


def update_pip_packages():
    """Update pip packages"""
    result = subprocess.run(
        ["pip3", "list", "--outdated", "--format=freeze"],
        capture_output=True,
        text=True,
    )
    for line in result.stdout.splitlines():
        if line.startswith("-e"):
            continue
        package = line.split("==")[0]
        if package:
            subprocess.run(["pip3", "install", "-U", package])


def gem_package_install(gem_packages, installed_gem_packages):
    """Install Ruby gem package"""
    for package in gem_packages:
        if package not in installed_gem_packages:
            print_message("green", "Installing gem package " + package)
            subprocess.run(["sudo", "gem", "install", package])


def update_gems():
    """Update gem packages"""
    subprocess.run(["gem", "outdated"], stdout=subprocess.DEVNULL)
    subprocess.run(["gem", "update"])


def install_golang_module(module, golang_install_directory):
    """Install the specified Golang module"""
    modulename = module.split("/")[-1].lower()
    gopath = golang_install_directory + "/" + modulename
    if not os.path.exists(gopath):
        print_message("green", "Installing go module " + modulename)
        env = {**os.environ, "GOPATH": gopath}
        subprocess.run(["go", "install", module + "@latest"], env=env)
        link_src = gopath + "/bin/" + modulename
        link_dst = "/usr/local/bin/" + modulename
        subprocess.run(["sudo", "ln", "-s", link_src, link_dst])


def update_go_packages(golang_modules_to_install, golang_install_directory):
    """Rebuild all Go modules"""
    print_message("green", "Rebuilding Go modules")
    for modulename in golang_modules_to_install:
        module = modulename.split("/")[-1].lower()
        env = {**os.environ, "GOPATH": golang_install_directory + "/" + module}
        subprocess.run(["go", "install", modulename + "@latest"], env=env)


def create_directory(directory):
    """Checks if the specified directory exists, and creates it if not"""
    if not os.path.exists(directory):
        print_message("green", "Creating directory: " + directory)
        os.makedirs(directory, exist_ok=True)


def remove_directory(directory):
    """Checks if the specified directory exists, and deletes it if it does"""
    directory = os.getenv("HOME") + "/" + directory
    if os.path.exists(directory):
        print_message("red", "Removing directory: " + directory)
        os.rmdir(directory)


def sync_git_repo(gitrepo, repo_collection_dir):
    """Sync the specified git repository"""
    repo_name = gitrepo.split("/")[-1].lower()
    repo_path = repo_collection_dir + "/" + repo_name
    if os.path.exists(repo_path):
        print_message("yellow", "Syncing " + repo_name + ": ")
        sys.stdout.flush()
        subprocess.run(["git", "-C", repo_path, "pull"])
    else:
        print_message("green", "Cloning " + repo_name)
        subprocess.run(["git", "clone", gitrepo, repo_path])


def run_scripts():
    """Run each .sh or .py file in the scripts directory"""
    script_directory = os.path.dirname(os.path.realpath(__file__)) + "/scripts"

    if os.path.exists(script_directory):
        scripts = sorted(os.listdir(script_directory))
        for script in scripts:
            if script.endswith(".sh") or script.endswith(".py"):
                subprocess.run([script_directory + "/" + script])
    else:
        print_message("error", "'scripts' directory is missing")
