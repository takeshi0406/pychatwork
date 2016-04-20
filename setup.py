from setuptools import setup, find_packages

setup(
    name='pychatwork',
    version='1.0.0',
    packages=find_packages(),
    author='takeshi0406',
    include_package_data=True,
    install_requires=[
        'requests'
    ]
)
