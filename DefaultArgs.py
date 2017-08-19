# Trying default args


def list_arg(a, L=[]):
    L.append(a)
    return L


def list_arg_clear(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L


print(list_arg(1))
print(list_arg(2))

print(list_arg_clear(1))
print(list_arg_clear(2))
