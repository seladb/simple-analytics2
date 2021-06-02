from dataclasses import dataclass
from typing import Optional


@dataclass()
class Job:
    id: int


class JobQueue:
    def __init__(self):
        pass

    def enqueue(self, job: Job):
        pass

    def dequeue(self) -> Optional[Job]:
        return None
