import os

from setuptools import setup


def find_stubs(package):
    stubs = []
    for root, dirs, files in os.walk(package):
        for file in files:
            path = os.path.join(root, file).replace(package + os.sep, "", 1)
            stubs.append(path)
    return {package: stubs}


setup(
    name="rebound-stubs",
    maintainer="Lukas Winkler",
    maintainer_email="rebound-stubs@lw1.at",
    description="type stubs for Rebound",
    license="GPL",
    version="3.18.0",
    packages=["rebound-stubs"],
    # PEP 561 requires these
    install_requires=[
        "rebound>=3.18.0",
    ],
    package_data=find_stubs("rebound-stubs"),
    zip_safe=False,
)
