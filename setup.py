from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    packages = find_packages(),
    name = 'grepimports',
    version='0.0.1',
    author="Stanislav Doronin",
    author_email="mugisbrows@gmail.com",
    url='https://github.com/mugiseyebrows/grep-imports',
    description="Greps sources for imports and prints dependencies as list of package names",
    long_description = long_description,
    long_description_content_type='text/markdown',
    install_requires = ['importlib_metadata'],
    entry_points={
        'console_scripts': [
            'grepimports = grepimports:main'
        ]
    },
)