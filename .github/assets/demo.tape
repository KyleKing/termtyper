# VHS documentation
#
# Run with:
#  vhs < .github/assets/demo.tape
#
# Output:
#   Output <path>.gif               Create a GIF output at the given <path>
#   Output <path>.mp4               Create an MP4 output at the given <path>
#   Output <path>.webm              Create a WebM output at the given <path>
#
# Settings:
#   Set FontSize <number>           Set the font size of the terminal
#   Set FontFamily <string>         Set the font family of the terminal
#   Set Height <number>             Set the height of the terminal
#   Set Width <number>              Set the width of the terminal
#   Set LetterSpacing <float>       Set the font letter spacing (tracking)
#   Set LineHeight <float>          Set the font line height
#   Set Theme <string>              Set the theme of the terminal (JSON)
#   Set Padding <number>            Set the padding of the terminal
#   Set Framerate <number>          Set the framerate of the recording
#   Set PlaybackSpeed <float>       Set the playback speed of the recording
#
# Sleep:
#   Sleep <time>                    Sleep for a set amount of <time> in seconds
#
# Type:
#   Type[@<time>] "<characters>"    Type <characters> into the terminal with a
#                                   <time> delay between each character
#
# Keys:
#   Backspace[@<time>] [number]     Press the Backspace key
#   Down[@<time>] [number]          Press the Down key
#   Enter[@<time>] [number]         Press the Enter key
#   Space[@<time>] [number]         Press the Space key
#   Tab[@<time>] [number]           Press the Tab key
#   Left[@<time>] [number]          Press the Left Arrow key
#   Right[@<time>] [number]         Press the Right Arrow key
#   Up[@<time>] [number]            Press the Up Arrow key
#   Down[@<time>] [number]          Press the Down Arrow key
#   Ctrl+<key>                      Press the Control key + <key> (e.g. Ctrl+C)
#
# Display:
#   Hide                            Hide the subsequent commands from the output
#   Show                            Show the subsequent commands in the output

Output .github/assets/demo.gif
Set PlaybackSpeed 0.5
Set TypingSpeed 50ms

Set Theme "SpaceGray Eighties"
Set FontFamily "Hack Nerd Font Mono"

Set FontSize 13
Set Width 800
Set Height 500

Hide
Type `cd ~/Developer/kyleking/tui-typer-tutor`  Enter  Sleep 500ms
Type `echo 'practice touch typing with any text you want. 1234567890-=_+\][{}|.,<>/:";~. Even with ⏎ (enter) and ␛ (escape) ' > example-file.txt`  Enter  Sleep 500ms
Type `clear`  Enter
Show

Type `poetry run ttt --seed-file='./example-file.txt'`  Enter  Sleep 1500ms
Type `practice touch typing with any text you want.`
Type `` Sleep 200ms
Type ` errors appear in red: `
Type `` Ctrl+r
Type `` Sleep 250ms
Type `` Ctrl+z
Type `` Sleep 250ms
Type `` Backspace 25
Type ` 1234567890-=_+\][{}|.,<>/:";~. Even with `  Enter
Type `` Sleep 100ms
Type ` (enter) and `  Escape
Type `` Sleep 100ms
Type ` (escape)`  Sleep 1000ms
# # FIXME: Typing this last space should exit, but it fails. Using Ctrl+q instead
# Type ` `  Sleep 500ms
Type `` Ctrl+q

Hide
Type `rm ./example-file.txt`  Sleep 10ms  Enter
Show

Type `` Sleep 1000ms
Type `poetry run ttt --help`  Enter  Sleep 750ms
Type `` Enter

Type `` Sleep 750ms
Type `poetry run ttt --version`  Enter  Sleep 1000ms
Type `` Enter
