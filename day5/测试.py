def is_even(n):
    return n%2 == 0

def sum_to(n):
    total = 0
    for i in range(1,n+1):
        total += i
        return total

def print_table(n):
    for i in range(1,10):
        print(f"{n}×{i}={n*i}")

print(is_even(4))
print(sum_to(100))
print_table(3)