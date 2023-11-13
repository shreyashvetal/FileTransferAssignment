from setuptools import setup, find_packages


setup(
    name="Filetransfer",
    version="1.0.0", 
    author="Shreyash Vetal",
    author_email="shreyasvetal99@gmail.com",
    description="A Python module for transferring files to AWS S3 and Google Cloud Storage",
    long_description_content_type="text/markdown",
    url="https://github.com/shreyashvetal/FileTransferAssignment.git",
    packages=find_packages(),
    install_requires=[
        "boto3", 
        "google-cloud-storage",
    ],
    entry_points={
        "console_scripts": [
            
        ]
    },
    python_requires=">=3.7",
    tests_require=[
        "pytest", 
    ],
)
