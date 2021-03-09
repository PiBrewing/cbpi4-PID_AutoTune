from setuptools import setup

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='cbpi4-PID_AutoTune',
      version='0.0.2',
      description='CraftBeerPi4 Kettle Logic for PID Auto Tune',
      author='Alexander Vollkopf',
      author_email='avollkopf@web.de',
      url='https://github.com/avollkopf/cbpi4-PIDAutoTune',
      license='GNU General Public License v3 (GPLv3)',
      include_package_data=True,
      package_data={
        # If any package contains *.txt or *.rst files, include them:
      '': ['*.txt', '*.rst', '*.yaml'],
      'cbpi4-PID_AutoTune': ['*','*.txt', '*.rst', '*.yaml']},
      packages=['cbpi4-PID_AutoTune'],
      long_description=long_description,
      long_description_content_type='text/markdown'
      )
