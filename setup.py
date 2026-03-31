from setuptools import setup, find_packages

setup(
    name="py_pkg",                 # package name
    version="0.1.0",               # version
    packages=find_packages(),      # find all packages in your folder
    install_requires=[],           # dependencies, e.g., ["numpy", "pandas"]
    author="Ahmed Ali Khakwani",
    author_email="your_email@example.com",
    description="My first Python package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ahmedalikhakwani-lab/py_pkg",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
