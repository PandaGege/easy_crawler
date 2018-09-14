# coding:utf8

import os
from setuptools import setup, find_packages

f = open(os.path.join(os.path.dirname(__file__), 'VERSION'))
__version__ = f.read().strip()
f.close()

setup(
    name='easy_crawler',
    version=__version__,
    description='a distributed http request server and client',
    author='regan',
    author_email='x-regan@qq.com',
    maintainer='regan',
    maintainer_email='x-regan@qq.com',
    license='MIT',
    keywords=['http client'],
    url='https://www.baidu.com',
    include_package_data=True,
    packages=find_packages(),
    entry_points={
        'console_scripts': ['ecserver = easy_crawler.crawler_server:execute']
    },
    install_requires=[
        'requests>=2.18.4',
        'pysocks>=1.6.8',
        'kazoo>=2.5.0',
        'grpc>=0.3',
        'lxml>=4.1.1',
        'grpcio_tools>=1.11.0',
        'click>=6.7',
        'psutil>=5.4.6',
    ],
)
