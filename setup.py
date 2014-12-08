# coding:utf-8

import sys
from setuptools import setup, find_packages


setup(name='pylemma',
      version='1.0.6',
      description='Mailgun Cryptographic Tools',
      long_description=open('README.rst').read(),
      classifiers=[],
      keywords='',
      author='Mailgun Inc.',
      author_email='admin@mailgunhq.com',
      url='http://www.mailgun.net',
      license='Apache 2',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      tests_require=[
          'nose',
          'mock'
      ],
      install_requires=[
          'expiringdict>=1.1.3',
          'cryptography>=0.5.1',
          'pynacl>=0.2.3',
      ],
      )
