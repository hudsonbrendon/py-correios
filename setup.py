import os
from setuptools import setup, find_packages


DESCRIPTION = "Informações de CEP, encomendas e endereços em poucas linhas de código."

LONG_DESCRIPTION = None
try:
    LONG_DESCRIPTION = open('README.md').read()
except:
    pass


setup(name='py-correios',
      version='0.0.1',
      description='Informações de CEP, encomendas e endereços em poucas linhas de código.',
      url='https://github.com/hudsonbrendon/py-correios',
      author='Hudson Brendon',
      author_email='contato.hudsonbrendon@gmail.com',
      license='MIT',
      packages=find_packages(exclude=['tests*']),
      install_requires=[
          'requests',
      ],
      zip_safe=False)
