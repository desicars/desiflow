from datetime import time

class Job:
    """Base abstract Job class"""
    start_time: list[time] = []
    name: str

    def run(self) -> None:
        """Run job"""
        ...