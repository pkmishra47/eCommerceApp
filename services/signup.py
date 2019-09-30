import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
from GetMyParking.models.user import User

class Signup:
    def __init__(self,UserID,Password,Name,Address,DOB,IsAdmin = False):
        self.__UserID = UserID
        self.__Password = Password
        self.__Name = Name
        self.__Address = Address
        self.__DOB = DOB
        self.__IsAdmin = IsAdmin
    
    def completeSignup(self,AllUsers):
        
        for userID in AllUsers:
            if userID == self.__UserID:
                return None

        obj = User(self.__UserID, self.__Password, self.__Name, self.__Address,self.__DOB, self.__IsAdmin)
        return obj
