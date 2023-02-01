print("Fish Pond Model")
print("===============")


width = float(input("Enter pond width: (meters)"))
length = float(input("Enter pond length: (meters)"))
depth = float(input("Enter pond depth: (meters)"))
print("\n")
print("Results")
print("-------")
area = width * length
print("Surface area of the pond:" , area , "square meters")

volume = area * depth
print("Pond contains:" , volume , "cubic meters of water")
    
fish = int(volume * 2)
print("Number of fish" , fish , "fish")

print("\n")
print("Filling the pond")
print("----------------")
second = float(input("Enter liters per second: "))
hour = 3600 * second
print(hour , "liters per hour")
day = hour*24
#convert liters/day to cubic meters/day (m^3 = 1000L)
day = day/1000
print(day, "cubic meters/day")
'''
The number of days to fill the pond is the volume the pond divided by the water flow in one day
'''
days = volume/day
#round the number to two decimal places
days = round(days,2)

#convert the numbers of days to full days plus extra hours
full_days = int(days)
part_day = days - full_days
hours = part_day * 24


#round the hours to two decimal places
hours = round(hours,2)
full_h = int(hours)
part_h = hours - full_h
min = part_h * 60
#convert the number of hours to full hours plus minutes and seconds
print("it will take", full_days , "days", "+", full_h, "hours","+", min,"min","+ to fill the pond")
