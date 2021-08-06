# Task3

def square(sq):
    for i in range(sq):
        res = []
        res.append(4 * sq)
        res.append(sq * sq)
        res.append(1.41 * sq)
        return tuple(res)


print(square(4))
