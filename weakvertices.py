def solve():
    TC = []
    while True:
        n = int(input())
        if n == -1:
            break
        A = []
        for i in range(n):
            A.append([ int(j) for j in input().split(' ')])
        V = [ False for i in range(n) ]
        N = { i : [] for i in range(n) }
        for i in range(n): #Translate adjacency matrix to a dictionary of nodes
            for j in range(n):
                if i != j and A[i][j] == 1:
                    N[i].append(j)
        #print(N)
        for i in range(n):
            if V[i] == False:
                for j in N[i]:
                    for z in N[j]:
                        if z != i and z in N[i]:
                            V[i] = True
                            V[j] = True 
                            V[z] = True     
        WV = []
        for i in range(n):
            if V[i] == False:
                WV.append(i)
        WV.sort()
        TC.append(WV)
    for i in TC:
        for j in i:
            print(j, end=" ")
        print("")
solve()