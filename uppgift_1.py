def main ():

    memory_value = None # Borjar med att deklarera en tom variable som ska funka som minnet i räknaren!

    def addtion(x, y): return x + y # Defienra summerings funktion som ska ropas senare vid calculering

    def subtract(x, y): return x - y #Defienra mer funktioner på samma sett för andra operationer.

    def multiply(x, y): return x * y

    def divide(x, y): return x / y


    while True: # Här borjar loopen alltid när man startar räknaren eller rensar memory via 'c' 
        
        if memory_value == None:
            first_number = float(input("Enter first number: ")) # här deklrar man det första numret genom inmatning från användaren!
        
        else:
            first_number = memory_value
            print(f"First number is: {first_number}") # Annars första variabeln kan ha ett värde som är lika med resultet från förra operationen
        
        operator = input("Enter operator: ") # Här deklrerar vi en variabel för operation genom att mata in det!

        if operator == 'x': #om input är 'x' då avslutas programmet genom att användra 'break'
            print('... End of calculator ...')
            break
        
        elif operator == 'c': # Om input är lika med 'c' då tommas minnet genom att likna 'memory_value' med 'None'
            memory_value = None
            continue # 'continue' används alltid för att backa till början of loopen

        second_number = float(input("Enter second number: ")) # här deklrar man det andra numret genom inmatning från användaren!

        # Här gör programmet beräkningar genom att känna igen operationen och sen använder sig av de defienerade funktionerna!
        if   operator == '+': 
            result = addtion (first_number, second_number)
        elif operator == '-': 
            result = subtract (first_number, second_number)
        elif operator == '*': 
            result = multiply (first_number, second_number)
        elif operator == '/': 
            result = divide (first_number, second_number)
        else:
            print(f"{operator} not valid!") # om operationen kan inte kännas igen då backar programmet till börjar av loopen!
            continue

        print(f"{first_number} {operator} {second_number} = {result}") # Skriva ut resultet och spara det i minnet av räknaren
        memory_value = result

if __name__ == "__main__":
    main () 