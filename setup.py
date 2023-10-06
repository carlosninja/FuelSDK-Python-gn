from os.path import dirname, join, realpath
from setuptools import setup


__version__ = '1.3.1'


with open('README.md') as f:
    readme = f.read()

with open(join(dirname(realpath(__file__)), 'requirements.txt')) as f:
    PACKAGE_INSTALL_REQUIRES = [line[:-1] for line in f]

print(PACKAGE_INSTALL_REQUIRES)

setup(
    version=__version__,
    name='Salesforce-FuelSDK-gn',
    description='Salesforce Marketing Cloud Fuel SDK for Python',
    long_description=readme,
    long_description_content_type="text/markdown",
    author='GetNinjas',
    py_modules=['ET_Client'],
    packages=['FuelSDK'],
    url='https://github.com/carlosninja/FuelSDK-Python-gn',
    license='MIT',
    install_requires=PACKAGE_INSTALL_REQUIRES,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries',
        'Programming Language :: Python :: 3.10',
    ],
)