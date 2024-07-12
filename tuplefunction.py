flight_list = []

def tuple_function(passenger, origin, destination):
    my_tuple = (passenger, origin, destination)
    flight_list.append(my_tuple)
    print(f"Itinerary: {passenger} from {origin} to {destination}")
            



tuple_function("Alice", "New York", "London")
tuple_function("Bob", "Tokyo", "San Francisco")