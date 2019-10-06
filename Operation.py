a =list(input('Введите первое число: '))
b =list(input('Введите второе число: '))

if a > b:
    n1 = a
    n2 = b
    itog = ['+']
else:
    n1 = b
    n2 = a
    itog = ['-']

if len(n1) > len(n2):
    n2 = ['0'] * (len(n1) - len(n2)) + n2
elif len(n1) < len(n2):
    n1 = ['0'] * (len(n2) - len(n1)) + n1

def plus(n1, n2):
    sum =0
    final_sp = []
    des = 0
    k = 0
    ed = int(list(str(int(n1[-1]) + int(n2[-1])))[-1])
    for i in reversed( (range(len(n1))) ):
        final_sp.append( int(list(str(ed + int(des)))[-1]) )
        if ed + int(des) < 0 or ed + int(des) > 9:
            k = int(list(str(ed + int(des)))[0])
        sum = int(n1[i]) + int(n2[i])+ int(k)
        if i==0:
            break
        if sum >=0 and sum < 10:
            ed = 0
        else:
            ed = int(list(str((sum)))[0])
        des = int(str(int(n1[i-1]) + int(n2[i-1]))[-1])
        k=0
    return list(reversed(final_sp))
print(plus(n1,n2))

def minus(n1, n2):
    k = [0]
    for i in reversed( (range(len(n1))) ):
        if i == 0:
            break
        else:
            if n1[i] >= n2[i]:
                k.append(0)
            else:
                k.append(1)
    k = list(reversed(k))

    final_sp = []
    for i in reversed( (range(len(n1))) ):
        if int(n1[i]) == 0:
            final_sp.append( 10 - k[i] - int(n2[i]) )
        else:
            final_sp.append( int(n1[i]) - k[i] - int(n2[i]) )
    itog.append( list(reversed(final_sp)) )
    return itog

print(minus(n1, n2))