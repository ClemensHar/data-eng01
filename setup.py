from setuptools import setup, find_packages
setup(
    name='data-eng01',
    version='0.0.1',
    author='Clemens Harasewycz',
    description='Scripts wrt data engineering',
    url='https://github.com/ClemensHar/data-eng01',
    python_requires='>=3.10, <4',
    packages=find_packages(include=['data-eng01', 'data-eng01.*']),
    install_requires=[
        'PyYAML',
        'numpy>=1.23.0',
        'matplotlib>=2.2.0',
        'jupyter'
    ],

    entry_points={
        
    }
)