import pathlib
from setuptools import find_packages, setup


def get_version() -> str:
    rel_path = "src/prama/__init__.py"
    with open(rel_path, "r") as fp:
        for line in fp.read().splitlines():
            if line.startswith("__version__"):
                delim = '"' if '"' in line else "'"
                return line.split(delim)[1]
    raise RuntimeError("Unable to find version string.")


setup(
    name="prama",
    version=get_version(),
    description="client for prama APIs",
    long_description=pathlib.Path("README.md").read_text(encoding="utf-8"),
    long_description_content_type="text/markdown",
    Homepage="https://github.com/PramaLLC/ben-api-python-integration",
    url="https://github.com/PramaLLC/ben-api-python-integration",
    Issues="https://github.com/PramaLLC/ben-api-python-integration/issues",
    authors=[{"name": "Prama", "email": "pramadevelopment@gmail.com"}],
    author_email="pramadevelopment@gmail.com",
    license="Apache 2.0 License",
    package_dir={"": "src"},
    packages=find_packages("src"),
    include_package_data=True,
    classifiers=["Topic :: Utilities", "Programming Language :: Python :: 3.9"],
    requires=["setuptools", "wheel", "typing", "pillow", "numpy", "requests", "tqdm"],
)
