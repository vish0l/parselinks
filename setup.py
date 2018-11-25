import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="parselinks",
    version="0.0.1",
    author="vishal singh",
    author_email="vishaldsingh06@gmail.com",
    description="Simple python module to extract links from pages.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/venins/pa",
    packages=setuptools.find_packages(),
    install_requires=['requests==2.20.1', 'lxml==4.2.5'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)