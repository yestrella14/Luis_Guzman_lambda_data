import setuptools


REQUIRED = ["pandas", "numpy"]

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lambdadata-laguz", # Replace with your own username
    version="0.0.1",
    author="laguz",
    author_email="laguz3@example.com",
    description="A collection of Data Science functions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/laguz/Luis_Guzman_lambda_data",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
