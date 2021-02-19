
from setuptools import setup, find_packages

setup(
        name='demo',
        version='0.0.1',
# packages=find_packages(), the package containing __init__.py is searched in the same directory of setup.py
# packages=find_packages(exclude=['*.test', 'test']), Exclude the specified 'test' package
        packages=find_packages('src'), # Contains all packages in the src directory.
        package_dir = {'':'src'}, # Tell distutils that all packages are under src.

        package_data = {
            '' : ['*.txt'], # Any package containing a .txt file includes it.
            'demo' : ['data/*.dat'], # Contains the *.dat file in the data folder of the demo package.
        },
        entry_point = {
            'console_scripts' : [
                'foo = demo:test',
                'bar = demo:test',
             ],        
        },
        include_package_data = True, # Contains all version-controlled files in the package.
        exclude_package_data = {'' : ['README.md']}, # Exclude all specified files in the package.
)
