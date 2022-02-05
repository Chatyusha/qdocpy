import setuptools
from setuptools import setup

def main():
      setup(
            name='qdocpy',
            version='1.0.0',
            description='Qdoc Parser by Python3',
            author='Chatyusha',
            author_email='hirounicat76@gmail.com',
            url='https://github.com/Chatyusha/qdocpy',
            packages = setuptools.find_packages()
      )

if __name__ == "__main__":
      main()