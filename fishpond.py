print("Fish Pond Model")
print("==============")
widht = float(input("Enter pond width (meters): "))
length = float(input("Enter pond lenght (meters): "))
depth = float(input("Enter pond depth (meters): "))
print("\n")
print("Results")
print("-------")
area = width * length
print("Surface area of the pond is", area, "square meters")
volume = area * depth
print("Pond contains", volume, "cubic meteres of water")
fish = volume * 2
fins = int(fish)
print("Number of fish: ", fish)
