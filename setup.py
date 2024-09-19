from setuptools import setup, find_packages

setup(
    name='skynetapi',
    version='0.1.0',
    packages=find_packages(exclude=['utils', 'utils.*', 'request._request']),
    install_requires=[
        'requests>=2.25.0',
    ],
    python_requires='>=3.10',
    author='Dylan Dutton',
    description='A Python package for interacting with the Skynet API',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/astrodyl/skynet-api',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
