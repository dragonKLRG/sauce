from setuptools import setup

setup(
    name="sauce",
    version="1.0",
    py_modules=["sauce"],
    entry_points={
        "console_scripts": [
            "sauce=sauce:main",
        ],
    },
)

