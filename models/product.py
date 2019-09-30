class Product:
    def __init__(self,ProductID, ProductName, ProductDescription, ProductPrice, UserID):
        self.__ID = ProductID
        self.__Name = ProductName
        self.__Description = ProductDescription
        self.__Price = ProductPrice
        self.__AddedBy = UserID
    
    def getID(self):
        return self.__ID
    
    def getName(self):
        return self.__Name
    
    def getDescription(self):
        return self.__Description
    
    def getPrice(self):
        return self.__Price

