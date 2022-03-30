class Marca:

    def __init__(self,nombre):
        self.nombre=nombre

    def get_nombre(self):
        return self.nombre

    def set_nombre(self,nombre):
        self.nombre = nombre

class TV:

    def __init__(self):
        self.canal = 1
        self.volumen = 1     
        self.precio = 500
        self.numTV=0              

    def __init__(self,marca,estado):
        self.marca = Marca
        self.estado = estado
        self.control = Control 



    def getMarca(self):
        return self.marca

    def setMarca(self,marca):
        self.marca = marca

    def getControl(self):
        return self.control

    def setControl(self,control):
        self.control = control

    def getPrecio(self):
        return self.precio

    def setPrecio(self,precio):
        self.precio = precio

    def getVolumen(self):
        return self.volumen

    def setVolumen(self,volumen):
        if self.estado == True and volumen <=7 and volumen >=0:
            self.volumen = volumen

    def getCanal(self):
        return self.canal

    def setCanal(self,canal):
        if self.estado == True and canal <=120 and canal >=1:
            self.canal = canal

    def getnumTV(self):
        return self.numTV

    def setnumTV(self,numTV):
        self.numTV = numTV
    
    @classmethod
    def conteoTV(cls):
        cls.numTV+=1

    
    def turnOn(self):
        self.estado = True
    
    def turnOff(self):
        self.estado = False

    def get_Estado(self):
        return self.estado

    def canalUp(self):
        if self.estado == True and self.canal <120:
            self.canal+=1
    
    def canalDown(self):
        if self.estado == True and self.canal > 1:
            self.canal-=1

    def volumenUp(self):
        if self.estado == True and self.volumen <7:
            self.volumen+=1

    def volumenDown(self):
        if self.estado == True and self.volumen > 0:
            self.volumen-=1
    
class Control:

    def __init__(self) :
        self.tv=TV

    def turnOn(self):
        self.tv.turnOn()
    
    def turnOff(self):
        self.tv.turnOff()
    
    def canalUp(self):
        self.tv.canalUp()
    
    def canalDown(self):
        self.tv.canalDown()
    
    def volumenUp(self):
        self.tv.volumenUp()
    
    def volumenDown(self):
        self.tv.volumenDown()
    
    def setCanal(self):
        self.tv.setCanal()

    def setTv(self,tv):
        self.tv = tv

    def enlazar(self,tv):
        self.tv=tv
        self.tv.setControl(self)


        
    


        

    

    
        
        