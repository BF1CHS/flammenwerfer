> [!NOTE]
> This project is migrated from [zyf722/flamethrower](https://github.com/zyf722/flamethrower).
> 
> For versions `v0.1.6` and earlier, please visit [Releases of that repository](https://github.com/zyf722/flamethrower/releases).
>
> **Starting from version `v0.1.7`, this project is renamed `flammenwerfer` to avoid naming conflicts with other projects.**

[![License](https://img.shields.io/github/license/BF1CHS/flammenwerfer)](./LICENSE)
[![PyPI version](https://img.shields.io/pypi/v/flammenwerfer)](https://pypi.org/project/flammenwerfer/)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/flammenwerfer)

# flammenwerfer
> 🔥 ***Flammenwerfer*** (*flamethrower* in German), where ❄️ ***Frostbite*** meets the dance of inferno.

`flammenwerfer` is a Python package designed to provide a simple interface for modders to interact with the original Frostbite engine binaries. 

## Installation
```shell
pip install flammenwerfer
```

In case you use Poetry:
```shell
poetry add flammenwerfer
```

## Usage
The package only supports the following features now:

- `flammenwerfer.hash`: Hash functions used by the Frostbite engine. Currently, only FNV series hash functions (`flammenwerfer.hash.fnv`) are supported.
- `flammenwerfer.localization`: Interface for `Histogram` and `LocalizationBinary` files.

Currently no documentation is available since the package is still in its early stages of development. However, [BF1CHS/bf1chs](https://github.com/BF1CHS/bf1chs) (a toolbox for Simplified Chinese localization of Battlefield 1) could be checked for some examples of usage. More examples are welcomed.

## Contributing
Though the package is still in its early stages of development, [Pull Requests](https://github.com/BF1CHS/flammenwerfer/pulls) are welcome.

You can setup your own copy of the source code with Git and [Poetry](https://python-poetry.org/):

```shell
# Git
git clone https://github.com/BF1CHS/flammenwerfer.git
cd flammenwerfer/

# Poetry
poetry lock
poetry install
poetry shell
```

It is strongly recommended to follow the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) specification when writing commit messages and creating pull requests.

## License
[GPL-3.0](/LICENSE)