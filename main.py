import sys

sys.path.append('./fibonacci_project')

from fibonacci_project import generate_fibonacci  

if __name__ == "__main__":     
	n = 10  # Changer la valeur si nécessaire  
	result = generate_fibonacci(n)     
	print(f"Fibonacci sequence of {n} elements: {result}") 
