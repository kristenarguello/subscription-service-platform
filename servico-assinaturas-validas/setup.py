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

setuptools.setup(
    name="assinaturas",
    version="0.0.1",
    author="Us",
    author_email="contato@.com",
    description="API.",
    long_description="",
    long_description_content_type="text/markdown",
    url="https://github.com/",
    packages=setuptools.find_packages(),
    keywords="",
    python_requires=">=3.12",
    install_requires=requirements,
    extras_require=opt_requirements,
)
