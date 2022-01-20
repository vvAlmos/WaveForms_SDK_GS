from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
   name = "WF_SDK",
   version = "1.0",
   description = "This module realizes communication with Digilent Test & Measurement devices",
   license = "MIT",
   long_description = long_description,
   author = "Almos Veres-Vitalyos",
   author_email = "almos.veres-vitalyos@digilent.ro",
   url = "https://digilent.com/reference/test-and-measurement/guides/waveforms-sdk-getting-started",
   packages = ["WF_SDK"],   # same as name
   install_requires = ["ctypes", "sys", "os"],    # external packages as dependencies
)
