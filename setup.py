from setuptools import setup, find_packages
import sys, os

version = '0.0.1'

setup(name='slack-bot',
      version=version,
      description="Slack Bot",
      long_description="""\
Slack Bot""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='slack bot',
      author='mihyaeru21',
      author_email='mihyaeru21@gmail.com',
      url='',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
