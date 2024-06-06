from setuptools import setup

setup(
    name='Python Simple Notebook',
    version='1.0.0',
    description='A Simple Notebook Application in Python, for internat content and file sharing.',
    author='Hegw',
    author_email='hegw@outlook.com',
    url='https://github.com/hegwout/pynb',
    packages=['pynb'],
    install_requires=[
        'flask'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)