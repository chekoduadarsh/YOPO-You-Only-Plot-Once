import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

    
setuptools.setup(
    name="yopo",
    version="0.0.20",
    author="Adarsh Chekodu",
    author_email="chekodu.adarsh@gmail.com",
    description="You Plot Only Once",
    license='Apache License 2.0',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/chekoduadarsh/YOPO-You-Only-Plot-Once",
    packages=setuptools.find_packages(exclude=("tests",)),
    install_requires=[
        "MarkupSafe>=2.0",
        "jupyter_dash",
        "click>=7.1.2",
        "ipython",
        "jupyter",
        "wtforms",
        "dash==2.0.0",
        "dash_daq",
        "pandas",
        "numpy",
        "dash_bootstrap_components",
        "pyngrok"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)