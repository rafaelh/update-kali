#!/usr/bin/env python3
import os
import apt
import subprocess
import sys

def print_bold_green(message):
    """ Prints a message to the console prefixed with a green '>>>' """
    print("\n\033[1;32m>>> \033[0;37m" + message + "\033[0;37m")

def print_green(message):
    """ Prints a message to the console prefixed with a green '>>>' """
    print("\033[0;32m>>> \033[0;37m" + message + "\033[0;37m")

def print_yellow(message):
    """ Prints a message to the console prefixed with a yellow '>>>' """
    print("\033[1;33m>>> \033[0;37m" + message + "\033[0;37m")

def print_grey(message):
    """ Prints a message to the console prefixed with a grey '>>>' """
    print("\033[0;37m>>> \033[0;37m" + message + "\033[0;37m")

def print_red(message):
    """ Prints a message to the console prefixed with a red '>>>' """
    print("\033[0;31m>>> \033[0;37m" + message + "\033[0;37m")

def elevate_privileges():
    """ Gets sudo privileges and returns the current date """
    status = os.system("sudo date")
    return status

def take_ownership(directory):
    username = os.path.expanduser("~").split('/')[2]
    cmdstring = "sudo chown " + username + ":" + username + " " + directory
    os.system(cmdstring)

def update_packages():
    """ Do a general update of the system packages """
    print_bold_green("General Update")
    updatecmds = ['update', 'upgrade', 'dist-upgrade', 'autoremove']
    for updatecmd in updatecmds:
        os.system("sudo apt -y " + updatecmd)

def install_package(package, apt_cache):
    """ Installs a package from apt or lets you know if its present """
    if apt_cache[package].is_installed:
        print_grey("Package '" + package + "' already installed")
    else:
        print_red("Installing " + package)
        cmdstring = "sudo apt install -y " + package
        if package == "pip": cmdstring += " && sudo pip3 install --upgrade pip"
        os.system(cmdstring)

def remove_package(package, apt_cache):
    """ Installs a package from apt or lets you know if its present """
    if not apt_cache[package].is_installed:
        print_grey("Package '" + package + "' already removed")
    else:
        print_red("\nRemoving " + package)
        cmdstring = "sudo apt remove -y " + package
        os.system(cmdstring)

def pip_package_install(pip_packages, installed_pip_packages):
    for package in pip_packages:
        if package in installed_pip_packages:
            print_grey("Pip package '" + package + "' already installed")
        else:
            print_red("Installing pip package " + package)
            cmdstring = "sudo pip3 install --upgrade " + package
            os.system(cmdstring)

def install_golang_module(module):
    ''' Install the specified Golang module '''
    modulename = module.split("/")[-1].lower()
    if not os.path.exists("/opt/" + modulename):
        print_red("Installing go module " + modulename)
        cmdseries = ["sudo -E go get -u " + module,
                     "sudo ln -s /opt/" + modulename + "/bin/" + modulename + " /usr/local/bin/" + modulename]
        os.environ["GOPATH"] = "/opt/" + modulename
        for cmdstring in cmdseries:
            os.system(cmdstring)

def create_directory(directory):
    ''' Checks if the specified directory exists, and creates it if not '''
    if os.path.exists(directory):
        print_grey("Directory exists: " + directory)
    else:
        print_red("Creating directory: " + directory)
        cmdstring = "mkdir " + directory
        os.system(cmdstring)

def remove_directory(directory):
    ''' Checks if the specified directory exists, and deletes it if it does '''
    directory = os.getenv("HOME") + '/' + directory
    if os.path.exists(directory):
        print_red("Removing directory: " + directory)
        cmdstring = "rmdir " + directory
        os.system(cmdstring)

def sync_git_repo(gitrepo, repo_collection_dir):
    ''' Sync the specified git repository '''
    repo_name = gitrepo.split("/")[-1].lower()
    if os.path.exists(repo_collection_dir + '/' + repo_name):
        print_yellow("Syncing " + repo_name)
        cmdstring = "git -C " + repo_collection_dir + '/' + repo_name + " pull origin master"
        os.system(cmdstring)
    else:
        print_red("Cloning " + repo_name)
        cmdstring = "git clone " + gitrepo + ' ' + repo_collection_dir + '/' + repo_name
        os.system(cmdstring)

def run_scripts():
    ''' Run each .sh or .py file in the scripts directory '''
    script_directory = os.path.dirname(os.path.realpath(__file__)) + '/scripts'

    if os.path.exists(script_directory):
        scripts = os.listdir(script_directory)
        for script in scripts:
            if '.sh' or '.py' in script:
                cmdstring = script_directory + '/' + script
                os.system(cmdstring)
    else:
        print_red("'scripts' directory is missing")
