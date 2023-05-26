# pycontent-type

<p align="center">
    <em>A Python library to access all Supported Content-Types/Media-Types ⚡</em>
</p>

<p align="center">
<a href="https://github.com/yezz123/pycontent-type/actions/workflows/ci.yml" target="_blank">
    <img src="https://github.com/yezz123/pycontent-type/actions/workflows/ci.yml/badge.svg" alt="lint">
</a>
<a href="https://pypi.org/project/pycontent-type" target="_blank">
    <img src="https://img.shields.io/pypi/v/pycontent-type?color=%2334D058&label=pypi%20package" alt="Package version">
</a>
<a href="https://codecov.io/gh/yezz123/pycontent-type">
    <img src="https://codecov.io/gh/yezz123/pycontent-type/branch/main/graph/badge.svg"/>
</a>
</p>

## Installation

You can add pycontent-type in a few easy steps. First of all, install the dependency:

```shell
$ pip install pycontent-type

---> 100%

Successfully installed pycontent-type
```

## Usage

We have a simple API to access all the supported content-types:

As known the categories of content-types are:

- `application`
- `audio`
- `font`
- `image`
- `message`
- `model`
- `multipart`
- `text`
- `video`

### Get Content-Type by extension

```python
# Get content-type for application
import pycontent_type

len(pycontent_type.application)

>>> 1551

# Get content-type for specific extension using Name
pycontent_type.application.get(Name='json')

>>> application(Name='json', Template='application/json')

# Get content-type for specific extension using Template
pycontent_type.application.get(Template='application/xml')

>>> application(Name='xml', Template='application/xml')
```

The same applies for all the categories, we have 2 ways to get the content-type:

- Using `Name` attribute
- Using `Template` attribute

## Development 🚧

### Setup environment 📦

You should create a virtual environment and activate it:

```bash
python -m venv venv/
```

```bash
source venv/bin/activate
```

And then install the development dependencies:

```bash
# Install dependencies
pip install -e .[test,lint]
```

### Run tests 🌝

You can run all the tests with:

```bash
bash scripts/test.sh
```

### Format the code 🍂

Execute the following command to apply `pre-commit` formatting:

```bash
bash scripts/format.sh
```

## License

This project is licensed under the terms of the MIT license.