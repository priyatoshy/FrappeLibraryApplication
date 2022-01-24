from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in library_app/__init__.py
from library_app import __version__ as version

setup(
	name="library_app",
	version=version,
	description="A Simple Library Management System Built Within Frappe\\",
	author="Priyatosh",
	author_email="priyatoshsatpati1@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
