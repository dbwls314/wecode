def Even():
    result = []
    for i in range(1, 51):
        if i % 2 == 0:
            result.append(i)
    return result

print(Even())