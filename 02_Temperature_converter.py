import sys
def Celsius(temp):
    k=temp+273.15
    f=temp*9/5+32
    print("\n",temp," in Celsius degrees is ",k," in Kelvin and ",f," in Fahrenheit degrees")
def Kelvin(temp):
    c=temp-273.15
    f=temp*9/5-459.67
    print("\n",temp," in Kelvin is ",c," in Kelvin and ",f," in Fahrenheit degrees")
def Fahrenheit(temp):
    c=(temp-32)*5/9
    k=(temp+459.67)*5/9
    print("\n",temp," in Fahrenheit degrees is ",c," in Celsius degrees and ",k," in Kelvin")
temp=float(input("Write temp to convert\n"))
unit=int(input("Choose unit\n1.Celsius\n2.Kelvin\n3.Fahrenheit\n"))
if unit==1: 
    Celsius(temp)
elif unit==2: 
    Kelvin(temp)
elif unit==3: 
    Fahrenheit(temp)
else: 
    sys.exit("Wrong number")