import subprocess
import os

# Read the package name from ~pip.txt
with open("pip.txt", "r") as file:
    package_name = file.read().strip()

# Define the package(s) you want to install
packages_to_install = [package_name]

# Loop through the list of packages and install them one by one
for package in packages_to_install:
    try:
        # Use subprocess to run the pip install command
        subprocess.run(["pip", "install", package], check=True)
        print(f"Successfully installed {package}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install {package}: {e}")

os.remove("pip.txt")