from setuptools import find_packages,setup
from typing import List
HYPHEN_e='-e .'
def get_requirements(file_path:str)->list[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        if HYPHEN_e in requirements:
            requirements.remove(HYPHEN_e)

    return requirements



setup(
    name='FLIGHT PREDICTION',
    version='0.0.1',
    author='Tejal',
    author_email='tejal.c15@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)