import os

import yaml

""" This file loads configuration from config.yaml """


def load_config():
    """Load configuration from config.yaml based on the current OS and environment"""

    # Determine release, and whether we are on Windows Subsystem for Linux (WSL)
    release = ""
    with open("/etc/os-release") as f:
        for line in f:
            if line.startswith("NAME="):
                release = line.strip().split("=", 1)[1].strip('"')
                break
    are_we_on_wsl = os.path.exists("/mnt/c/Windows/System32/wsl.exe")

    # Load the YAML configuration file
    config_path = os.path.join(
        os.path.dirname(os.path.realpath(__file__)), "config.yaml"
    )

    try:
        with open(config_path, "r") as config_file:
            all_configs = yaml.safe_load(config_file)
    except FileNotFoundError:
        raise Exception(f"Configuration file not found: {config_path}")
    except yaml.YAMLError as e:
        raise Exception(f"Error parsing YAML configuration file: {e}")

    # Determine which configuration to use
    if "Kali" in release:
        config = all_configs["Kali"]
    elif "Ubuntu" in release and are_we_on_wsl:
        config = all_configs["Ubuntu-WSL"]
    elif "Ubuntu" in release:
        config = all_configs["Ubuntu"]
    else:
        raise Exception(
            f"Unsupported OS: {release}. Supported OS types are: Kali, Ubuntu"
        )

    # Set personal_repo_directory to $HOME if it's null
    if config.get("personal_repo_directory") is None:
        config["personal_repo_directory"] = os.getenv("HOME")

    # Validate required keys and types
    required_lists = [
        "directories_to_remove",
        "packages_to_install",
        "packages_to_remove",
        "pip_packages",
        "gem_packages",
        "golang_modules_to_install",
        "ext_repositories_to_sync",
        "personal_repositories_to_sync",
    ]
    required_strings = ["external_tools_directory", "personal_repo_directory"]

    for key in required_lists:
        if key not in config:
            raise ValueError(f"Missing required config key: {key}")
        if config[key] is None:
            config[key] = []
        if not isinstance(config[key], list):
            raise ValueError(
                f"Config key '{key}' must be a list, got {type(config[key]).__name__}"
            )

    for key in required_strings:
        if key not in config or not config[key]:
            raise ValueError(f"Missing required config key: {key}")
        if not isinstance(config[key], str):
            raise ValueError(
                f"Config key '{key}' must be a string, got {type(config[key]).__name__}"
            )

    return config


# Load the configuration
_config = load_config()

# Export configuration variables for backward compatibility
directories_to_remove = _config["directories_to_remove"]
packages_to_install = _config["packages_to_install"]
packages_to_remove = _config["packages_to_remove"]
pip_packages = _config["pip_packages"]
gem_packages = _config["gem_packages"]
golang_install_directory = _config.get("golang_install_directory", "/opt")
golang_modules_to_install = _config["golang_modules_to_install"]
external_tools_directory = _config["external_tools_directory"]
ext_repositories_to_sync = _config["ext_repositories_to_sync"]
personal_repo_directory = _config["personal_repo_directory"]
personal_repositories_to_sync = _config["personal_repositories_to_sync"]
