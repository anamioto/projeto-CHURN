from setuptools import setup, find_packages

setup(
    name='pre_processamento',
    version='0.1.0',
    description='Pré-processamento de dados de clientes para modelo de ML de Churn',
    author='Ana',
    packages=find_packages(),
    install_requires=[
        'pandas>=1.0.0',
    ],
    python_requires='>=3.7',
)
