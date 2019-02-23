import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ecolibrium-assessment-bhushanrathod",
    version="0.0.1",
    author="BHushan Rathod",
    author_email="abhushanprathod@example.com",
    description="There is a configuration where users can setup the time when they want to perform a particular task",
    long_description=long_description,
    url="https://github.com/BHushanRathod/ecolibrium-assessment",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)