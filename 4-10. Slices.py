#Taken from 4-9. Cube Comprehension
cubes = [x**2 for x in range(1,11)]
for cube in cubes:
    print(cube)

print("The first three items on the list are:" + str(cubes[:3]))
print("Three items from the middle of the list are: " + str(cubes[3:6]))
print("The last three items on the list are: " + str(cubes[-3:]))
