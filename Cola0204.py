class Cola:
    def __init__(self):
        self.items = []
    
    def enqueue(self, elemento):
        self.items.append(elemento)
        
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        raise RuntimeError("La cola está vacía")
    
    def is_empty(self):
        return len(self.items)==0
    
    def size(self):
        return len(self.items)
        
    def __str__(self):
        return " <- ".join(map(str, self.items))
    
    
colita = Cola()

while True:
    try:
        print("Menu")
        print("1. Encolar")
        print("2. Desencolar")
        print("3. Esta Vacia")
        print("4. Tamaño")
        print("5. Mostrar cola")
        print("0. Salir")
        opcion = int(input("Ingrese una opcion: "))
        match opcion:
            case 1:
                colita.enqueue(input("Ingrese un elemento: "))
                print("Elemento ingresado con éxito.")
            case 2:
                print(f"Se desencoló a {colita.dequeue()}.")
            case 3:
                if colita.is_empty():
                    print("La cola está vacía")
                else:
                    print("La cola no está vacía")
            case 4:
                print(f"Hay {colita.size()} elementos")
            case 5:
                print(colita)
            case 0:
                print("Saliendo...")
                break
            case _:
                print("Opcion invalida.")
    except EOFError:
        print("\nPrograma terminado.")
        break
    except ValueError:
        print("No se ingresó un argumento apropiado.")
    except RuntimeError as e:
        print("Error:", e)
        
    
