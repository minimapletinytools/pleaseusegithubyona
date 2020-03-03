def s(l):
    #size
    n = len(l)
    print("n:",n)
    print("range:", range(n,-1,-1))
    #build heap
    for i in range(n,-1,-1):
        max = i
        l_idx = 2*i+1
        r_idx = 2*i+2
        print("max:",max)
        print("l_idx:",l_idx)
        print("r_idx:",r_idx)
        if l_idx < n and l[i] < l[l_idx]:
            max=l_idx
        print("max -1:",max)
        if r_idx < n and l[max] < l[r_idx]:
            max=r_idx
        print("max -2:",max)
        if max!=i:
            l[i],l[max] = l[max],l[i]
        print("l:",l)
    for i in range(n-1, 0, -1):
           l[i], l[0] = l[0], l[i]
    print(l)
