# 1. https://www.codewars.com/kata/56a1c074f87bc2201200002e/train/python

def smaller(nums):
    sorted_nums = sorted(set(nums))
    indices = {num: i + 1 for i, num in enumerate(sorted_nums)}

    tree = [0] * (len(indices) + 2)

    def update(i):
        while i < len(tree):
            tree[i] += 1
            i += i & -i

    def query(i):
        res = 0
        while i > 0:
            res += tree[i]
            i -= i & -i
        return res

    result = []
    for num in reversed(nums):
        idx = indices[num]
        result.append(query(idx - 1))
        update(idx)

    return result[::-1]

#2. https://www.codewars.com/kata/62275b5bf6c169002379fa65/train/python

def divide_and_multiply(ns):
    MOD = 10**9 + 7

    total_twos = 0
    rest_nums = []

    for num in ns:
        count = 0
        while num % 2 == 0:
            num //= 2
            count += 1
        total_twos += count
        rest_nums.append(num)

    max_val = max(rest_nums)
    rest_nums.remove(max_val)

    max_val *= pow(2, total_twos, MOD)
    max_val %= MOD

    total = (max_val + sum(rest_nums)) % MOD
    return total
