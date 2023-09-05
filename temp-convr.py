
print("welcome to temperature unit converter\ncelcius to fahrenheit or fahrenheit to celcius ")

while True:

    unit = input("Enter 'c' for celcius and 'f' for fahrenheit:")
    temp = input(f"enter the number of temperature in {unit}:")
    print("Click 'Double Enter' for Exit ")   

    if unit =="" and temp=="":
        break
    
    elif unit=="f": 
        temp = int(temp)       
        temp_c = ((temp) - 32) * 5/9.
        print(f"the {temp} fahrenheit in celcius is {temp_c}")

    elif unit=="c": 
        
        temp = int(temp)         
        temp_f = ((temp) * 9/5) + 32.
        print(f"the {temp} celcius in fahrenheit is {temp_f}")

    else:
        print("wrong input\nwrite a valid number")           
  
