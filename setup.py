from setuptools import setup, find_packages

setup(
    name='euro_2024_tournament-data',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pandas',
    ],
    author='Patrick Russell',
    description='Euro 2024 Tournament Data',
    url='https://github.com/prussell94/Euro-2024-tournament-data',
)