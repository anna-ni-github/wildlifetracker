from typing import Any, Optional


class Animal:
    def __init__(self, 
                 animal_id: int, 
                 species: str, 
                 age: Optional[int] = None, 
                 health_status: Optional[str] = None) -> None:
        self.animal_id: int = animal_id
        self.species: str = species
        self.age: Optional[int] = age #TODO or []
        self.health_status: Optional[str] = health_status

    def get_animal_details(animal_id) -> dict[str, Any]:
        pass

    def update_animal_details(animal_id: int, **kwargs: Any) -> None:
        pass
