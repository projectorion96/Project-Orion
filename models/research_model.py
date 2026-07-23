from dataclasses import dataclass, field
from typing import List


@dataclass
class ResearchReport:
    title: str
    category: str

    summary: str = ""

    key_points: List[str] = field(default_factory=list)

    people: List[str] = field(default_factory=list)

    organizations: List[str] = field(default_factory=list)

    keywords: List[str] = field(default_factory=list)

    sources: List[str] = field(default_factory=list)