from setup import setuptools, find_packages
from typing import List

# Declaring constants for the project
PROJECT_NAME = "House Price Predictor"
VERSION = "0.0.1"
AUTHOR = "Lovish Mittal"
DESCRIPTION = "This application will give the prices of house based on certain parameters."
REQUIREMENT_FILE_NAME = "requirements.txt"

def get_requirements_list() -> List[str]:
    """
    Description: This function is going to return the list of all the packages mentioned in requirements.txt file.

    return: List of packages in requirements.txt file.
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove("-e .")  # -e . is used to find all the packages with a init file.


setup(
name = PROJECT_NAME,
version = VERSION,
author = AUTHOR,
description = DESCRIPTION,
packages = find_packages,       # find packages find all packages with init file
install_requires = get_requirements_list()
)