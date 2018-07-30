from setuptools import setup
setup(
    name = 'BlueJIntelliJ',
    description='Converts BlueJ Projects to IntelliJ projects',
    url="blank",
    author='Aidan Handa',
    author_email='handa.aidan@gmail.com',
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