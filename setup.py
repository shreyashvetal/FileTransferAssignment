from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as readme_file:
    long_description = readme_file.read()

setup(
    name="SacumenAssignment",
    version="1.0.0", 
    author="Shreyash Vetal",
    author_email="shreyasvetal99@gmail.com",
    description="A Python module for transferring files to AWS S3 and Google Cloud Storage",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/my_file_transfer_module",  # Replace with your repository URL
    packages=find_packages(),
    install_requires=[
        "boto3", 
        "google-cloud-storage",
    ],
    entry_points={
        "console_scripts": [
            "SacumenAssignment=services.transfer:main"
        ]
    },
    python_requires=">=3.7",
    tests_require=[
        "pytest", 
    ],
)
