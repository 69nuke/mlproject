# Import necessary modules
from setuptools import find_packages, setup
from typing import List as TypingList  # Changed the import here

# Define a constant for '-e .' to simplify code readability
HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> TypingList[str]:  # Changed the return type annotation here
    '''
    Retrieve requirements from a file.
    Args:
        file_path (str): Path to the requirements file.
    Returns:
        TypingList[str]: List of requirements extracted from the file. Changed the return type annotation here
    '''
    # Initialize an empty list to store requirements
    requirements = []

    # Open the file and read its contents
    with open(file_path) as file_obj:
        # Read lines from the file and store them as requirements
        requirements = file_obj.readlines()

        # Remove newline characters from each requirement
        requirements = [req.replace("\n", "") for req in requirements]

        # If '-e .' is found in requirements, remove it
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

# Setup configuration
setup(
    name='mlproject',
    version='0.0.1',
    author='Krish',
    author_email='krishnaik06@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)