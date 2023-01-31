from setuptools import setup, find_packages

setup(
    name='books',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
        'flask-sqlalchemy',
        'Jinja2',
    ],
)
