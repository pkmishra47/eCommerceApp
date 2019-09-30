import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
from datetime import datetime

class Login:
    def __init__(self,UserID,Password):
        self.__UserID = UserID
        self.__Password = Password
        self.__LoginDateTime = datetime.now()
    
    def validateLogin(self,AllUsers):
        
        for userid,userobj in AllUsers.items():
            if userid == self.__UserID:
                if userobj.getPassword() == self.__Password:
                    return True
        return False

