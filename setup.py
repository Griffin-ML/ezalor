from setuptools import setup

setup(
    name='ezalor',
    version='0.1.0',    
    description='Keeper of the Libraries',
    url='https://github.com/shuds13/pyexample',
    author='Calvin Tran',
    author_email='',
    license='BSD 2-clause',
    packages=['ezalor'],
    install_requires=[
        'numpy',
        'pyhive',
        'pandas'
    ],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 3',
    ],
)
