from itertools import permutations

def solve_cryptarithmetic():
    for perm in permutations(range(10), 8):
        S, E, N, D, M, O, R, Y = perm
        if S != 0 and M != 0:
            send = S * 1000 + E * 100 + N * 10 + D
            more = M * 1000 + O * 100 + R * 10 + E
            money = M * 10000 + O * 1000 + N * 100 + E * 10 + Y

            if send + more == money:
                return (send, more, money)
    return None

result = solve_cryptarithmetic()
if result:
    send, more, money = result
    print(f'SEND: {send}')
    print(f'MORE: {more}')
    print(f'MONEY: {money}')
else:
    print("No solution found.")

