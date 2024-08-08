import sys

def ans(n: int, m: int) -> str:
    res = ["1"]
    i = 0
    while True:
        i += m - 1
        i %= n
        j = (i + m - 1) % n
        res.append(str(i + 1))
        if j == 0:
            break

    return ''.join(res)


if __name__ == "__main__":
    print(ans(int(sys.argv[1]), int(sys.argv[2])))
