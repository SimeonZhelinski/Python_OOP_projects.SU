from project.band_members.singer import Singer
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band import Band
from project.concert import Concert


class ConcertTrackerApp:
    VALID_MUSICIAN = ["Guitarist", "Drummer", "Singer"]

    def __init__(self):
        self.bands = []
        self.musicians = []
        self.concerts = []

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in self.VALID_MUSICIAN:
            raise ValueError("Invalid musician type!")
        for musician in self.musicians:
            if musician.name == name:
                raise Exception(f"{name} is already a musician!")

        current_musician = None

        if musician_type == "Guitarist":
            current_musician = Guitarist(name, age)
        if musician_type == "Drummer":
            current_musician = Drummer(name, age)
        if musician_type == "Singer":
            current_musician = Singer(name, age)

        self.musicians.append(current_musician)
        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        for band in self.bands:
            if band.name == name:
                raise Exception(f"{name} band is already created!")

        self.bands.append(Band(name))
        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        for con in self.concerts:
            if con.place == place:
                raise Exception(f"{place} is already registered for {con.genre} concert!")

        self.concerts.append(Concert(genre, audience, ticket_price, expenses, place))
        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        current_musician = None
        current_band = None

        for musician in self.musicians:
            if musician.name == musician_name:
                current_musician = musician
        if not current_musician:
            raise Exception(f"{musician_name} isn't a musician!")

        for band in self.bands:
            if band.name == band_name:
                current_band = band
        if not current_band:
            raise Exception(f"{band_name} isn't a band!")

        current_band.members.append(current_musician)
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        current_musician = None
        current_band = None

        for band in self.bands:
            if band.name == band_name:
                current_band = band
        if not current_band:
            raise Exception(f"{band_name} isn't a band!")

        for member in current_band.members:
            if member.name == musician_name:
                current_musician = member
        if not current_musician:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

        current_band.members.remove(current_musician)
        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):
        current_band = next(filter(lambda b: b.name == band_name, self.bands))
        guitar_count = 0
        drummer_count = 0
        singer_count = 0
        for member in current_band.members:
            if member.__class__.__name__ == "Guitarist":
                guitar_count += 1
            if member.__class__.__name__ == "Drummer":
                drummer_count += 1
            if member.__class__.__name__ == "Singer":
                singer_count += 1

        if guitar_count < 1 or drummer_count < 1 or singer_count < 1:
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        current_concert = next(filter(lambda c: c.place == concert_place, self.concerts))

        if current_concert.genre == "Rock":
            for member in current_band.members:
                if member.__class__.__name__ == "Drummer":
                    if "play the drums with drumsticks" not in member.skills:
                        raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if member.__class__.__name__ == "Singer":
                    if "sing high pitch notes" not in member.skills:
                        raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if member.__class__.__name__ == "Guitarist":
                    if "play rock" not in member.skills:
                        raise Exception(f"The {band_name} band is not ready to play at the concert!")

        if current_concert.genre == "Metal":
            for member in current_band.members:
                if member.__class__.__name__ == "Drummer":
                    if "play the drums with drumsticks" not in member.skills:
                        raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if member.__class__.__name__ == "Singer":
                    if "sing low pitch notes" not in member.skills:
                        raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if member.__class__.__name__ == "Guitarist":
                    if "play metal" not in member.skills:
                        raise Exception(f"The {band_name} band is not ready to play at the concert!")

        if current_concert.genre == "Jazz":
            for member in current_band.members:
                if member.__class__.__name__ == "Drummer":
                    if "play the drums with drum brushes" not in member.skills:
                        raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if member.__class__.__name__ == "Singer":
                    if "sing high pitch notes" and "sing low pitch notes" not in member.skills:
                        raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if member.__class__.__name__ == "Guitarist":
                    if "play jazz" not in member.skills:
                        raise Exception(f"The {band_name} band is not ready to play at the concert!")

        profit = (current_concert.audience * current_concert.ticket_price) - current_concert.expenses
        return f"{band_name} gained {profit:.2f}$ from the {current_concert.genre} concert in {concert_place}."
