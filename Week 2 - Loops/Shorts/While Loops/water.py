# Soil is considered dry when it reaches a moisture level of 20% or less
# write a program to check what the moisutre content of this plant's soil is, alerting me if it is 20% or less
from soil import sample # this program uses a function called 'sample' from another program called 'soil'
# 'sample' purpose: sample our soil and return to us the percent moisture it has sampled from the soil on a particular day
def main():
    moisture = sample()
    days = 0 # the day we start watering is days = to 0
    print(f"Day: {days}: Moisture is {moisture}%")

    # While loop great when we are not sure how many times we want to loop but
    # rather applying a loop while some condition is True/False.
    while(moisture > 20): # While Loop --> good for things like randomness
        moisture = sample() # sample again 
        days += 1 # every time we iterate, it'll add 1 to days
        print(f"Day {days}: Moisture is {moisture}%") # report moisture content again

    print("Time to water!")


main()