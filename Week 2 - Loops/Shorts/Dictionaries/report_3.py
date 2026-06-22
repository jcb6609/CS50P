def main():
    spacecraft = {
        "name": "James Webb Space Telescope"
    }
    # If we wanted to add not just one key at a time, but maybe multiple at once, then we could use a method called .update()    spacecraft["distance"] = 0.01
    spacecraft.update({"distance": 0.01, "orbit": "Sun"}) # update takes as an argument (input) another dictionary, but it will really take that dict's argument keys and values and then just add them to the dict I started with (the referenced dict)
    print(create_report(spacecraft))

def create_report(spacecraft):
    return f""" 
    ========= REPORT =========

    Name: {spacecraft["name"]} 
    Distance: {spacecraft.get("distance", "Unknown")} AU (Astronomic Units)
    Orbit: {spacecraft["orbit"]}
    
    ==========================
    """

main()