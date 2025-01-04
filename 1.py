def store():
    cal = [6, 0, 2, 0, 3]
    return cal

def calculate(cal, x):
    result = 0
    for i, j in enumerate(cal):
        result += j * (x ** (len(cal) - i - 1))
    return result

polynomial = store()
x = 91
result = calculate(polynomial, x)
print(f"當 x = {x} 時，f(x) 的值為: {result}")