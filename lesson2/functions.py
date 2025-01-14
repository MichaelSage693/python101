import math

def add(x, y):
    return x + y

x = 5
y = 11

# Convert Celsius to Fahrenheit (0°C × 9/5) + 32 = 32°F
def convert_celsius_to_fahrenheit(c: int) -> int:
    return (c * 9/5) + 32

celsius = 100
fahrenheit = convert_celsius_to_fahrenheit(celsius)
#print(fahrenheit)

# Almighty quadratic equation formula ax2 + bx + c = 0 -> (x1, x2)
def quadratic_solution(a=0, b=0, c=0):
    evaluate = math.sqrt(math.pow(b, 2) - (4 * a * c))
    x1 = (-b + evaluate) / (2 * a)
    x2 = (-b - evaluate) / (2 * a)

    return x1, x2


a = 5
b = 6
c = 1

solution = quadratic_solution(a, b, c)

print(f"{a}x2 + {b}x + {c} evaluates to x={solution[0]:.2f} or x={solution[1]:.2f}")