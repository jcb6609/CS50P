distances = {
    "Voyager 1": 163,
    "Voyager 2": 136,
    "Pioneer 10": 80,
    "New Horizons": 58,
    "Pioneer 11": 44
}

def main():
    for i in distances:
        m = convert(distances[i]) # this line of code can be printed directly, no need to create/assignate a variable mandatorily
        print(f"{distances[i]} AU correspond to {m:,} m ") # a variable using 'var:,' automatically displays commas (thousands separators) to its assignated number value

def convert(au):
    return au * 149597870700

main() 