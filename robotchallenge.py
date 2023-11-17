def solve():
    T = []
    while True:
        w,l = map(int,input().split(' '))
        if w==l==0:
            break
        r = []
        for i in range(l):
            for j in range(w):
                r.append([j,i])
        #print(r)
        #Horizontal boundary is 0 to w-1
        #Vertical boundary is 0 to l-1
        p = [0,0]
        pa = [0,0]
        n = int(input())
        for i in range(n):
            line = input().split(' ')
            x = line[0]
            y = int(line[1])
            if x=="u":
                p[1] += y
                for j in range(pa[1],pa[1]+y):
                    if j<l-1:
                        pa[1]+=1
            elif x=="d":
                p[1] -= y
                for j in range(pa[1]-y,pa[1]):
                    if pa[1]>0:
                        pa[1]-=1
            elif x=="r":
                p[0] += y
                for j in range(pa[0],pa[0]+y):
                    if j<w-1:
                        pa[0]+=1
            elif x=="l":
                p[0] -= y
                for j in range(pa[0]-y,pa[0]):
                    if pa[0]>0:
                        pa[0]-=1
        T.append(["Robot thinks " + str(p[0])+" "+str(p[1]),"Actually at " + str(pa[0])+" "+str(pa[1])])
    for i in T:
        for j in i:
            print(j)
        print("")
solve()