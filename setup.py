from setuptools import setup, find_packages

setup(
    name="pypaze",  # The name of your package
    version="0.1.0",  # Version of your package
    description="A lightweight full-stack web framework on top of Flask",
    long_description=open('README.md').read(),  # Read the long description from the README file
    long_description_content_type="text/markdown",  # Markdown format for README
    author="Vishal Singh Baraiya",  # Your name or organization
    author_email="realvixhal@gmail.com",  # Your email address
    url="https://github.com/vishal-singh-baraiya/pypaze",  # Link to your GitHub or website
    packages=find_packages(),  # Automatically discover packages in your project
    include_package_data=True,  # Include non-Python files like templates, static, etc.
    install_requires=[
        "Flask",  # Add any dependencies your framework requires
        "watchdog",  # For hot-reloading support
        "click",
        "pathlib",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "pypaze=pypaze.cli:cli",  # CLI command to run the app
        ],
    },
)
