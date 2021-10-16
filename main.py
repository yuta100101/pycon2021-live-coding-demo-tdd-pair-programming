from __future__ import annotations

from abc import ABCMeta, abstractmethod
from dataclasses import dataclass


@dataclass(frozen=True)
class Range(metaclass=ABCMeta):
    lower_endpoint: int
    upper_endpoint: int

    def __post_init__(self) -> None:
        if self.lower_endpoint >= self.upper_endpoint:
            raise ValueError()

    def __str__(self) -> str:
        return f"[{self.lower_endpoint},{self.upper_endpoint}]"

    @abstractmethod
    def contains(self, target: int) -> bool:
        pass

    def is_connected_to(self, target: ClosedRange) -> bool:
        return self.contains(target.lower_endpoint) or self.contains(
            target.upper_endpoint
        )


class ClosedRange(Range):
    def contains(self, target: int) -> bool:
        return self.lower_endpoint <= target <= self.upper_endpoint


class OpenedRange(Range):
    def contains(self, target: int) -> bool:
        return self.lower_endpoint < target < self.upper_endpoint
