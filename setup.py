from setuptools import setup
import glob,os

def readme():
      with open('README.md',encoding="utf-8") as f:
        return f.read()

setup(name='scTE-testground',
        version='1.0',
        description='Tool for estimating differential enrichment of Transposable Elements and other highly repetitive regions in single-cell data',
        long_description=readme(),
        classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        ],
        python_requires=">=3.6",
        keywords='..',
        url='..',
        author='..',
        author_email='he_jiangping@grmh-gdl.cn; andrewh@sustech.edu.cn',
        license='..',
        packages=[
          'scTE',
          'scTE.miniglbase',
        ],
        platforms=[
          'Linux',
          'MacOS'
        ],
        install_requires=[
          'argparse','scipy','pandas',
          'numpy','anndata',
        ],
        include_package_data=True,
        zip_safe=False,
        scripts=[
          'bin/scTE_testground',
          'bin/scTE_build_testground',
          'bin/scTEATAC_build_testground',
          'bin/scTEATAC_testground',
        ]
        )
