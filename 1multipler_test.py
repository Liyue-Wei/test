def find_min_ones(n):
    num = 1
    count = 1

    while num % n != 0:
        num = (num * 10 + 1) % n
        count += 1

    return count

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    k = int(data[0])
    results = []

    for i in range(1, k + 1):
        n = int(data[i])
        results.append(find_min_ones(n))

    for result in results:
        print(result)

if __name__ == "__main__":
    main()
