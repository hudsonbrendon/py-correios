# Pycorreios

Informações de CEP, encomendas e endereços em poucas linhas de código.

[![Build Status](https://travis-ci.org/hudsonbrendon/py-correios.svg?branch=master)](https://travis-ci.org/hudsonbrendon/py-correios)
[![Github Issues](http://img.shields.io/github/issues/hudsonbrendon/py-correios.svg?style=flat)](https://github.com/hudsonbrendon/py-correios/issues?sort=updated&state=open)
![MIT licensed](https://img.shields.io/badge/license-MIT-blue.svg)

# Instalação

```bash
$ pip install py-correios
```
ou

```bash
$ python setup.py install
```

# Modo de uso

## CEPs

A biblioteca disponibiliza o método **cep** que retorna os dados de um endereço como é mostrado abaixo:

```python
>>> from correios import Correios

>>> Correios().cep('59142070')
```

ou

```python
>>> from correios import Correios

>>> correios = Correios()

>>> correios.cep('59142070')
```

## Encomendas

A biblioteca disponibiliza o método **encomenda** que retorna os dados de uma encomenda como é mostrado abaixo:

```python
>>> from correios import Correios

>>> Correios().encomenda('RY508958848CN')
```
ou

```python
>>> from correios import Correios

>>> correios = Correios

>>> correios.encomenda('RY508958848CN')
```

# Como contribuir?

Clone o projeto no seu PC:

```bash
$ git clone https://github.com/hudsonbrendon/py-correios.git
```

Certifique-se de que o [Pipenv](https://github.com/kennethreitz/pipenv) está instalado, caso contrário:

```bash
$ pip install -U pipenv
```

No diretório py-correios instale as dependências executando o comando abaixo:

```bash
$ pipenv install --dev
```

# Licença

[MIT](http://en.wikipedia.org/wiki/MIT_License)
