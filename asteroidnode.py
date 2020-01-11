
import globals as g
import math

class AsteroidNode :

    def __init__(self, priority, dx, dy) :
        self.dx = dx
        self.dy = dy
        self.priority = priority

    def __lt__(self, other) :
        return self.priority < other.priority