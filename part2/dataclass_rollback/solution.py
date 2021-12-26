import datetime
from dataclasses import dataclass, field
from typing import Optional, List


class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
