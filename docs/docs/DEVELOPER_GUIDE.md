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
| File                                               |   Statements |   Missing |   Excluded | Coverage   |
|----------------------------------------------------|--------------|-----------|------------|------------|
| `tui_typer_tutor/__init__.py`                      |            2 |         0 |          0 | 100.0%     |
| `tui_typer_tutor/app/__init__.py`                  |            0 |         0 |          0 | 100.0%     |
| `tui_typer_tutor/app/typer.py`                     |            8 |         8 |          0 | 0.0%       |
| `tui_typer_tutor/cli.py`                           |            7 |         7 |          1 | 0.0%       |
| `tui_typer_tutor/constants/__init__.py`            |            1 |         1 |          0 | 0.0%       |
| `tui_typer_tutor/constants/vim_to_textual.py`      |            4 |         4 |          0 | 0.0%       |
| `tui_typer_tutor/events/__init__.py`               |            2 |         2 |          0 | 0.0%       |
| `tui_typer_tutor/events/events.py`                 |           34 |        34 |          0 | 0.0%       |
| `tui_typer_tutor/keys.py`                          |           29 |        29 |          0 | 0.0%       |
| `tui_typer_tutor/screens/__init__.py`              |            0 |         0 |          0 | 100.0%     |
| `tui_typer_tutor/screens/main.py`                  |           61 |        61 |          0 | 0.0%       |
| `tui_typer_tutor/scripts.py`                       |            7 |         7 |          0 | 0.0%       |
| `tui_typer_tutor/tasks/__init__.py`                |            0 |         0 |          0 | 100.0%     |
| `tui_typer_tutor/tasks/all_tasks.py`               |           18 |        18 |          0 | 0.0%       |
| `tui_typer_tutor/ui/__init__.py`                   |            2 |         2 |          0 | 0.0%       |
| `tui_typer_tutor/ui/settings_options.py`           |          114 |       114 |          0 | 0.0%       |
| `tui_typer_tutor/ui/tui.py`                        |          161 |       161 |          0 | 0.0%       |
| `tui_typer_tutor/ui/widgets/__init__.py`           |            7 |         7 |          0 | 0.0%       |
| `tui_typer_tutor/ui/widgets/banner.py`             |            5 |         5 |          0 | 0.0%       |
| `tui_typer_tutor/ui/widgets/button.py`             |           30 |        30 |          0 | 0.0%       |
| `tui_typer_tutor/ui/widgets/menu.py`               |           70 |        70 |          0 | 0.0%       |
| `tui_typer_tutor/ui/widgets/menus.py`              |           35 |        35 |          0 | 0.0%       |
| `tui_typer_tutor/ui/widgets/minimal_scrollview.py` |           37 |        37 |          0 | 0.0%       |
| `tui_typer_tutor/ui/widgets/number_scroll.py`      |           47 |        47 |          0 | 0.0%       |
| `tui_typer_tutor/ui/widgets/option.py`             |           77 |        77 |          0 | 0.0%       |
| `tui_typer_tutor/ui/widgets/progress_bar.py`       |           48 |        48 |          0 | 0.0%       |
| `tui_typer_tutor/ui/widgets/race_hud.py`           |           84 |        84 |          0 | 0.0%       |
| `tui_typer_tutor/ui/widgets/screen.py`             |          233 |       233 |          0 | 0.0%       |
| `tui_typer_tutor/utils/__init__.py`                |            5 |         5 |          0 | 0.0%       |
| `tui_typer_tutor/utils/generator.py`               |           34 |        34 |          0 | 0.0%       |
| `tui_typer_tutor/utils/getting_started.py`         |           26 |        26 |          0 | 0.0%       |
| `tui_typer_tutor/utils/help_menu.py`               |           15 |        15 |          0 | 0.0%       |
| `tui_typer_tutor/utils/parser.py`                  |           91 |        91 |          0 | 0.0%       |
| `tui_typer_tutor/utils/words.py`                   |            1 |         1 |          0 | 0.0%       |
| **Totals**                                         |         1295 |      1293 |          1 | 0.1%       |

Generated on: 2023-06-24
<!-- {cte} -->
