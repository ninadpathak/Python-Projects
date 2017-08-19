# These arguments are used for passing multiple different parameters.
# *a is a tuple while **b is a dictionary argument


def arguments(*a, **b):
    for i in a:
        print(i)
    for j in b:
        print(j, " - ", b[j])


arguments("Hello", "My name is ninad", name="Ninad", time="12:30")
