#!/usr/bin/python3
import subprocess
import random
import os

packages = subprocess.check_output("pacman -Q | cut -d ' ' -f1", shell=True)
packages = packages.decode().split("\n")
packages.pop()

random_package = random.choice(packages)
data = subprocess.check_output('pacman -Qi {} | grep "Description" | cut -d ":" -f2'.format(random_package), shell=True)

data = "{}:{}".format(random_package, data.decode())
os.system("cowsay '{}'".format(data))
