# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

import os


package_dir = os.path.dirname(os.path.abspath(__file__))
version = open(os.path.join(package_dir, "VERSION")).read().strip()
readme = open(os.path.join(package_dir, "README.md")).read().strip()

setup(
    name="panel-bootstrap-vue",
    version=version,
    author="Paulo Lopes",
    author_email="paulopes00@gmail.com",
    url="https://github.com/paulopes/panel-bootstrap-vue",
    description="Use bootstrap-vue VueJs components supporting Bootstrap 4 in Panel templates.",
    long_description=readme,
    packages=find_packages("panel_bootstrap_vue"),
    install_requires=["panel", "panel-components"],
    test_suite="tests",
)
