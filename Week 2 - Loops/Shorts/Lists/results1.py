results = ["Mario", "Luigi", "Princess", "Yoshi", "Koopa Troopa", "Toad", "Bowser", "Donkey Kong Jr."]

results.remove("Bowser") # .remove() method removes the desired argument of our referenced list 
# results.append("Bowser") # .append() mehtod add the desired argument into the referenced list for the last position
results.insert(0, "Bowser") # .insert() method takes as a first argument the index at which I want to insert some given element, which would be the second argument

print(results)

results.reverse() # .reverse() method reverses the referenced list

print(results)