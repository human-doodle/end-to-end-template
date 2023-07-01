from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'
def get_requirements(filepath: str) -> List[str]:
    '''
    This function will return a list of libraries from requirements.txt
    '''
    requirements = []
    with open(filepath) as fileobj:
        requirements = fileobj.readline()
        requirements = [req.replace('\n','') for req in requirements]

        # HYPHEN_E_DOT is used in requirements.txt to map it to setup.py
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)


setup(
    name = 'project',
    version = '0.0.1',
    author = 'Shivani',
    author_email = 'shivanipal4994@gmail.com',
    packages = find_packages(),
    # install_requires = ['pandas', 'numpy', 'seaborn'],
    install_requires = get_requirements('requirements.txt')
)