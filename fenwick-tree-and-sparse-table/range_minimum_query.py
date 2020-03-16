import math
def build_table(data):
    n = len(data)
    sparse_table = [[float("inf") for j in range(math.floor(math.log2(n) + 1))] for i in range(n)]
    for i in range(n):
        sparse_table[i][0] = i

    j = 1
    while 1 << j <= n:
        i = 0
        while i + (1 << j) - 1 < n:
            if data[sparse_table[i][j - 1]] < data[sparse_table[i + (1 << (j - 1))][j - 1]]:
                sparse_table[i][j] = sparse_table[i][j - 1]

            else:
                sparse_table[i][j] = sparse_table[i + (1 << (j - 1))][j - 1]
            i += 1

        j += 1

    return sparse_table

def query(data, table, left, right):
    number_of_elements = right - left + 1
    end_query = math.floor(math.log2(number_of_elements))
    return min(data[table[left][end_query]],
                data[table[left + number_of_elements - (1 << end_query)][end_query]])

n = int(input())
data = list(map(int, input().split()))
sparse_table = build_table(data)
q = int(input())
for i in range(q):
    left, right = list(map(int, input().split()))
    print(query(data, sparse_table, left, right))
