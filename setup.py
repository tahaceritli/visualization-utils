import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="visualization-utils", # Replace with your own username
    version="0.0.1",
    author="Taha Yusuf Ceritli",
    author_email="t.y.ceritli@sms.ed.ac.uk",
    description="My visualization package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tahaceritli/visualization-utils",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)