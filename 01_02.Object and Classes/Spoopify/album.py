from song import Song
from typing import Tuple, List


class Album:
    def __init__(self, name: str, *songs: Tuple[Song]):
        self.name = name
        self.published = False
        self.songs: List[Song] = [*songs]

    def add_song(self, song: Song):

