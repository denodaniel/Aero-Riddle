from itertools import permutations

def calculate_total_time(order, airport_names, flight_times, chosen_company):
    total_time = 0
    for i in range(len(order) - 1):
        from_airport = airport_names[order[i] - 1]
        to_airport = airport_names[order[i + 1] - 1]
        total_time += flight_times[chosen_company][from_airport][to_airport]
    return total_time

def calculate_total_cost(order, airport_names, flight_costs, chosen_company):
    total_cost = 0
    for i in range(len(order) - 1):
        from_airport = airport_names[order[i] - 1]
        to_airport = airport_names[order[i + 1] - 1]
        total_cost += flight_costs[chosen_company][from_airport][to_airport]
    total_cost += flight_costs[chosen_company][airport_names[order[-1] - 1]][airport_names[order[0] - 1]]
    return total_cost

def get_predefined_airports():
    airport_names = ["New Delhi", "Kolkata", "Mumbai", "Chennai", "Bangalore", "Guwahati"]
    return airport_names

def get_user_selection(airport_names):
    print("\nChoose the airports you want to travel to and from:")
    for i, airport in enumerate(airport_names, start=1):
        print(f"{i}. {airport}")

    user_choice = input("Enter the numbers of the airports separated by spaces (or 'exit' to exit): ").lower()
    if user_choice == 'exit':
        return None
    selected_airports_indices = list(map(int, user_choice.split()))

    selected_airport_names = [airport_names[i-1] for i in selected_airports_indices]

    return selected_airport_names
def get_flight_times():
    # For simplicity, let's assume different times for three flight companies
    flight_times = {
        "AirIndia": {
            "New Delhi": {"New Delhi": 0, "Kolkata": 2.5, "Mumbai": 2.5, "Chennai": 2.5, "Bangalore": 3, "Guwahati": 3},
            "Kolkata": {"New Delhi": 2.2, "Kolkata": 0, "Mumbai": 2.5, "Chennai": 2.25, "Bangalore": 2.5, "Guwahati": 1.25},
            "Mumbai": {"New Delhi": 2.25, "Kolkata": 2.5, "Mumbai": 0, "Chennai": 2.5, "Bangalore": 1.5, "Guwahati": 2.75},
            "Chennai": {"New Delhi": 2.5, "Kolkata": 2.25, "Mumbai": 1.9, "Chennai": 0, "Bangalore": 1.05, "Guwahati": 4},
            "Bangalore": {"New Delhi": 2.75, "Kolkata": 2.5, "Mumbai": 1.5, "Chennai": 1, "Bangalore": 0, "Guwahati": 3.5},
            "Guwahati": {"New Delhi": 2.25, "Kolkata": 1.25, "Mumbai": 2.8, "Chennai": 3.9, "Bangalore": 3.7, "Guwahati": 0},
        },
        "SpiceJet": {
            "New Delhi": {"New Delhi": 0, "Kolkata": 2.25, "Mumbai": 2, "Chennai": 2.75, "Bangalore": 2.5, "Guwahati": 2.5},
            "Kolkata": {"New Delhi": 2.25, "Kolkata": 0, "Mumbai": 2.75, "Chennai": 2.5, "Bangalore": 2.5, "Guwahati": 1.25},
            "Mumbai": {"New Delhi": 2, "Kolkata": 2.5, "Mumbai": 0, "Chennai": 2.5, "Bangalore": 1.75, "Guwahati": 3.5},
            "Chennai": {"New Delhi": 2.75, "Kolkata": 2.25, "Mumbai": 1.25, "Chennai": 0, "Bangalore": 2, "Guwahati": 3},
            "Bangalore": {"New Delhi": 2.5, "Kolkata": 2.25, "Mumbai": 1.75, "Chennai": 2.2, "Bangalore": 0, "Guwahati": 2.75},
            "Guwahati": {"New Delhi": 2.5, "Kolkata": 1.25, "Mumbai": 3.5, "Chennai": 3, "Bangalore": 3, "Guwahati": 0},
        },
        "IndiGo": {
            "New Delhi": {"New Delhi": 0, "Kolkata": 2.2, "Mumbai": 2, "Chennai": 2.75, "Bangalore": 2.5, "Guwahati": 2.25},
            "Kolkata": {"New Delhi": 2, "Kolkata": 0, "Mumbai": 2.5, "Chennai": 2.25, "Bangalore": 2.5, "Guwahati": 1},
            "Mumbai": {"New Delhi": 2.25, "Kolkata": 2.25, "Mumbai": 0, "Chennai": 2.25, "Bangalore": 2.5, "Guwahati": 3.25},
            "Chennai": {"New Delhi": 2.5, "Kolkata": 2.5, "Mumbai": 1.9, "Chennai": 0, "Bangalore": 1.05, "Guwahati": 3.5},
            "Bangalore": {"New Delhi": 2.5, "Kolkata": 2.5, "Mumbai": 1.5, "Chennai": 1.05, "Bangalore": 0, "Guwahati": 2.75},
            "Guwahati": {"New Delhi": 2.25, "Kolkata": 1.35, "Mumbai": 3.5, "Chennai": 3.75, "Bangalore": 2.5, "Guwahati": 0},
            }
        }
    return flight_times
def get_flight_costs():
    # For simplicity, let's assume different costs for three flight companies
    flight_costs = {
        "AirIndia": {
            "New Delhi": {"New Delhi": 0, "Kolkata": 6436, "Mumbai": 5394, "Chennai": 6496, "Bangalore": 5892, "Guwahati": 5836},
            "Kolkata": {"New Delhi": 6926, "Kolkata": 0, "Mumbai": 7368, "Chennai": 8103, "Bangalore": 9713, "Guwahati": 2866},
            "Mumbai": {"New Delhi": 6501, "Kolkata": 5422, "Mumbai": 0, "Chennai": 4200, "Bangalore": 5020, "Guwahati": 11634},
            "Chennai": {"New Delhi": 6500, "Kolkata": 6887, "Mumbai": 5515, "Chennai": 0, "Bangalore": 2230, "Guwahati": 12626},
            "Bangalore": {"New Delhi": 6593, "Kolkata": 8673, "Mumbai": 4802, "Chennai": 5417, "Bangalore": 0, "Guwahati": 12656},
            "Guwahati": {"New Delhi": 5897, "Kolkata": 5286, "Mumbai": 12636, "Chennai": 12668, "Bangalore": 13177, "Guwahati": 0},
        },
        "SpiceJet": {
            "New Delhi": {"New Delhi": 0, "Kolkata": 5902, "Mumbai": 6455, "Chennai": 9643, "Bangalore": 7253, "Guwahati": 6436},
            "Kolkata": {"New Delhi": 6314, "Kolkata": 0, "Mumbai": 9199, "Chennai": 13766, "Bangalore": 8623, "Guwahati": 3440},
            "Mumbai": {"New Delhi": 5320, "Kolkata": 6728, "Mumbai": 0, "Chennai": 3499, "Bangalore": 3567, "Guwahati": 6902},
            "Chennai": {"New Delhi": 9156, "Kolkata": 12129, "Mumbai": 4225, "Chennai": 0, "Bangalore": 1571, "Guwahati": 8124},
            "Bangalore": {"New Delhi": 6733, "Kolkata": 6594, "Mumbai": 3289, "Chennai": 1826, "Bangalore": 0, "Guwahati": 8333},
            "Guwahati": {"New Delhi": 6234, "Kolkata": 3219, "Mumbai": 6794, "Chennai": 8998, "Bangalore": 9246, "Guwahati": 0},
        },
        "IndiGo": {
            "New Delhi": {"New Delhi": 0, "Kolkata": 6373, "Mumbai": 4431, "Chennai": 6373, "Bangalore": 6235, "Guwahati": 6437},
            "Kolkata": {"New Delhi": 6944, "Kolkata": 0, "Mumbai": 6876, "Chennai": 7994, "Bangalore": 6524, "Guwahati": 3409},
            "Mumbai": {"New Delhi": 7704, "Kolkata": 8702, "Mumbai": 0, "Chennai": 3500, "Bangalore": 3150, "Guwahati": 8051},
            "Chennai": {"New Delhi": 8407, "Kolkata": 8144, "Mumbai": 3700, "Chennai": 0, "Bangalore": 4298, "Guwahati": 7992},
            "Bangalore": {"New Delhi": 11323, "Kolkata": 7697, "Mumbai": 3834, "Chennai": 5554, "Bangalore": 0, "Guwahati": 8916},
            "Guwahati": {"New Delhi": 6022, "Kolkata": 3689, "Mumbai": 9039, "Chennai": 11088, "Bangalore": 8404, "Guwahati": 0},
        }
    }
    return flight_costs

def find_optimal_flight_route(airport_names, flight_data, user_airport_order, optimization_choice):
    num_airports = len(airport_names)
    airports = list(range(num_airports))

    min_value = float('inf')
    optimal_order = None
    chosen_company = None

    for company, data in flight_data.items():
        if optimization_choice == 'time':
            total_value = calculate_total_time(user_airport_order, airport_names, flight_data, company)
        elif optimization_choice == 'cost':
            total_value = calculate_total_cost(user_airport_order, airport_names, flight_data, company)
        else:
            raise ValueError("Invalid optimization choice. Use 'time' or 'cost'.")

        if total_value < min_value:
            min_value = total_value
            chosen_company = company

    optimal_route = [airport_names[i-1] for i in user_airport_order]

    return optimal_route, min_value, chosen_company

# Main program
while True:
    predefined_airport_names = get_predefined_airports()
    user_airport_names = get_user_selection(predefined_airport_names)

    if user_airport_names is None:
        print("Thankyou for visiting us(>_<).")
        break

    while True:
        optimization_choice = input("Do you want to optimize for 'time' or 'cost' (or 'exit' to change airports)? ").lower()

        if optimization_choice == 'exit':
            break
        elif optimization_choice not in ['time', 'cost']:
            print("Invalid choice. Please enter 'time', 'cost', or 'exit'.")
        else:
            flight_data = get_flight_times() if optimization_choice == 'time' else get_flight_costs()

            user_airport_order = list(range(1, len(user_airport_names) + 1))
            optimal_route, min_value, chosen_company = find_optimal_flight_route(user_airport_names, flight_data, user_airport_order, optimization_choice)

            print("Flight Route:", optimal_route)
            
            if optimization_choice == 'time':
                print(f"Total Flight Time: {min_value} hours")
                print("Chosen Company:", chosen_company)
            elif optimization_choice == 'cost':
                #print(f"Total Flight Cost: {min_value} rupees")
                print("Chosen Company:", chosen_company)
                costval=min_value
                adult=int(input("How many adult passengers?: "))
                child=int(input("How many child passengers?: "))
                currval=(adult*costval)+(child*costval*0.75)
                print("Total cost= ",currval,"rupees for Economy")
                bc=input("Do u wish to know about the business class?")
                if bc=="yes":
                    if chosen_company=="AirIndia":
                        print("Total cost= ",currval*5,"rupees for Business Class")
                    elif chosen_company=="SpiceJet":
                        print("Total cost= ",currval*2,"rupees for Business Class")
                    elif chosen_company=="IndiGo":
                        print("Total cost= ",currval*3.5,"rupees for Business Class")   
                    else:
                        continue
                    
                print("""
CONGRATULATIONS! WE HAVE FOUND YOU THE BEST FLIGHT OFFERS!!!
Choose suitable criteria:
a) Student (single ticket)
b) Doctor (single ticket)
c) Senior Citizen (single ticket)
d) Indian military personnel (single ticket)
e) none of the above(single ticket)
f) none of the above(multiple ticket)
g) Business Class""")
                opt=input("Enter option: ")
                if opt=='a':
                    print("10% OFF!!!")
                    print(costval-(0.1*costval)," rupees ")
                elif opt=='b':
                    print("5% OFF!!!")
                    print(costval-(0.05*costval)," rupees")
                elif opt=='c':
                    print("10% OFF!!!")
                    print(costval-(0.1*costval)," rupees")
                elif opt=='d':
                    print("12% OFF!!!")
                    print(costval-(0.12*costval),"rupees")
                elif opt=='e':
                    if costval<=15000:
                        print("2.5% DISCOUNT!!")
                        print(costval-(0.025*costval)," rupees")
                    elif 15000<costval<=25000:
                        print("7.5% DISCOUNT!!")
                        print(costval-(0.075*costval)," rupees")
                    elif 25001<costval:
                        print("10% DISCOUNT!!")
                        print(costval-(0.1*costval)," rupees")
                    else:
                        print("Sorry no offers currently available")
                elif opt=='f':
                    if currval<=25000:
                        print("4% DISCOUNT!!")
                        print(currval-(0.04*currval)," rupees")
                    elif 25000<currval<=40000:
                        print("7.5% DISCOUNT!!")
                        print(currval-(0.075*currval)," rupees")
                    elif 40001<currval<=60000:
                        print("10% DISCOUNT!!")
                        print(currval-(0.1*currval)," rupees")
                    elif 60001<currval<=90000:
                        print("13% DISCOUNT!!")
                        print(currval-(0.13*currval)," rupees")
                    elif currval>90000:
                        print("15% DISCOUNT!!")
                        print(currval-(0.15*currval)," rupees")
                elif opt=="g":
                    continue
                else:
                    print("Enter valid option")
                
            break
