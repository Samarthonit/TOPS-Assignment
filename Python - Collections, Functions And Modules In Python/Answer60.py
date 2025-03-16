Radius = float(input("Enter the Radius of the cylinder: "))
Height = float(input("Enter the Height of the cylinder: "))

Surface_area = 2 * 3.14159265359 * Radius * (Radius + Height)

Volume = 3.14159265359 * Radius**2 * Height

print(f"Surface Area of the cylinder: {Surface_area}")
print(f"Volume of the cylinder: {Volume}")
