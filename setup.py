import setuptools
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()
# change all this
setup(
    name="scoobydoo",
    version="0.1",
    description="Giving Scooby Doo Character Catch Phrases",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kyle-woodward/scooby-doo",
    packages=setuptools.find_packages(),
    author="Kyle Woodward",
    author_email="kw.geospatial@gmail.com",
    license="GNU GPL v3.0",
    zip_safe=False,
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "scoobydoo = scoobydoo.main:main",
        ]
    },
    #install_requires=["simplecmr", "earthengine-api", "gcsfs", "fire", "pipetools"],
)