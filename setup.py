# setup.py
import os
import sys
from pathlib import Path
from setuptools import setup, Extension, find_packages
import pybind11

# ----------------------------------------------------------------------
# Helper: locate the Python include directory (required for pure C‑API)
# ----------------------------------------------------------------------
def get_python_include():
    from sysconfig import get_paths
    return get_paths()["include"]

def get_pybind_include():
    return pybind11.get_include()

cpp_sources = [ 
                "src/sextupole_pybind.cpp",
                "MagnetModel/src/Sextupole.cpp",
                "MagnetModel/src/Magnet.cpp",
                "MagnetModel/src/Multipole.cpp",
                "MagnetModel/src/SextuCorrModel.cpp",
                "MagnetModel/src/Interpolation.cpp"
              ]
extra_compile_args = ["-std=c++14"]          # adjust for your compiler


# ----------------------------------------------------------------------
# Build the Extension object
# ----------------------------------------------------------------------
extension = Extension(
    name="ebs_sextupole_bind",
    sources=cpp_sources,
    language="c++",
    include_dirs=[
        get_python_include(),
        get_pybind_include(),
        "MagnetModel/include",
        "/segfs/tango/contrib/eigen/include/eigen3"
    ],
    extra_compile_args=extra_compile_args,
    # For MSVC on Windows you may need:
    # extra_compile_args=["/std:c++14"] if os.name == "nt" else ["-std=c++14"],
)

# ----------------------------------------------------------------------
# setuptools configuration
# ----------------------------------------------------------------------
setup(
    name="ebs-sextupole",
    version="0.0.1",
    description="EBS Sextupole magnet model binding for PyAML",
    author="Jean Luc PONS",
    packages=["ebs_sextupole"],
    package_dir={"ebs_sextupole":"src/ebs_sextupole"},
    ext_modules=[extension],
    python_requires=">=3.12",
    setup_requires=["wheel"],
    zip_safe=False,
)