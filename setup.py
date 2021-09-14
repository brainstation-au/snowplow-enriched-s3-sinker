from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name="snowplow-enriched-s3-sinker",
    version="0.0.1",
    author="Khalid Saifullah",
    author_email="khalid@outlook.com.au",
    description="Transform snowplow enriched tsv records to json and dump them in S3 via firehose",
    entry_points={},
    install_requires=requirements,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/brainstation-au/snowplow-enriched-s3-sinker",
    project_urls={
        "Bug Tracker": "https://github.com/brainstation-au/snowplow-enriched-s3-sinker/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.6",
)
