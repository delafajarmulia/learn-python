def minimal(a, b):
    if a < b :
        return a
    elif b < a :
        return b
    else:
        return a
    
print(minimal(12, 15))