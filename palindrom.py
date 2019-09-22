def pal(n):
    n2=str(n)
    if n>=10000 or n<=0:
        return 'error'
    if n<1000:
        if n<10:
            n2='000'+str(n)
        elif n<100:
            n2='00'+str(n)
        else:
            n2='0'+str(n)
    revers=str(n2)[::-1]
    if n2==revers:
        return 'palindrom'
    else:
        return 'not palindrom'

print(pal(550))