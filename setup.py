from setuptools import setup, find_packages

setup(
    name="gterm",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    package_data={"gittui.ascii": ["*.txt"]},
    install_requires=["rich", "questionary"],
    entry_points={"console_scripts": ["gterm=gittui.cli:run"]},
)
