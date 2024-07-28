from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'


def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]  # when we are moving the install to next requirement we will get '\n' this line is used to remove the '\n'

        if HYPEN_E_DOT in requirements:  # this is required to ignore -e . from requirements file
            requirements.remove(HYPEN_E_DOT)
    return requirements


setup(
    name='mlproject',
    version='0.0.1',
    author='Mohammed',
    author_email='mdsamdani34@gmail.com',
    packages=find_packages(),
    # install_requires=['pandas','numpy','seaborn']
    # Insted of the above line we can create a python package to get the intsalled packages in this file
    install_requires=get_requirements('requirement.txt')

)