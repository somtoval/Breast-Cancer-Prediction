import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "Breast-Cancer-Prediction"
AUTHOR_USER_NAME = "Somto Ogbe"
SRC_REPO = "Breast-Cancer-Prediciton"
AUTHOR_EMAIL = "ogbesomto4@gmail.com"
GITHUB_USER_NAME = "somtoval"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Breast Cancer Prediction Machine Learning Project",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{GITHUB_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{GITHUB_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)