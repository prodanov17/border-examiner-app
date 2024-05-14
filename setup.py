from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='border-traffic-app',
    version='0.1.0',
    description='Sample package for Python-Guide.org',
    long_description=readme,
    author='Kenneth Reitz',
    author_email='trajce.p@live.com',
    url='https://github.com/prodanov17/border-traffic-app',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)