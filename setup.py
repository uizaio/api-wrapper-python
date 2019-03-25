from setuptools import setup, find_packages

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='uiza',
    version='1.1.2',
    author='Uiza',
    author_email='developer@uiza.io',
    description='Uiza SDK tool',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/uizaio/api-wrapper-python',
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
