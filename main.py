from dataclasses import dataclass


@dataclass(frozen=True)
class ClosedRange:
    lower_endpoint: int
    upper_endpoint: int

    def __post_init__(self) -> None:
        if self.lower_endpoint >= self.upper_endpoint:
            raise ValueError()

    def __str__(self) -> str:
        return f"[{self.lower_endpoint},{self.upper_endpoint}]"
