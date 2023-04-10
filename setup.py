from setuptools import setup, find_packages

PACKAGE_NAME = 'Demo'
PACKAGE_VERSION = '0.1'
INSTALL_REQUIRES = [
    'selene==2.0.0b17',
    'whocares',
    'pytest',
    'allure-pytest',
    'PyHamcrest',
    'requests',
    'python-dotenv',
    'mariadb',
    'Faker',
    'jsonschema',
    'addict',
    'pytest-xdist'
]
setup(
    name=PACKAGE_NAME,
    version=PACKAGE_VERSION,
    description=('Demo Test Project for bank app'),
    packages=find_packages(),
    install_requires=INSTALL_REQUIRES
)
