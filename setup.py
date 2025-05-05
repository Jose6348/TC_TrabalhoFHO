from setuptools import setup, find_packages

setup(
    name="dataflow",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "antlr4-python3-runtime>=4.13.1",
        "pandas>=2.2.0",
        "matplotlib>=3.8.0",
    ],
) 