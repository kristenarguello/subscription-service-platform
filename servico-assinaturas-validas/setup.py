from __future__ import annotations

from pathlib import Path

import setuptools


def read_multiline_as_list(file_path: str) -> list[str]:
    with open(file_path) as fh:
        contents = fh.read().split("\n")
        if contents[-1] == "":
            contents.pop()
        return contents


def get_optional_requirements() -> dict[str, list[str]]:
    """Get dict of suffix -> list of requirements."""
    requirements_files = Path(".").glob(r"requirements-*.txt")
    requirements = {
        p.stem.split("-")[-1]: read_multiline_as_list(p) for p in requirements_files  # type: ignore
    }
    return requirements


requirements = read_multiline_as_list("requirements.txt")
opt_requirements = get_optional_requirements()

with open("README.md", "r") as readme_file:
    long_description = readme_file.read()

setuptools.setup(
    name="athena",
    version="2.0.0",
    author="Teialabs",
    author_email="contato@teialabs.com",
    description="Teia Athena bot API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TeiaLabs/athena",
    packages=setuptools.find_packages(),
    keywords="athena, chatbot, api, gpt3",
    python_requires=">=3.12",
    install_requires=requirements,
    extras_require=opt_requirements,
)
