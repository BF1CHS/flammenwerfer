> [!NOTE]
> This project is migrated from [zyf722/flamethrower](https://github.com/zyf722/flamethrower).
> 
> For versions `v0.1.6` and earlier, please visit [Releases of that repository](https://github.com/zyf722/flamethrower/releases).
>
> **Starting from version `v0.1.7`, this project is renamed `flammenwerfer` to avoid naming conflicts with other projects.**

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

Examples of how to use the package are available in the `examples` directory. There is only one example now, which is an interactive toolbox for Chinese localization of Battlefield 1 (with UI in Chinese). More examples are welcomed.

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