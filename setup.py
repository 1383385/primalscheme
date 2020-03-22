from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='primalscheme',
    version='0.2.1',
    author='Josh Quick',
    author_email='j.quick@bham.ac.uk',
    license='GPL',
    description='A tool for designing multiplex PCR primers for generating '
                ' tiling amplicons.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/aresti/primalscheme',
    packages=find_packages(),
    install_requires=[
          'biopython>=1,<2',
          'Cython>=0,<1',
          'primer3-py>=0,<1',
          'reportlab>=3,<4',
          'Porechop @ git+https://github.com/joshquick/Porechop'
      ],
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
