def tower(n, t1, t2, t3, i=1):
    if n == 0:
        return i
    i = tower(n-1, t1, t3, t2, i)
    print(f'Step {i}: Move Disk no. {n} from {t1} to {t3}')
    i += 1
    i = tower(n-1, t2, t1, t3, i)
    return i
tower(5, 'A', 'C', 'B')