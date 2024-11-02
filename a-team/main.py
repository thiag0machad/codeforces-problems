n = int(input())

implemented_problems = 0

for _ in range(n):
    problem_conditions = input().strip().split()
    true_conditions = 0

    if problem_conditions[0] == '1':
        true_conditions += 1

    if problem_conditions[1] == '1':
        true_conditions += 1

    if problem_conditions[2] == '1':
        true_conditions += 1

    if true_conditions >= 2:
        implemented_problems += 1

print(implemented_problems)