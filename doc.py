class carro():
    
    def __init__(self, name):
        self.nombre = name
        
    def acelerar(self):
        print ("estoy acelerando")

    def transportar(self,per):
        print ("estoy transpotando",per,"personas",self.nombre)
       
bmw01 = carro("bmw01")
bmw01.acelerar()
bmw01.transportar(4)

mazda01 = carro("mazda01")
mazda01.acelerar()
mazda01.transportar(10)