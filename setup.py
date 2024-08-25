from setuptools import setup, find_packages

setup(
    name='sql-injection-tool',
    version='1.0.0',
    description='A tool for detecting and exploiting SQL injections, with a dashboard interface',
    author='Jacob Thomas Messer',
    author_email='alistairbiltmore@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'requests',
        'beautifulsoup4',
        'pyarmor',
        'pyinstaller',
        'aiohttp',
        'tqdm',
        'scikit-learn',
        'keras',
        'PyYAML',
        'graphene',
        'flask',
        'flask-graphql',
        'flask-cors'
    ],
    entry_points={
        'console_scripts': [
            'sql-injection-tool=unified_script:main',
        ],
    },
)
