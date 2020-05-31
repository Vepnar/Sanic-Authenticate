import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    required = f.read().splitlines()

setuptools.setup(
    name="sanic-authenticate",
    version="0.1.0",
    author="Arjan de Haan",
    author_email="vepnardev@gmail.com",
    license="MIT",
    description="Easy way to handle users and authentication",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Vepnar/Sanic-Authenticate",
    platforms="any",
    packages=['sanic_authenticate'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=required
)