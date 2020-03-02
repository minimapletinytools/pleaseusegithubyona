def s(l,st,end):
  if len(l) <= 1: return
  m=len(l)//2
  ll=l[:m]
  rr=l[m:]
  s(ll,st,m)
  s(rr,m+1,end)
  i=0
  j=0
  k=0
  while i < len(ll) and j< len(rr):
    print('i', i)
    print('j', j)
    print('len(ll)', len(ll))
    print('len(rr)', len(rr))
    print('ll[i]', ll[i])
    print ('rr[j]', rr[j])

    if ll[i]>rr[j]:
      l[k] = rr[j]
      j+=1
    if ll[i]<=rr[j]:
      l[k]=ll[i]
      i+=1
    k+=1
  print('i:',i)
  print('k:',k)
  print('j:',j)
  print('ll:',ll)
  print('rr:',rr)
  while i < len(ll):
    l[k]=ll[i]
    i+=1
    k+=1
  print('k -1:',k)
  while j < len(rr):
    l[k] = rr[j]
    j+=1
    k+=1
  print('k -2:',k)
  print(l)
  
