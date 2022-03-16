import os
from setuptools import setup, find_packages

setup(
    name='anki',
    version='2.1.40',
    description='an anki package for all platform',
    license='GPL Licence',
    author='bohong65',
    author_email='bohong65@gmail.com',
    url='https://github.com/bohong65/anki-whl',
    packages=find_packages(exclude=('test*',)),
    include_package_data=True,
    python_requires='>=3.8',
    install_requires=['beautifulsoup4', 'requests', 'decorator','protobuf','orjson','psutil','distro'],
    data_files=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Development Status :: 4 - Beta"
    ],
    scripts=[],
)