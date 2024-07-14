from typing import List
from hanoi_adt import State, Tower


def tower_coincidence(next_state: State, goal_state: State) -> int:
    def most_populated_tower(towers: List[Tower]) -> int:
        indexed_rings_number = [len(tower.rings) for tower in towers]
        most_populated = max(indexed_rings_number)
        return indexed_rings_number.index(most_populated)

    if most_populated_tower(next_state.towers) == most_populated_tower(goal_state.towers):
        return -1
    return 1


def rings_to_be_moved(next_state: State, goal_state: State) -> int:
    goal_tower = next(tower for tower in goal_state.towers if tower.rings)
    to_be_moved = 0

    for next_tower in next_state.towers:
        for ring in next_tower.rings:
            if ring not in goal_tower.rings:
                to_be_moved += 1

    return to_be_moved


def manhattan_distance(next_state: State, goal_state: State) -> int:
    goal_tower_index = next(i for i, tower in enumerate(goal_state.towers) if tower.rings)
    goal_tower_rings = goal_state.towers[goal_tower_index].rings
    total_distance = 0

    for next_tower_index, next_tower in enumerate(next_state.towers):
        for next_ring_index, next_ring in enumerate(next_tower.rings):
            goal_ring_index = goal_tower_rings.index(next_ring)
            total_distance += abs(goal_tower_index - next_tower_index) + abs(goal_ring_index - next_tower_index)

    return total_distance


def combined(next_state: State, goal_state: State) -> int:
    return tower_coincidence(next_state, goal_state) + manhattan_distance(next_state, goal_state)
