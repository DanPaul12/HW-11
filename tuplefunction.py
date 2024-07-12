flight_list = []

def tuple_function(passenger, origin, destination):
    my_tuple = (passenger, origin, destination)
    flight_list.append(my_tuple)
    for flight in flight_list:
        flight_num = flight_list.index(flight) + 1
        print(f"Itinerary {flight_num}: {passenger} from {origin} to {destination}")
            



tuple_function("Alice", "New York", "London")
tuple_function("Bob", "Tokyo", "San Francisco")