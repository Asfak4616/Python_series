def fahrenheit_to_celsius(fahrenheit): 
    celsius = (fahrenheit - 32) * 5 / 9 
    return celsius 
 
# Main program 
if __name__ == "__main__": 
    # Get user input 
    fahrenheit = float(input("Enter temperature in Fahrenheit: ")) 
     
    # Convert to Celsius 
    celsius = fahrenheit_to_celsius(fahrenheit) 
     
    # Display the result 
    print(f"{fahrenheit}°F is equal to {celsius:.3f}°C") 
