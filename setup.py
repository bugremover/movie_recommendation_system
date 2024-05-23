from setuptools import setup

with open("README.md", "r",encoding="utf-8") as fh:
    long_description = fh.read()

AUTHOR_NAME='HARSHA VARDHAN K'
SRC_REPO='src'
LIST_OF_REQUIREMENTS=['streamlit','pandas']
setup(
    name=SRC_REPO,
    version='0.0.1',
    author=AUTHOR_NAME,
    description='Movie Recommendation Model Package',
    long_description=long_description,
    long_description_content_type="text/markdown",
  
    author_email='harshavardhan75anc@gmail.com',
    packages=[SRC_REPO],
    license='MIT',
    python_requires='>=3.9',
    install_requires=LIST_OF_REQUIREMENTS
)
