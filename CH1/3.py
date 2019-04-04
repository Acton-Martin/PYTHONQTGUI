def integer(number):
    try:
        x = int(round(float(number)))
    except ValueError:
        x = 0
    return x