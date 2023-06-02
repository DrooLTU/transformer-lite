from setuptools import setup

setup(
    name='your-library',
    version='0.1.0',
    author='Justinas Karaliunas',
    author_email='your@email.com',
    description='A short description of your library',
    long_description='A longer description of your library',
    long_description_content_type='text/markdown',
    url='https://github.com/your-username/your-library',
    packages=['your_library'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires='>=3.6',
    install_requires=[
        'numpy>=1.18.0',
        'requests>=2.25.0',
    ],
    extras_require={
        'dev': [
            'pytest>=6.0.0',
            'coverage>=5.3',
        ],
    },
)