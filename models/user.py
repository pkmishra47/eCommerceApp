class User:
    def __init__(self, UserID, Password, Name, Address, DOB, IsAdmin = False):
        self.__ID = UserID
        self.__Password = Password
        self.__Name = Name
        self.__Address = Address
        self.__DOB = DOB
        self.__IsAdmin = IsAdmin
        self.__CheckedOutItems = []

    
    def getUserID(self):
        return self.__ID

    def getPassword(self):
        return self.__Password
    
    def getName(self):
        return self.__Name
    
    def getAddress(self):
        return self.__Address
    
    def getDOB(self):
        return self.__DOB
        
    def IsAdmin(self):
        return self.__IsAdmin
    
    def getCheckedOutItems(self):
        return self.__CheckedOutItems
    
    def addProductToCheckoutList(self,productObj):
        self.__CheckedOutItems.append(productObj)