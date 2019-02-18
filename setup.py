from setuptools import setup, find_packages

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='uiza',
    version='1.0.0',
    author='hoangtruongminh;minhhahao;ngoduykhanh',
    author_email='hoang.truong.minh@framgia.com;ha.hao.minh@framgia.com;ngo.duy.khanh@framgia.com',
    description='Uiza SDK tool',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='',
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
