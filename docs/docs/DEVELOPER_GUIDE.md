# Developer Notes

## Local Development

```sh
git clone https://github.com/kyleking/tui-typer-tutor.git
cd tui-typer-tutor
poetry install --sync

# See the available tasks
poetry run calcipy
# Or use a local 'run' file (so that 'calcipy' can be extended)
./run

# Run the default task list (lint, auto-format, test coverage, etc.)
./run main

# Make code changes and run specific tasks as needed:
./run lint.fix test
```

## Publishing

For testing, create an account on [TestPyPi](https://test.pypi.org/legacy/). Replace `...` with the API token generated on TestPyPi or PyPi respectively

```sh
poetry config repositories.testpypi https://test.pypi.org/legacy/
poetry config pypi-token.testpypi ...

./run main pack.publish --to-test-pypi
# If you didn't configure a token, you will need to provide your username and password to publish
```

To publish to the real PyPi

```sh
poetry config pypi-token.pypi ...
./run release

# Or for a pre-release
./run release --suffix=rc
```

## Current Status

<!-- {cts} COVERAGE -->
| File                                          |   Statements |   Missing |   Excluded | Coverage   |
|-----------------------------------------------|--------------|-----------|------------|------------|
| `tui_typer_tutor/__init__.py`                 |            2 |         0 |          0 | 100.0%     |
| `tui_typer_tutor/app/__init__.py`             |            0 |         0 |          0 | 100.0%     |
| `tui_typer_tutor/app/ttt.py`                  |            6 |         6 |          0 | 0.0%       |
| `tui_typer_tutor/constants/__init__.py`       |            1 |         0 |          0 | 100.0%     |
| `tui_typer_tutor/constants/seed_data.py`      |            5 |         5 |          0 | 0.0%       |
| `tui_typer_tutor/constants/vim_to_textual.py` |            5 |         0 |          0 | 100.0%     |
| `tui_typer_tutor/core/__init__.py`            |            0 |         0 |          0 | 100.0%     |
| `tui_typer_tutor/core/scrolled_labels.py`     |            0 |         0 |          0 | 100.0%     |
| `tui_typer_tutor/core/typing.py`              |           69 |         0 |          0 | 100.0%     |
| `tui_typer_tutor/screens/__init__.py`         |            0 |         0 |          0 | 100.0%     |
| `tui_typer_tutor/screens/main.py`             |           53 |        53 |          0 | 0.0%       |
| `tui_typer_tutor/scripts.py`                  |            6 |         6 |          6 | 0.0%       |
| **Totals**                                    |          147 |        70 |          6 | 52.8%      |

Generated on: 2023-06-25
<!-- {cte} -->
