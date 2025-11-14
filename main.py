#Laboratorio python 14/nov_2025
#reviison cambio 2 prueba/4:31

def addmultiplenumbers(numbers):
    return sum(numbers)

def multiplymultiplenumbers(numbers):
    resultado = 1
    for n in numbers:
        resultado *= n
    return resultado

def isitaninteger(num):
    return isinstance(num, int)

def isiteven(num):
    if isitaninteger(num) and num % 2 == 0:
        return True
    else:
        return False
    

def main():
    print("Hello learners!")

if __name__ == "__main__":
    main()
