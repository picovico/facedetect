"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

install_requires = [
    'six', 
    'numpy',
    'opencv-python'
    ]

tests_require = [
    # 'pytest-mock',
    # 'pytest-cov',
    ]

setup(
    name='facedetectpy',
    packages=['facedetect', ],
    scripts=['bin/facedetect'],
    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='1.0.5',

    description='Facedetect Library for Python (Originally by wave++ "Yuri D\'Elia" <wavexx@thregr.org>)',
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/picovico/facedetect-py',

    # Author details
    author='Picovico (originally authored by wave++)',
    author_email='info@picovico.com',

    # Choose your license
    license='GPLv2+',
    install_requires = install_requires,
    tests_require = tests_require,

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 5 - Production/Stable',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    setup_requires=['pytest-runner'],

    # What does your project relate to?
    keywords='facedetect wave++ picovico slideshow-maker video-maker sdk',
)
