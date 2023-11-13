def solve():
    T = int(input()) #number of test cases
    TC = [] #holds our results to be printed later
    for _ in range(T): #an _ is used because we don't care about initializing a variable
        input() #for this problem, test cases were preceded by a blank line for some reason
        N = int(input())
        s = 0 #sum of candies (elements)
        for _ in range(N):
            c = int(input())
            s += c
        if s%N != 0: #modulo operation used to test for remainders
            TC.append("NO")
        else:
            TC.append("YES")
    for i in TC:
        print(i)
solve()