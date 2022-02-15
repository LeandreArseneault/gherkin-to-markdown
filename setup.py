from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='gherkin-to-markdown',
    version='0.0.1',
    author="Léandre Arseneault",
    author_email="arseneault.leandre@gmail.com",
    description="A converter from Gherkin feature files to markdown files.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/LeandreArseneault/gherkin-to-markdown",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
