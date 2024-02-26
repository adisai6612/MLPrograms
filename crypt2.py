from itertools import permutations

def solve_cryptarithmetic():
    # Define the letters and their possible digit assignments
    letters = "SENDMORY"
    digits = list(range(10))
    
    # Generate all possible permutations of digit assignments for the letters
    digit_permutations = permutations(digits, len(letters))
    
    # Iterate through each permutation and check if it satisfies the equation
    for perm in digit_permutations:
        digit_mapping = dict(zip(letters, perm))
        
        # Check if any of the numbers start with 0
        if digit_mapping['S'] == 0 or digit_mapping['M'] == 0:
            continue
        
        send = digit_mapping['S'] * 1000 + digit_mapping['E'] * 100 + digit_mapping['N'] * 10 + digit_mapping['D']
        more = digit_mapping['M'] * 1000 + digit_mapping['O'] * 100 + digit_mapping['R'] * 10 + digit_mapping['E']
        money = digit_mapping['M'] * 10000 + digit_mapping['O'] * 1000 + digit_mapping['N'] * 100 + digit_mapping['E'] * 10 + digit_mapping['Y']
        
        if send + more == money:
            print("Solution found:")
            print(f"SEND = {send}")
            print(f"MORE = {more}")
            print(f"MONEY = {money}")
            return
    
    print("No solution found")

if __name__ == "__main__":
    solve_cryptarithmetic()
