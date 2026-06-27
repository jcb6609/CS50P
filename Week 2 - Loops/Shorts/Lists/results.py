results = ["Mario", "Luigi"]

# use the .append() method to add on some element at the end of a referenced list:
results.append("Princess")
results.append("Yoshi")
results.append("Koopa Troopa")
results.append("Toad")

# pass a list to the referenced list (list containing another list obj)
results.append(["Bowser", "Donkey Kong Jr."])

# .remove() method to remove items of the referenced list
results.remove(["Bowser", "Donkey Kong Jr."])

# Add two objects to the list --> use the .extend() method:
results.extend(["Bowser", "Donkey Kong Jr."])

print(results)