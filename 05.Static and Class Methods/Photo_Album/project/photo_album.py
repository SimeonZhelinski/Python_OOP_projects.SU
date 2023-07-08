from typing import List
import math


class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages = pages
        self.photos: List[List[str]] = self.__initialize_photos()
        self.current_row_index = 0

    def __initialize_photos(self):
        matrix = []
        for i in range(self.pages):
            matrix.append([])
        return matrix

    @classmethod
    def from_photos_count(cls, photos_count: int):
        pages = math.ceil(photos_count / 4)
        return cls(pages)

    def add_photo(self, label: str):
        if len(self.photos[self.current_row_index]) == 4:
            self.current_row_index += 1
        try:
            self.photos[self.current_row_index].append(label)
            return f"{label} photo added successfully on page {self.current_row_index + 1} slot " \
                   f"{len(self.photos[self.current_row_index])}"
        except IndexError:
            return "No more free slots"

    def display(self):
        res = "-" * 11 + "\n"
        for page in self.photos:
            res += " ".join(["[]" for photo_name in page]) + "\n"
            res += "-" * 11 + "\n"
        return res[:-1]
