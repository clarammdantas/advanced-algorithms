t = int(input())
input()
for i in range(t):
    n = int(input())
    data = [0 for j in range(n)]
    for j in range(n):
        data[j] = int(input())
    input()

    greatest = max(data)
    tree = [0 for j in range(greatest + 2)]
    def update_tree(index):
        while index < len(tree):
            tree[index] += 1
            index += index & (-index)

    def query(index):
        inv_sum = 0
        while index > 0:
            inv_sum += tree[index]
            index -= index & (-index)

        return inv_sum

    total_inv = 0
    for j in range(n - 1, -1, -1):
        total_inv += query(data[j] - 1)
        update_tree(data[j])

    print(total_inv)
