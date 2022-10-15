def compute(nums, n, m):
    return [x **n % m for x in nums]


if __name__ == "__main__":
    result = compute(nums=[1, 2, 3], n=10, m=7)
    print(result)