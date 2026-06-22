vertices = ['A', 'B', 'C', 'D']

edges = [
    ('A', 'B', 1),
    ('B', 'C', 4),
    ('C', 'D', 2),
    ('D', 'A', 3),
    ('B', 'D', 5)
]

mst = [
    ('A', 'B', 1),
    ('C', 'D', 2),
    ('D', 'A', 3)
]

print("Edges in MST:")
total = 0

for u, v, w in mst:
    print(u, "-", v, "=", w)
    total += w

print("Total Weight =", total)
