import heapq


def bestFirstSearch(initial_state, goal_state, evaluation_function):
    priority_queue = []
    heapq.heappush(priority_queue, (evaluation_function(initial_state), initial_state))

    while priority_queue:
        current_state = heapq.heappop(priority_queue)[1]

        if current_state == goal_state:
            return current_state

        next_states = generateNextStates(current_state)
        for next_state in next_states:
            priority_value = evaluation_function(next_state)
            heapq.heappush(priority_queue, (priority_value, next_state))

    return "No solution found"

def evaluationFunction(state):
    # Implement your evaluation function here
    # This function assigns a priority value to a state based on a specific heuristic or evaluation criteria
    pass

def generateNextStates(state):
    # Generate all possible next states from the current state
    pass
