from wildlife_tracker.migration_path import MigrationPath
from wildlife_tracker.habitat import Habitat

class Migration:

    def __init__(self, 
                 migration_id: int, 
                 migration_path: MigrationPath, 
                 start_date: str, 
                 status: str = "Scheduled"):
        self.migration_id: int = migration_id
        self.migration_path: MigrationPath = migration_path
        self.start_date: str = start_date
        self.status: str = status
        self.current_location: str = ""
        self.destination: Habitat = None
        self.duration: int = None

    def get_migration_details(migration_id: int) -> dict[str, Any]:
        pass

    def update_migration_details(migration_id: int, **kwargs: Any) -> None:
        pass