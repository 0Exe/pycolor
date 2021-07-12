import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pycolor-0Exe",
    version="0.0.1",
    author="0Exe",
    author_email="zeroexe3000@gmail.com",
    description="Color Markup in Python!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/0Exe/pycolor",
    project_urls={
        "Bug Tracker": "https://github.com/0Exe/pycolor/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)