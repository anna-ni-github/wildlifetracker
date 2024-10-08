from typing import Any, List, Optional

from wildlife_tracker.animal import Animal

class AnimalManager:
    def __init__(self):
        self.animals: dict[int, Animal] = {}

    def get_animal_by_id(self, animal_id: int) -> Optional[Animal]:
        pass

    def register_animal(self, Animal) -> None:
        pass

    def remove_animal(self, animal_id: int) -> None:
        pass
