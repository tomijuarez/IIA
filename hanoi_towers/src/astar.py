from typing import Dict, Optional
from queue import PriorityQueue
from hanoi_adt import State


class AStar:

    def __init__(self, heuristic):
        self.heuristic = heuristic

    def execute(self, initial_state: State, goal: State) -> Optional[State]:
        counter = 0
        frontier: PriorityQueue[State] = PriorityQueue()
        visited_states: Dict[str, State] = {}

        frontier.put(initial_state)

        visited_states[str(initial_state)] = initial_state

        while not frontier.empty():
            current_state = frontier.get()

            counter += 1

            if current_state == goal:
                print(f'Cantidad de pasos dados: {counter}')
                return current_state

            for next_state in current_state.expand():

                new_cost = current_state.accumulated_cost + 1

                visited_next_state = visited_states.get(str(next_state))

                if visited_next_state is None or visited_next_state.accumulated_cost > new_cost:
                    estimated_left_cost = self.heuristic(next_state, goal)

                    next_state.accumulated_cost = new_cost
                    next_state.priority = new_cost + estimated_left_cost

                    visited_states[str(next_state)] = next_state
                    frontier.put(next_state)

        return None