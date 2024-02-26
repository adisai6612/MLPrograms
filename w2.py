from collections import deque

def water_jug_bfs(jug1_capacity, jug2_capacity, target_liters):
    # Initialize the queue for BFS
    queue = deque()
    # Create a set to keep track of visited states
    visited = set()

    # Initialize the initial state with both jugs empty
    initial_state = (0, 0)
    queue.append(initial_state)
    visited.add(initial_state)

    while queue:
        current_state = queue.popleft()
        jug1, jug2 = current_state

        # Check if the target_liters is reached
        if jug1 == target_liters or jug2 == target_liters:
            return current_state

        # Perform all possible operations: fill jug1, fill jug2, empty jug1, empty jug2, pour from jug1 to jug2, pour from jug2 to jug1
        operations = [
            (jug1_capacity, jug2),
            (jug1, jug2_capacity),
            (0, jug2),
            (jug1, 0),
            (min(jug1 + jug2, jug1_capacity), max(jug1 + jug2 - jug1_capacity, 0)),
            (max(jug1 + jug2 - jug2_capacity, 0), min(jug1 + jug2, jug2_capacity))
        ]

        for operation in operations:
            new_state = operation
            if new_state not in visited:
                queue.append(new_state)
                visited.add(new_state)

    # If the target_liters cannot be reached, return None
    return None

# Example usage:
jug1_capacity = 4
jug2_capacity = 3
target_liters = 2

result = water_jug_bfs(jug1_capacity, jug2_capacity, target_liters)
if result:
    print(f"Solution found: ({result[0]}, {result[1]})")
else:
    print("No solution found.")
