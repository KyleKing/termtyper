## Unreleased

## 1.1.0 (2023-07-07)

### Feat

- expand default seed data
- keep text centered on many deletes
- add VHS demo
- switch to arguably for the CLI

### Fix

- cleanup demo tape
- ignore bound keys from metrics

## 1.0.1 (2023-06-27)

### Fix

- add missing platformdirs dependency

## 1.0.0 (2023-06-27)

### Feat

- better handle edge cases
- add user configurable --seed-file
- add uninstall and test metrics
- implement save metrics
- load seed data from default file
- use the actual character width per Key when displaying
- implement an MVP of the TUI
- merge runnable version of termtyper
- rename to tui-typer-tutor to avoid confusion with terminal-typing-tutor
- initialize with calcipy template

### Fix

- center the typed text
- catch at the end of the input
- show whitespace as a block for the fill color to work
- remove accumulator for multi-width keys
- drop Vim bindings and being enforcing single character width Keys
- test the UI and resolve minor bugs
- correctly parse the adjusted index
- restore latest textual

### Refactor

- move whitespace logic to the GUI
- try to
- initial support for multi-char text & remove focus toggle
- delete invoke task logic and use argparse like tail-jsonl
- remove legacy code with event references
- remove pre-ttt code
- remove sounds
- run automated tooling

## 0.0.0 (2023-06-24)

### Feat

- Add `-q` flag for quiet mode (closes #12)
- `Time/Word` progress
- dim untyped-characters
- Add g and G keybindings for `getting started`
- Add mode change menu
- Add timeout menu
- Add timer mode
- Add shortcuts for numbers and punctuations
- Escape to close floating menu + live change display
- Better config
- Toggle details for race bar
- New word generator
- better parser
- Bar theme change on the fly!
- Add multiple-themed progress bars
- Add size change menu
- UI improvements
- monkeytype typing UI
- Add MinimalScrollView
- Add main screen menu
- better option menu
- Add getting started menu and remove quit button
- add `ctrl+l` for sentence deletetion (for #10)
- Update lockfile
- Add `ctrl+w` for deleting a word for #1
- Add key-bindings for navigation (closes #3)
- Add vim/arrow keys keybindings in main menu
- Update speed measurement for different size paragraphs
- Add keypress sounds
- Add min burst
- Add Difficulty mode
- Add Confidence mode
- Add typing results + racebar sync fix
- Now race bar moves with the screen
- Read and Write settings data from .ini
- add Chomsky :)
- Improve Settings + Refactor
- Add Number scroll + Some Improvements
- Add parser
- Improvements +  More Widgets
- Improve button + Main Menu layout added
- Add Button class
- Add Screen Skeleton code + RaceBar

### Fix

- toggle numbers and punctuations not working  (closes #42)
- Module not found (for #19)
- > 100% accuracy
- AUR package
- keypress_sound setting not working!
- unclear instruction in help menu (closes #18)
- Update `discord` link
- Timer not stopping on finish
- caret setting not working
-  Menu option fallback
- Setting missing from menu + some code refactor
- incorrect bar theme menu default value
- App crash on pressing `Esc` in main menu
- Bar reset on completing typing
- Broken live changes on race bar
- Update help menu to new keybindings
- Bar not resetting after mode change
- broken racebar render
- remove punctuation words from text file
- paragraph size change + code refactor
- playsound
- Vertical alignment of remarks on completion
- Keypress sound not working issue #4
- `cursor buddy speed` not changing
- RaceBar remarks not visible on completion
- Tab Reset Bug
- Sound location error
- make compatible with python 3.9
- Sound location error
- Race bar not resetting
- escape fix for typing screen + remarks on finishing
- Typos
- race bar not responding on fail
- classmethod clash

### Refactor

- instance re-use
- Add banner class
