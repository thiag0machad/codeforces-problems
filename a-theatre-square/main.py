inputs = input().strip().split()

n = int(inputs[0])
m = int(inputs[1])
a = int(inputs[2])

print(((n + a - 1) // a) * ((m + a - 1) // a))