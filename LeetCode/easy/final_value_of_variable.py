def variableF(operations):
    X = 0
    for i in operations:
        if "+" in i:
            X += 1
        elif "-" in i:
            X -= 1 
    return X
operations = ["++X","++X","X++"]
result = variableF(operations)
print(result)



