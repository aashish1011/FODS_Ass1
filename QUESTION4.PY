'''Write a program to find the Euclidean distance between two coordinates. Take both the coordinates from the user as input.'''
import math
x1, y1 = map(float, input("Enter the first coordinate (x1 y1): ").split())
x2, y2 = map(float, input("Enter the second coordinate (x2 y2): ").split())
distance=math.sqrt((x2-x1)**2+(y2-y1)**2)
print("The Euclidean distance is:",distance)