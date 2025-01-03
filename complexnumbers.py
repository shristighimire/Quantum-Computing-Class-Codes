# -*- coding: utf-8 -*-
"""Complexnumbers.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1lfJz8_tyNHG6ZG6iG3mfuMiZC5dWCfqD

Programming Drill 1.3.2 If you like graphics, write a program that accepts a small
 drawing around the origin of the complex plane and a complex number. Theprogram
 should change the drawing by multiplying every point of the diagram by a complex
 number
"""

import matplotlib.pyplot as plt
import cmath

drawing = [complex(1, 1), complex(-1, 1), complex(0, -1)] # Original drawing points
real_part = float(input("Enter the real part of the complex number: "))
imaginary_part = float(input("Enter the imaginary part of the complex number: "))
complex_number = complex(real_part, imaginary_part)

transformed_drawing = [point * complex_number for point in drawing]
plt.figure(figsize=(6, 6))
plt.scatter([p.real for p in drawing], [p.imag for p in drawing], color='b', label='Original')
plt.scatter([p.real for p in transformed_drawing], [p.imag for p in transformed_drawing], color='r', label='Transformed')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.gca().set_aspect('equal', adjustable='box')
plt.legend()
plt.grid(True)
plt.title("Original vs Transformed Drawing")
plt.show()

""" Programming Drill 1.3.3 Expand your program. Add functions for multiplication,
 division, and returning the polar coordinates of a number.
"""

operation = input("Choose operation (multiply, divide, polar): ").lower()
if operation == 'multiply':
    transformed_drawing = [point * complex_number for point in drawing]
elif operation == 'divide':
    transformed_drawing = [point / complex_number for point in drawing]
elif operation == 'polar':
    r, theta = cmath.polar(complex_number)
    print(f"Polar coordinates of {complex_number}: r = {r}, theta = {theta} radians")
    exit()
else:
    print("Invalid operation!")
    exit()
plt.figure(figsize=(6, 6))
plt.scatter([p.real for p in drawing], [p.imag for p in drawing], color='b', label='Original')
plt.scatter([p.real for p in transformed_drawing], [p.imag for p in transformed_drawing], color='r', label='Transformed')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.gca().set_aspect('equal', adjustable='box')
plt.legend()
plt.grid(True)
plt.title("Original vs Transformed Drawing")
plt.show()



