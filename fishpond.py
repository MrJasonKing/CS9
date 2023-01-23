print("Fish Pond Model")
print("==============")
width = float(input("Enter pond width (meters): "))
length = float(input("Enter pond length (meters): "))
depth = float(input("Enter pond depth (meters): "))
print("\n")
print("Results")
print("-------")
area = width * length
print("Surface area of the pond is", area, "square meters")
volume = area * depth
print("Pond contains", volume, "cubic meters of water")
fish = volume * 2
fins = int(fish)
print("Number of fish: ", fish)
