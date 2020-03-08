# update-kali
A script to set up Kali Linux with additional tools

[TOC]

## What is this?
I find that I need to keep a lot of Kali linux installations up to date, and I like them to be setup in a similar format. This script installs the tools I'm likely to use, creates directories, etc. Currently it's just set up for my personal use, but I'm intending to make it more generic over time.



## Config

The default config can be found in config.py. You should updated it to match what you want, otherwise you'll have my preferences used. This script will:

* Perform a general update
* Install the specified packages
* Remove specified packages [TODO]
* Install python modules
* Set up some standardized directories
* Run each of the `.sh` or `.py` files in the `scripts` directory. If you add a script to this directory, make sure they can be run multiple times without causing a problem. [TODO]

