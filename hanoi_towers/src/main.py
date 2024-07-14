from astar import AStar, State
from hanoi_adt import Ring, Tower
from heuristics import tower_coincidence, rings_to_be_moved, manhattan_distance, combined


def run_algorithm(heuristic):
    initial_state_towers = [Tower([Ring(weight=w) for w in range(8)]), Tower([]), Tower([])]
    initial_state = State.with_towers(initial_state_towers)

    goal_state_towers = [Tower([]), Tower([]), Tower([Ring(weight=w) for w in range(8)])]
    goal = State.with_towers(goal_state_towers)

    search_algorithm = AStar(heuristic)
    result = search_algorithm.execute(initial_state, goal)
    print(f"Resultado: {result}")


def main():
    run_algorithm(tower_coincidence)
    run_algorithm(rings_to_be_moved)
    run_algorithm(manhattan_distance)
    run_algorithm(combined)


if __name__ == "__main__":
    main()
