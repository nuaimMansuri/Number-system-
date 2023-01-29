conversion_table = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A' , 'B', 'C', 'D', 'E', 'F']

decimal = int(input("\nEnter the decimal Number: "))
hexadecimal = ''

while(decimal>0):
    remainder = decimal%16
    hexadecimal = conversion_table[remainder]+ hexadecimal
    decimal = decimal//16
    
print("Hexadecimal number is: ",hexadecimal)
