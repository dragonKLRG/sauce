from setuptools import setup

setup(
    name="sauce",
    version="1.0",
    py_modules=["sauce"],
    install_requires=[
        "setuptools",  # Asegura que setuptools esté instalado
    ],
    entry_points={
        "console_scripts": [
            "sauce=sauce:main",
        ],
    },
)
