def waterJugSteps(jug1_capacity, jug2_capacity, target_amount):
    steps = []  # List to store the steps
    jug1 = 0  # Initialize the first jug to be empty
    jug2 = 0  # Initialize the second jug to be empty

    while jug1 != target_amount and jug2 != target_amount:
        # Fill jug1 to its capacity
        jug1 = jug1_capacity
        steps.append((jug1, jug2))

        # Pour water from jug1 to jug2 until jug2 is full or jug1 is empty
        while jug2 < jug2_capacity and jug1 > 0:
            pour_amount = min(jug1, jug2_capacity - jug2)
            jug1 -= pour_amount
            jug2 += pour_amount
            steps.append((jug1, jug2))

        if jug2 == target_amount:
            break  # Target amount achieved, no need to empty jug2

        # Empty jug2 as much as possible while keeping the desired amount in jug1
        jug2 = 0
        steps.append((jug1, jug2))

        # Pour water from jug1 to jug2 until jug2 is full or jug1 is empty
        while jug2 < jug2_capacity and jug1 > 0:
            pour_amount = min(jug1, jug2_capacity - jug2)
            jug1 -= pour_amount
            jug2 += pour_amount
            steps.append((jug1, jug2))
        return steps

jug1_capacity, jug2_capacity, target_amount = 4, 3, 2
steps = waterJugSteps(jug1_capacity, jug2_capacity, target_amount)

if steps:
    print("Steps to achieve {} units of water with minimum waste:".format(target_amount))
    for step in steps:
        print(step)
else:
    print("It is not possible to achieve {} units of water.".format(target_amount))