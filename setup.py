from setuptools import setup, find_packages


with open('README.rst', "r") as fh:
    readme = fh.read()

setup(
    name='SNAP',
    version='1.0.0',
    description='Simulate game of Snap between 2 players on the command line',
    long_description=readme,
    author='Alexander Ogedengbe',
    author_email='aogedengbe11@gmail.com',
    url='https://github.com/XanderHere/SNAP',
    license=license,
    packages=find_packages()
)
