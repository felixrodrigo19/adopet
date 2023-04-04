from setuptools import find_packages, setup


def read(filename):
    return [req.strip() for req in open(filename)]


setup(
    name="adopet",
    version="1.0.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=read("requirements.txt")
)
