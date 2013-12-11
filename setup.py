#!/usr/bin/env python
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(name='CastingWords API',
      version='1.0',
      description='CastingWords Transcription API4 Client - order transcripts and view status',
      author='CastingWords',
      author_email='nathan@castingwords.com',
      url='http://www.castingwords.com',
      packages=['castingwords'],
      license='Apache License 2.0',
      keywords='CastingWords transcription api',
      install_requires=[
          "requests >=2.0.0"
      ],
     )
