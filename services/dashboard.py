import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))))
from GetMyParking.services.signup import Signup
from GetMyParking.services.login import Login
from GetMyParking.models.product import Product

class Dashboard:
    def __init__(self):
        self.__Users = {}
        self.__Products = {}
        self.__ActiveLogginUsers = []
        
    def getAllUsers(self):
        return self.__Users
    
    def getAllProducts(self):
        return self.__Products
    
    def getAllActiveLoginUsers(self):
        return self.__ActiveLogginUsers
    
    def setActiveLogginUsers(self,UsersID):
        (self.__ActiveLogginUsers).append(UsersID)
    
    def signUpNewUser(self,UserDetails):
        UserID = UserDetails['ID']
        Password = UserDetails['Password']
        Address = UserDetails['Address']
        Name = UserDetails['Name']
        DOB = UserDetails['DOB']
        IsAdmin = UserDetails['IsAdmin']

        signup = Signup(UserID,Password,Name,Address,DOB,IsAdmin)
        UserObj = signup.completeSignup(self.__Users)
        
        if UserObj:    
            (self.__Users)[UserID] = UserObj
        else:
            print("User Already exists.")
    
    def IsLoggingSuccess(self,UserDetails):
        UserID = UserDetails['ID']
        Password = UserDetails['Password']

        if UserID in  self.__ActiveLogginUsers:
            print("User alrady logged in.")
            return
            
        login = Login(UserID, Password)
        response = login.validateLogin(self.__Users)
        
        if response:
            self.setActiveLogginUsers(UserID)
        else:
            print("Login Failed!!!")

    def IsLogoutSuccess(self,UserDetails):

        if UserDetails["UserID"] in self.__ActiveLogginUsers:
            (self.__ActiveLogginUsers).remove(UserDetails["UserID"])
            print("User Logged out successfully.")
        else:
            print("User Is not in logged in state. Logout Failed!!!")
    
    def setProduct(self,productDetails):
        for productID in self.__Products:
            if productID == productDetails['ID']:
                print("Product already exists!!!")
                return
        
        (self.__Products)[productDetails['ID']] = Product(productDetails["ID"],productDetails["Name"],productDetails["Description"],productDetails["Price"],productDetails['AddedBy'])
    
    def removeProduct(self,ProductID):
        if ProductID in self.__Products:
            del self.__Products[ProductID]
        else:
            print("No such product exists!!!")

    def checkoutProduct(self,UserID, ProductID):
        
        if UserID in self.__Users:
            if ProductID in self.__Products:
                (self.__Users)[UserID].addProductToCheckoutList((self.__Products)[ProductID])
            else:
                print("Product doesn't exist!!!")
        else:
            print("User doesn't exists!!!")