#1 la interfaz son los mensajes que entiende el objeto, en este caso: c



"""class Perro:
    def __init__(self):
        self._alimento = 0
        self._caricias = 0

    def energia(self):
        return self._alimento + (self._caricias * 10)

    def comer(self, gramos):
        self._alimento += gramos

    def acariciar(self):
        self._caricias += 1

    def estaDebil(self):
        return self._caricias < 2"""""


#3 Creá una clase Notebook cuyo estado sea: marca, modelo y precio, y que tenga un método que le aplique un descuento al precio, el cual tiene que recibir un número entero (el porcentaje de descuento) y tiene que devolver cuánto valdría esa notebook si se aplicase el descuento. Por último hay que instanciar esta clase y en algunos casos aplicar este descuento.

"""class Notebook:
    def __init__(self,marca,modelo,precio):
        self.marca = marca
        self.modelo = modelo 
        self.precio = precio
    
    def aplicar_descuento(self,numero):
        descuento = self.precio * numero 
        precio_con_Descuento = self.precio - descuento"""""

#4 Definí una clase que modele un contador, el cual puede incrementar o disminuir en uno el valor que se ingresa, recordando el valor actual. También puede resetear este valor y al hacerlo se pone en cero. Además es posible indicar directamente un número nuevo que reemplace al valor actual. Este objeto debe entender los siguientes mensajes:
#inc()
#dis()
#reset()
#valorActual()
#valorNuevo(nuevoValor)

"""class contador:
    def __init__(self,valor):
        self.valor = valor

    def dis(self):
        self.valor -= 1

    def inc(self):
        self.valor += 1  

    def reset(self):
       self.valor = 0

    def valorActual(self):
        return self.valor    

    def valorNuevo(self, nuevo):
       self.valor == nuevo 
        

pepita = contador(10)"""""

#5
class contador:
    def __init__(self,valor):
        self.valor = valor
        self.lista_comandos = []

    def dis(self):
        self.valor -= 1
        self.lista_comandos.append("disminucion")

    def inc(self):
        self.valor += 1  
        self.lista_comandos.append("incrementar")

    def reset(self):
       self.valor = 0
       self.lista_comandos.append("reset")

    def valorActual(self):
        return self.valor    

    def valorNuevo(self, nuevo):
       self.valor == nuevo 
       self.lista_comandos.append("actualizacion")
    def ultimo_comando (self):
        self.lista[-1]


pepita = contador(10)


