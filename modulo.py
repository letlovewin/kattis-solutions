def solve():
    k = set()
    for i in range(10):
        k.add(int(input())%42)
    print(len(k))
    
solve()