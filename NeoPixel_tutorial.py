class VektorToIndexConverter:
    def __init__(self, dimX, dimY):
        self.dimX =dimX
        self.dimY =dimY
        

    def xyToIndex(self, x,y):
    
        
        

        if x >=self.dimX:
            x = max(0, min(x, self.dimX - 1))
        if y>=self.dimY:
            y = max(0, min(y, self.dimY - 1))

        if x%2 == 0:
            index = x*self.dimX +y
        else:
            index = x*self.dimX+(self.dimY-1) -y

        return index

vektortoindex = VektorToIndexConverter(16,16) # klasse mit matrix dimensionen initalisieren
index = vektortoindex.xyToIndex(3,5) # als Test
print(index)

matrix = neopixel.NeoPixel(pin0,256) # Klasse initalisieren

matrix[index]=(15,30,145)  # Pixel anmachen mit RGB werten
matrix.show()   # MUSS genutzt werden um änderungen zu übernehmen