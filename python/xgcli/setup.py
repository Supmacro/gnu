
from setuptools import setup, find_packages

install_requirements = [
    'Pygments >= 1.6',
    'prompt_toolkit>=3.0.6,<4.0.0',
    'configobj >= 5.0.5',
    'click >= 7.0',
]

setup(
    name="xgcli",
    version="2.0.2",
    author="Supmacro",
    author_email="supmacro@foxmail.com",
    description="CLI for Xugu database, with syntax highlighting",

    packages=find_packages(), 
    package_data={'xgcli': ['xgclirc', 'AUTHORS']},
    python_requires=">=3.6", 
    install_requires=install_requirements,    

    # https://pypi.org/pypi?%3Aaction=list_classifiers
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: SQL',
        'Topic :: Database',
        'Topic :: Database :: Front-Ends', 
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ], 

    entry_points={
        'console_scripts': ['xgcli = xgcli.main:client'],
    }, 
)

