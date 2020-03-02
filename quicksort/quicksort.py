def s(l,st,end):
    print("st,end: ", st, end)
    if len(l) <= 1: return
    idx = random.randint(st,end)
    l[idx],l[st]=l[st],l[idx]
    pivot=l[st]
    small=st
    big = st
    for big in range(st+1,end):
        if l[big] < pivot:
            small+=1
            l[small],l[big]=l[big],l[small]
    l[st],l[small]=l[small],l[st]
    s(l,st,small-1)
    s(l,small+1,big)
    print(l)
