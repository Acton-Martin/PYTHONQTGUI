def incrementString(text="AAAA"):
    OrdA = ord("A")
    OrdZ = ord("Z")
    changed = False
    values = [ord(c) for c in reversed(text.upper())]
    for i in range(len(values)):
        if values[i] < OrdZ:
            values[i] += 1
            changed = True
            break
        elif values[i] == OrdZ:
            values[i] = OrdA
    if not changed:
        values = [OrdA] + values
    return "".join([chr(v) for v in reversed(values)])
