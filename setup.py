from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


AUTHOR_NAME = "Randika Hewage"
SRC_REPO = 'src'
LIST_OF_REQUIREMENTS = ['streamlit']


setup(
    name = SRC_REPO,
    version = '0.0.1',
    author = AUTHOR_NAME,
    author_email = 'it210@my.sllit.lk',
    description = 'simple package',
    long_description = long_description,
    long_description_text_type = 'text/markdown',
    package = [SRC_REPO],
    python_requires = '>=3.7',
    install_requirements = LIST_OF_REQUIREMENTS
)
