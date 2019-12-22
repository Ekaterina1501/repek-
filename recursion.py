def task1(n):
    sp = sum(map(int, list(str(n))))
    if len(list(str(sp))) == 1:
        return sp
    else:
        return task1(sp)

def task2(m, n):
    if m == 0:
        return n+1
    elif n == 0:
        return task2(m-1, 1)
    else:
        return task2(m-1, task2(m, n-1))

def task3(n, s=[]):
    if n>=0 and n<10:
        s.append(n)
        return s
    else:
        s.append(n % 10)
        return (task3(n//10, s))

def task4(n, s=[]):
    if n == 0:
        s.reverse()
        return int(''.join(str(i) for i in s))
    else:
        s.append(n%2)
        return task4(n//2)

def task5(n, k=2):
    if k > n/2:
        print(int(n))
        return None
    elif n % k == 0:
        print(int(k))
        task5(n/k, k)
    else:
        task5(n,k+1)