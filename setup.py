from setuptools import setup

setup(
    name='vendor',
    version="0.0.4",
    description='Makes all modules and packages in the folder '
                'find each other first, before trying to check sys.path',
    long_description='',
    author='Heorhi Samushyia',
    py_modules=["vendor"],
    install_requires=[],
    zip_safe=False
)