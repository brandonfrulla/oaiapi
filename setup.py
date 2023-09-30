from setuptools import setup

setup(
    name='scndLk_cli',
    version='0.1',
    py_modules=['scndLk'],
    entry_points={
        'console_scripts': [
            'scndLk = scndLk:main',
        ],
    },
)