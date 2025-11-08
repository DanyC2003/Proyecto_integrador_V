from setuptools import setup, find_packages

setup(
    name="proyecto_integrador_v",
    version="0.0.1",
    author="Camilo Olea, Daniela Coronado",
    author_email="camilo.olea@est.iudigital.edu.co, daniela.coronado@est.iudigital.edu.co",
    description="Proyecto integrador V",
    py_modules=["proyecto_integrador_v"],
    install_requires=[
        "pandas",
        "openpyxl",
        "requests",
        "beautifulsoup4",
        "matplotlib",
        "kagglehub[pandas-datasets]>=0.3.8",
        "seaborn",
        "pyarrow"
    ]
)