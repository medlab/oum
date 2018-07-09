import pathlib
from distutils.core import setup

setup(
    name='oum',
    version='0.99.1',
    description='Object<-->UI Automation Map',
    long_description=pathlib.Path('readme.rst').read_text(encoding='utf-8'),
    install_requires=[
        'selenium',
    ],
    packages=['oum'],
    url='https://github.com/medlab/oum',
    license='BSD 3-Clause "New" or "Revised" License',
    author='Cong Zhang',
    author_email='congzhangzh@gmail.com',
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Testing',
    ],
)