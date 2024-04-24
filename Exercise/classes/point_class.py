# class as a structure for the object to be created
class Point:
    def move(self):
        print("Move")

    def draw(self):
        print("Draw")


# lets create an object

point = Point()

# lets add things to the object

point.x = 10
point.y = 20

# lets call this newly created object

point.draw()
print(point.x)
print(point.y)
