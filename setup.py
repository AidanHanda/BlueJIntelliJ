from setuptools import setup
setup(
    name = 'BlueJIntelliJ',
    description='Converts BlueJ Projects to IntelliJ projects',
    author='Aidan Handa',
    version = '0.1.0',
    packages = ['BlueJIntelliJ'],
    install_requires=[
          'click',
      ],
    entry_points = {
        'console_scripts': [
            'BlueJIntelliJ = BlueJIntelliJ.__main__:main'
        ]
    })