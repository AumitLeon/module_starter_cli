from setuptools import setup

# Should match git tag
VERSION = '0.1.1'

def readme():
    with open('README.md') as f:
        return f.read()

with open('requirements.txt') as file:
    REQUIRED_MODULES = [line.strip() for line in file]

with open('requirements-dev.txt') as file:
    DEVELOPMENT_MODULES = [line.strip() for line in file]


setup(name='module-starter.leon',
      version=VERSION,
      description='Starter project for python modules',
      long_description=readme(),
      keywords='module starter',
      url='https://github.com/AumitLeon/module_starter_cli',
      author='Aumit Leon',
      author_email='aumitleon@gmail.com',
      packages=['src'],
      install_requires=REQUIRED_MODULES,
      extras_require={'dev': DEVELOPMENT_MODULES},
      entry_points={
          'console_scripts': ['command=src.command_line:main'],
      },
      include_package_data=True)
