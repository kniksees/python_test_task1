import sys

def ans(nums):
    count = sum(nums)
    avg = round(count / len(nums))
    res = sum(abs(i - avg) for i in nums)
    return res


if __name__ == "__main__":
    nums_file = open(sys.argv[1])
    nums_param = []
    for line in nums_file:
        nums_param.append([int(x) for x in line.split()][0])
    print(ans(nums_param))

