# goal: to respresent where in the world we currwently are
import sys # importing the sys module 

def main():
    coordinates = (42.376, -71.115) # combination of longitude and latitude values
    print(f"Latitude: {coordinates[0]}, Longitude: {coordinates[1]}")

    # tuples cab be unpacked / unpack tuple variables into distinct variables:
    latitude, longitude = coordinates
    print(f"Latitude: {latitude}")
    print(f"Longitude: {longitude}")

    # Why would I use tuples instead of lists?
    # Tuples: 
    """
        - Does not support item assignment
        - Does not support adding values after we've created it (a tuple)

    # Why would we use tuples but not a list?
    --> If we are sure about not going to change or add values, 
        then there is a benefit --> a more efficient way to represent our collection of data
    """

    # How much space do these data structures take up in memory:
    coordinate_tuple = (42.376, -71.115)
    coordinate_list = [42.376, -71.115]

    # .getsizeof() method with sys module reference (imported) tells the size in bytes for any Python object or variable
    print(f"{sys.getsizeof(coordinate_tuple)}") # Answ: 56 (bytes) --> More efficient since less space in memory
    print(f"{sys.getsizeof(coordinate_list)}") # Answ: 72 (bytes)



main()