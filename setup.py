from setuptools import setup

setup(
  name="cli",
  version='1.0',
  py_modules=['cli'],
  install_requires=[
    'click', 'pyserial'
  ],
  entry_points='''
        [console_scripts]
        cli = cli:cli
    '''
)
