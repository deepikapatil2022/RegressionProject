from setuptools import setup,find_packages

from typing import List
HYPEN_E_DOT='-e .'

def get_requirements(filepath:str)->List[str]:
    requirements=[]
    with open(filepath) as file_obj:
        requirements=file_obj.readlines() 
        requirements=[req.replace('/n',"") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


setup(name="RegressorProject",
      version="0.0.1",
      author="Deepika",
      author_email="deepikapatil2022@gmail.com",
      packages=find_packages(),
      install_requires=get_requirements("requirements.txt")
      )