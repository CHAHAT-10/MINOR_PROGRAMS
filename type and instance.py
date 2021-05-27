class polygon:
    def sides_no(self):
       pass

class triangle(polygon):
    def area(self):
       pass

obj_polygon = polygon()
obj_triangle = triangle()

print(type(obj_triangle) == triangle)
print(type(obj_triangle) == polygon)

print(isinstance(obj_polygon, polygon))
print(isinstance(obj_triangle,polygon))