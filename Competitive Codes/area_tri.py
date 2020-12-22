def areaoftri(base, height):
    """Gives area of a triangle"""
    return str(0.5 * (base * height)) + " sq meter"


while True:
    try:
        inp1 = int(input())
        inp2 = int(input())
        break
    except ValueError:
        print("Invalid lenght")
        continue
print(areaoftri(inp1, inp2))
print(areaoftri(inp1, inp2))
