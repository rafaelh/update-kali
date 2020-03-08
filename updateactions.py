#!/usr/bin/env python3
import os
import apt
import subprocess
import sys

def print_bold_green(message):
    """ Prints a message to the console prefixed with a green '>>>' """
    print("\n\033[1;32;40m>>> \033[1;37;40m" + message + "\033[0;37;0m")

def print_green(message):
    """ Prints a message to the console prefixed with a green '>>>' """
    print("\033[0;32;40m>>> \033[0;37;40m" + message + "\033[0;37;0m")

def print_yellow(message):
    """ Prints a message to the console prefixed with a yellow '>>>' """
    print("\033[1;33;40m>>> \033[0;37;40m" + message + "\033[0;37;0m")

def print_grey(message):
    """ Prints a message to the console prefixed with a grey '>>>' """
    print("\033[0;37;40m>>> \033[0;37;40m" + message + "\033[0;37;0m")

def print_red(message):
    """ Prints a message to the console prefixed with a red '>>>' """
    print("\033[0;31;40m>>> \033[0;37;40m" + message + "\033[0;37;0m")

def update_packages():
    """ Do a general update of the system packages """
    print_bold_green("General Update")
    updatecmds = ['update', 'upgrade', 'dist-upgrade', 'autoremove']
    for updatecmd in updatecmds:
        os.system("sudo apt -y " + updatecmd)

def check_service_status(service):
    """ Returns 'active' or 'inactive' depending on service status """
    status = os.system("systemctl is-active --quiet " + service)
    return status

def package_install(package, cache):
    if cache[package].is_installed:
        print_grey("Package '" + package + "' already installed")
    else:
        print_red("\nInstalling " + package)
        cmdstring = "sudo apt install -y " + package
        if package == "pip": cmdstring += " && sudo pip3 install --upgrade pip"
        os.system(cmdstring)

def pip_package_install(pip_packages, installed_pip_packages):
    for package in pip_packages:
        if package in installed_pip_packages:
            print_grey("Pip package '" + package + "' already installed")
        else:
            print_red("Installing pip package " + package)
            cmdstring = "sudo pip3 install --upgrade " + package
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

def git_sync(gitrepo, directory):
    if os.path.exists(directory):
        print_yellow("Syncing " + directory)
        cmdstring = "git -C " + directory + " pull origin master"
        os.system(cmdstring)
    else:
        print_red("Cloning " + directory)
        cmdstring = "git clone " + gitrepo + " " + directory
        if directory == '/impacket': cmdstring += " && pip install " + os.getenv("HOME") + '/z/impacket'
        os.system(cmdstring)

def run_scripts():
    """ Run each .sh or .py file in the scripts directory """
    script_directory = os.path.dirname(os.path.realpath(__file__)) + '/scripts'

    if os.path.exists(script_directory):
        scripts = os.listdir(script_directory)
        for script in scripts:
            if '.sh' or '.py' in script:
                cmdstring = script_directory + '/' + script
                os.system(cmdstring)
    else:
        print_red("'scripts' directory is missing")
