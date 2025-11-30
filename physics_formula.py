print("my physics formulas")
print("a = force formula")
print("b = power formula")
print("c = pressure formula")
print("d =  work formula")
print("e = distance formula")
print()

z = input("what formula is preferrable by you in the 5 formulas")

#Force
if z == "a":
    print("Force = m * a")
    mass = float(input("Enter mass(kg): "))
    acceleration = float(input("Enter acelleration(m/s^2):"))
    force = mass * acceleration 
    print(f"/nforce = {force} N")

#Power 
elif z == "b":
    print("Power = W/t")
    work = float(input("Enter work(J): "))
    time = float(input("Enter time(s):"))
    Power = work / time
    print(f"/nPower = {Power} Watts")

#pressure
elif z == "c":
    print("pressure = f / a")
    force = float(input("Enter force(n): "))
    Area = float(input("Enter Area(m^2):"))
    pressure = force / Area
    print(f"/npressure = {pressure} Pa")

#work
elif z == "d":
    print("work = f * d")
    force = float(input("Enter force(n): "))
    distance = float(input("Enter distance(m): "))
    work = force * distance 
    print(f"/nwork = {work} joulse")

#distance 
elif z == "e":
    print("distance = s * t")
    speed = float(input("Enter speed(m/s): "))
    time = float(input("Enter time(t):"))
    distance = speed * time
    print(f"/ndistance = {distance} m")

else:
     print ("invalid (choose between formula a-e)")