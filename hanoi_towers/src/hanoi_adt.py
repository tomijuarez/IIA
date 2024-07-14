from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Ring:
    weight: int

    def __eq__(self, other):
        if other.__class__ is self.__class__:
            return self.weight == other.weight
        return NotImplemented

    def __str__(self):
        return f"{self.weight}"


@dataclass
class Tower:
    rings: List[Ring]

    @classmethod
    def empty(cls) -> "Tower":
        return Tower([])

    def __eq__(self, other):
        if other.__class__ is self.__class__:
            return len(self.rings) == len(other.rings) and all(r1 == r2 for r1, r2 in zip(self.rings, other.rings))
        return NotImplemented

    def __str__(self):
        return "{" + ",".join(str(ring) for ring in self.rings) + "}"


@dataclass(order=True)
class State:
    priority: float
    accumulated_cost: float = field(compare=False)
    towers: List[Tower] = field(compare=False)
    parent: Optional["State"] = field(compare=False)

    @classmethod
    def with_towers(cls, towers: List[Tower]) -> "State":
        return State(priority=0, accumulated_cost=0, towers=towers, parent=None)

    def expand(self) -> List["State"]:
        """
        Genera todas las posibles combinaciones de estados válidos a partir del actual, teniendo en cuenta
        que cada disco sólo puede moverse por encima de otro de mayor peso.
        """
        new_states = []
        for current_tower_index, current_tower in enumerate(self.towers):
            if len(current_tower.rings) == 0:
                continue

            movable_ring = current_tower.rings[0]
            for destination_tower_index, destination_tower in enumerate(self.towers):
                if destination_tower_index == current_tower_index:
                    continue

                if len(destination_tower.rings) == 0 or movable_ring.weight < destination_tower.rings[0].weight:
                    new_towers = [Tower(tower.rings.copy()) for tower in self.towers]
                    new_towers[current_tower_index].rings.pop(0)
                    new_towers[destination_tower_index].rings.insert(0, movable_ring)
                    new_states.append(
                        State(
                            priority=0,
                            accumulated_cost=self.accumulated_cost + 1,
                            towers=new_towers,
                            parent=self))
        return new_states

    def __eq__(self, other):
        if other.__class__ is self.__class__:
            return self.towers == other.towers
        return NotImplemented

    def __str__(self):
        return " + ".join(str(tower) for tower in self.towers)