from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='python_grund_kurs',
    version='1.0.0',
    author='Julia Imlauer',
    author_email='info@linkedinlearning.com',
    description='Beispielcode für das LinkedIn Learning Kurs: Python Grundkurs',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/LinkedInLearning/python-grundkurs-2685000',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    install_requires=requirements,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Specify Python version requirement
)
