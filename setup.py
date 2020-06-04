import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="postcode_api",
    version="1.0.0",
    description="Get Information about a PostCode!",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/smi7hy96/post_code_api",
    author="Ryan Smith",
    license="MIT",
    install_requires=["requests"],
)