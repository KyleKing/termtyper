from os import path
from threading import Thread

from ..utils.parser import MAIN_PARSER
from .preferredsoundplayer import playsound

SOUNDS_LOC = path.join(path.dirname(__file__), '..', 'sounds')


def get_sound_location(sound: str) -> str:
    return str(path.join(SOUNDS_LOC, f'{sound}.wav'))


def play(sound_file: str) -> None:
    Thread(target=playsound, args=(sound_file,), daemon=True).start()


def play_keysound() -> None:
    sound = MAIN_PARSER.get_theme('sound')
    sound_file = get_sound_location(sound)
    play(sound_file)


def play_failed() -> None:
    sound_file = get_sound_location('failed')
    play(sound_file)
