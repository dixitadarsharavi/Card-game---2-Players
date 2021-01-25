from setuptools import setup
setup(
    name = 'cardgamecli',
    version = '0.1.0',
    packages = ['cardgamecli'],
    entry_points = {
        'console_scripts': [
            'cardgamecli = cardgamecli.__main__:main'
        ]
    })