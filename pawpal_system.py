from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Pet:
    name: str
    species: str

    def get_description(self) -> str:
        """Return a short description of the pet."""
        raise NotImplementedError


@dataclass
class Task:
    title: str
    duration_minutes: int
    priority: str

    def get_details(self) -> str:
        """Return a short summary of the task."""
        raise NotImplementedError


@dataclass
class Schedule:
    day_of_week: str
    time_of_day: str
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        raise NotImplementedError

    def remove_task(self, task: Task) -> None:
        raise NotImplementedError

    def get_tasks(self) -> List[Task]:
        raise NotImplementedError


class Owner:
    def __init__(self, name: str) -> None:
        self.name = name
        self.pets: List[Pet] = []
        self.schedule: Optional[Schedule] = None

    def add_pet(self, pet: Pet) -> None:
        raise NotImplementedError

    def add_task(self, task: Task) -> None:
        raise NotImplementedError

    def get_schedule(self) -> Optional[Schedule]:
        raise NotImplementedError
