print("Size of Pond")
print("------------")
width = input("Enter pond width(meters): ")
width = float(width)
length = input("Enter pond length(meters): ")
length = float(length)
depth = input("Enter pond depth(meters): ")
depth = float(depth)
area = width * length
volume = area * depth
print(volume, "cubic meteres of water")
print("\n")

print("Filling the pond")
print("----------------")
second = input("Enter liters per second: ")
second = float(second)
hour = second * 3600
print(hour, "litters per hour")
day = hour * 24
#convert liters per day to cubic meteres per day (1000L=m^3)
day = day/1000
print(day,"cubic meteres per day")
'''
The number of days to fill the pond is the volume of the
pond, divided by the water flow in one day
'''
days = volume/day

#round the number to 2 decimal places
days = round(days,2)

print("it will take", days, "days to fill the pond")

#convert the numbers of days to full days plus exrra hours
full_days = int(days)
part_day = days - full_days
hours = part_day * 24
print("it will take", full_days, "days","+",hours,"hours to fill the pond")
