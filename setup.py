import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="latterearthquake-indonesia",
    version="0.1.1",
    author="Ryandri",
    author_email="radhinusa@gmail.com",
    description="This package will get recent earthquake detected from"
                "Meteorological, Climatology and Geophysics Agency of Indonesia's website",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Glaceon-Training/recent-indonesia-earthquake",
    project_url={
        "Linkedin": "https://www.linkedin.com/in/ryandri-adhinusa/",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta"
    ],
    # package_dir={"": "src"},
    # packages=setuptools.find_packages(where="src"),
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)
