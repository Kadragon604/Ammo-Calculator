"""Weapon module"""

import json
from os import path, getcwd
from math import ceil

__location__ = path.realpath(
    path.join(getcwd(), path.dirname(__file__)))

with open(path.join(__location__, 'perks.json'), encoding="utf-8") as json_f:
    json_data = json.load(json_f)
    overflow_perks = json_data["overflowing_perks"]
    generate_perks = json_data["generating_perks"]


class Weapon():
    """ WIP
    """
    def __init__(self, magazine: int, reserves: int,
                 overflow: bool, perks: list):
        self.magazine = magazine
        self.reserves = reserves
        self.overflow = overflow
        self.perks = perks.copy()

    @property
    def magazine(self) -> int:
        """magazine property

        Returns:
            int: _description_
        """
        return self._magazine

    @magazine.setter
    def magazine(self, magazine: int) -> None:
        if not isinstance(magazine, int):
            raise TypeError("Magazine must be an int.")
        if magazine <= 0:
            raise ValueError("Magazine must be positive.")
        self._magazine = magazine

    @property
    def reserves(self) -> int:
        """reserves property

        Returns:
            int: reserves value
        """
        return self._reserves

    @reserves.setter
    def reserves(self, reserves: int) -> None:
        if not isinstance(reserves, int):
            raise TypeError("reserves must be an int.")
        if not isinstance(self._magazine, int):
            raise ValueError("magazine must be defined before reserves")
        if reserves < self._magazine:
            raise ValueError("reserves must not be less than magazine")
        self._reserves = reserves

    @property
    def overflow(self) -> bool:
        """ overflow propety

        Returns:
            bool: overflow status
        """
        return self._overflow

    @overflow.setter
    def overflow(self, overflow: bool) -> None:
        if not isinstance(overflow, bool):
            raise TypeError("overflow must be a bool")
        self._overflow = overflow

    @property
    def perks(self) -> list:
        """ perks property

        Returns:
            list: list of weapon perks
        """
        return self._perks

    @perks.setter
    def perks(self, perks: list) -> None:
        if not isinstance(perks, list):
            raise TypeError("perks must be a list")
        if not set(perks).issubset([*overflow_perks, *generate_perks]):
            raise ValueError("perks must contain only valid perks")
        self._perks = perks.copy()

    @property
    def max_magazine(self) -> int:
        """ max magazine property

        Returns:
            int: max rounds in magazine based off overflow percentage
        """
        percentage = max([overflow_perks.get(perk, 0) for perk in self._perks])
        max_mag = int(ceil((percentage + 100) * self._magazine / 100))
        return min([max_mag, self._reserves])
