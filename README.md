# Collector-script-network-devices-Huawei-and-Cisco-tested

## Description

This simple script collects data via CLI commands using an SSH connection. This script stores command output in `ip_address.txt` format.
This script is useful for a fast inspection of a small or medium amount of network elements for both Cisco and Huawei vendors cause here it used neutral-vendor `paramiko` python module

## How to use 

1. Clone the repo to your local machine
2. Prepare `device_list.txt`: input your management IP addresses (for which you connect to SSH manually)
3. Prepare `command_list.txt`: input commands that will be sent by the script to network elements
4. Specify in `main.py` your credentials: username and password.
5. Install on your local machine `paramiko` module with mandatory dependencies
6. Launch `main.py`. All logs will be stored in the project directory.

## Note

Please be sure that your user has enough permissions to input several commands on network elements according to AAA user privilege level
