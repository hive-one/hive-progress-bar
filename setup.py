import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hive-progress-bar",  # Replace with your own username
    version="0.0.4",
    author="Heinrich Malan",
    author_email="heinrich@hive.one",
    description="A small progress bar for iterating over a collection and showing progress.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hive-one/hive-progress-bar",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
