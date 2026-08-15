def main():
    name = get_name() # getter function get_name() assigned to var 'name'
    house = get_house() # getter function get_house() assigned to var 'house' 

    print(f"{name} from {house}")


def get_name():
    return input("Nmae: ")


def get_house():
    return input("House: ")


if __name__ == "__main__":
    main()