#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum = 0
    total = len(sys.argv) - 1
    if total == 0:
        print(total)
    elif total != 0:
        for i in range(1, total + 1):
            sum += int(sys.argv[i])
        print("{:d}".format(sum))
