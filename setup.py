from setuptools import setup, find_packages

setup(
    name='venvat',
    version='0.2.18',
    description='A script to activate Python virtual environments.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Kelocker',
    author_email='thekelvin0fficials@gmail.com',
    license='MIT',
    url='https://github.com/Kelocker/venvat.git',
    project_urls={
        'Homepage': 'https://github.com/Kelocker/venvat.git',
        'Issues': 'https://github.com/Kelocker/venvat.git/issues'
    },
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    entry_points={
    'console_scripts': [
        'venvat=venvat.venvat_runner:main'
        ]
    },
    scripts=['scripts/venvat.ps1'],
)
