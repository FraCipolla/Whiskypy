from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='whiskypy',
    url='https://github.com/FraCipolla/whiskypy',
    author='Matteo Cipolla',
    author_email='matcip@hotmail.com',
    # Needed to actually package something
    packages=['whiskypy'],
    # Needed for dependencies
    install_requires=['requests, os'],
    # *strongly* suggested for sharing
    version='0.1',
    # The license can be anything you like
    license='MIT',
    description='A Python openwhisk wrapper',
    # We will also need a readme eventually (there will be a warning)
    long_description=open('README.md').read()
)