from os.path import dirname, abspath, join
from setuptools import setup, find_packages
import toml

with open("pyproject.toml", "r") as f:
   requirements = toml.loads(f.read())

prod = requirements['install_requires']
dev = requirements['extras_require']['dev']

setup(
    install_requires=[x + prod[x] if prod[x] != "*" else x for x in prod],
    extras_require={'dev': [x + dev[x] if dev[x] != "*" else x for x in dev]},
)