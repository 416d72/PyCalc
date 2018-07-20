import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PyCalc",
    version="1.0.0",
    author="@416d72",
    author_email="@416d72@pm.me",
    description="A small calculator app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/@416d72/PyCalc",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)