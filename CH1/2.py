def charcount(text):
    stats = {} # Same as: stats = dict()
    for char in "abcdefghijklmnopqrstuvwxyz":
        stats[char] = 0
    stats["whitespace"] = 0
    stats["others"] = 0
    for char in text.lower():
        if char in stats:
            stats[char] += 1
        elif char.isspace():
            stats["whitespace"] += 1
        else:
            stats["others"] += 1
    return stats
print(charcount("Exceedingly Edible"))