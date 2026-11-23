# 1. SPEED
print("\n1. SPEED")
distance = float(input("Enter distance in metres: "))
time = float(input("Enter time in seconds: "))
speed = distance / time
print("Speed =", speed, "m/s")

# 2. FORCE
print("\n2. FORCE")
mass = float(input("Enter mass in kg: "))
acceleration = float(input("Enter acceleration in m/s2: "))
force = mass * acceleration
print("Force =", force, "N")


# 3. WEIGHT
print("\n3. WEIGHT")
mass = float(input("Enter mass in kg: "))
gravity = 9.8
weight = mass * gravity
print("Weight =", weight, "N")


# 4. KINETIC ENERGY
print("\n4. KINETIC ENERGY")
mass = float(input("Enter mass in kg: "))
velocity = float(input("Enter velocity in m/s: "))
kinetic_energy = 0.5 * mass * velocity ** 2
print("Kinetic Energy =", kinetic_energy, "J")


# 5. POTENTIAL ENERGY
print("\n5. POTENTIAL ENERGY")
mass = float(input("Enter mass in kg: "))
height = float(input("Enter height in metres: "))
gravity = 9.8
potential_energy = mass * gravity * height
print("Potential Energy =", potential_energy, "J")

# Assignment 2: Physics Operations - Speed, Force, Weight, KE, PE

def speed():
    distance = float(input("Enter distance (m): "))
    time = float(input("Enter time (s): "))
    s = distance / time
    print(f"Speed = {s} m/s")

def force():
    mass = float(input("Enter mass (kg): "))
    acceleration = float(input("Enter acceleration (m/s²): "))
    f = mass * acceleration
    print(f"Force = {f} N")

def weight():
    mass = float(input("Enter mass (kg): "))
    g = 9.8
    w = mass * g
    print(f"Weight = {w} N")

def kinetic_energy():
    mass = float(input("Enter mass (kg): "))
    velocity = float(input("Enter velocity (m/s): "))
    ke = 0.5 * mass * velocity**2
    print(f"Kinetic Energy = {ke} Joules")

def potential_energy():
    mass = float(input("Enter mass (kg): "))
    height = float(input("Enter height (m): "))
    g = 9.8
    pe = mass * g * height
    print(f"Potential Energy = {pe} Joules")

# MAIN PROGRAM - Runs in while loop infinitely
while True:
    print("\n--- PHYSICS CALCULATOR ---")
    print("1. Speed")
    print("2. Force")
    print("3. Weight")
    print("4. Kinetic Energy")
    print("5. Potential Energy")

    choice = input("Choose an operation (1-5): ")

    if choice == "1":
        speed()
    elif choice == "2":
        force()
    elif choice == "3":
        weight()
    elif choice == "4":
        kinetic_energy()
    elif choice == "5":
        potential_energy()
    else:
        print("Invalid choice!")

    # Ask user if they want to continue
    cont = input("\nDo you want to continue? (yes/no): ").lower()
    if cont != "yes" and cont != "y":
        print("Program ended. Goodbye!")
        break


