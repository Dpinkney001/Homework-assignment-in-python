def bar(n):
    if n >= 32:
        return 2
    else:
        return 1
def foo(l):
    n = bar(l[2])
    return l[n]
