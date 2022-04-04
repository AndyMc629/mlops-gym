import itertools
import os.path
import sys

from setuptools import find_packages, setup

# Don't import mlops_gym module here, since deps may not be installed
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "mlops_gym"))
from version import VERSION

setup(
    name="mlops_gym",
    version=VERSION,
    description="MLOps Gym: A toolkit for supporting development of MLOps pipelines",
    # url="https://www.gymlibrary.ml/",
    author="Andrew McMahon",
    license="MIT",
    packages=[package for package in find_packages() if package.startswith("gym")],
    zip_safe=False,
    # install_requires=[
    #     "numpy>=1.18.0",
    #     "cloudpickle>=1.2.0",
    #     "importlib_metadata>=4.10.0; python_version < '3.10'",
    #     "gym_notices>=0.0.4",
    # ],
    # extras_require=extras,
    # package_data={
    #     "gym": [
    #         "envs/mujoco/assets/*.xml",
    #         "envs/classic_control/assets/*.png",
    #         "envs/toy_text/font/*.ttf",
    #         "envs/toy_text/img/*.png",
    #         "py.typed",
    #     ]
    # },
    tests_require=["pytest", "mock"],
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
