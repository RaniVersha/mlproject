from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirement(file_path : str) ->List[str]:
    '''
    this function will return the list of requiremnets
    '''

    requirement = []
    with open(file_path) as file_obj:
        requirement = file_obj.readlines()
        requirement = [req.replace("\n","") for req in requirement]

    if HYPEN_E_DOT in requirement:
        requirement.remove(HYPEN_E_DOT)

    return requirement

setup(
    name= "mlproject",
version= "0.0.1",
author= "Versha Rani",
author_email= "vershar1990@gmail.com",
description="end to end ML project",
long_description=open("README.md").read(),
packages=find_packages(),
install_requires = get_requirement("requirement.txt"),
url="https://github.com/RaniVersha/mlproject.git"
)