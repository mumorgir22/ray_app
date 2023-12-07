from enum import Enum


class RedisKeys:
    def __init__(self, enum_: Enum) -> None:
        self.tasks_key = enum_.value.lower()
