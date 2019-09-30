import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
from GetMyParking.services.signup import Signup
from GetMyParking.services.login import Login
from GetMyParking.services.dashboard import Dashboard

class GetMyParking:
    def __init__(self):
        pass

    def start_application(self):
        dashboad = Dashboard() 

        while True:

            input_Details = list(input().split())

            if input_Details[0] == "SIGNUP":
                dashboad.signUpNewUser({"ID":input_Details[1],
                                    "Password":input_Details[2],
                                    "Address":input_Details[3],
                                    "Name":input_Details[4],
                                    "DOB":input_Details[5],
                                    "IsAdmin":input_Details[6]
                                })
                print(dashboad.getAllUsers())
            elif input_Details[0] == "LOGIN":
                dashboad.IsLoggingSuccess({ "ID":input_Details[1],
                                        "Password":input_Details[2]
                                        })
                print(dashboad.getAllActiveLoginUsers())
            elif input_Details[0] == "LOGOUT":
                dashboad.IsLogoutSuccess({ "UserID":input_Details[1]})
            elif input_Details[0] == "ADD_PRODUCT":
                userid = input_Details[1] 
                
                if userid in dashboad.getAllActiveLoginUsers():
                    if userid in dashboad.getAllUsers() and dashboad.getAllUsers()[userid].IsAdmin() == "True":
                        dashboad.setProduct({ "ID":input_Details[2],
                                            "Name": input_Details[3],
                                            "Description":input_Details[4],
                                            "Price": input_Details[5],
                                            "AddedBy":userid                                       
                                        })
                    else:
                        print("User is not authorized to add product.")
                else:
                    print("User is not logged in at this moment.")
            elif input_Details[0] == "DELETE_PRODUCT":
                userid = input_Details[1]

                if userid in dashboad.getAllActiveLoginUsers():
                    if userid in dashboad.getAllUsers() and dashboad.getAllUsers()[userid].IsAdmin():
                        dashboad.removeProduct(input_Details[2])
                    else:
                        print("User is not authorized to remove product.")
                else:
                    print("User is not logged in at this moment.")
            elif input_Details[0] == "BROWSE_PRODUCTS":
                products = dashboad.getAllProducts()
                if products:
                    print("Here is the list of products:")

                for productID,productObj in products.items():
                    print("ProductID " + str(productID) + " is  " + productObj.getName())
            elif input_Details[0] == "CHECKOUT_PRODUCT":
                userid = input_Details[1]
                productid = input_Details[2]

                if userid in dashboad.getAllActiveLoginUsers():
                    dashboad.checkoutProduct(userid,productid)
                else:
                    print("User is not logged in at this moment.")
            
            elif input_Details[0] == "CHECKOUT_LIST":
                userid = input_Details[1]

                if userid in dashboad.getAllActiveLoginUsers():
                    checkout_list = dashboad.getAllUsers()[userid].getCheckedOutItems()

                    for items in checkout_list:
                        print(items.getName(),end=', ')
                else:
                    print("User is not logged in at this moment.")
            elif input_Details[0] == "TOPAY":
                userid = input_Details[1]
                topay = 0

                if userid in dashboad.getAllActiveLoginUsers():
                    checkout_list = dashboad.getAllUsers()[userid].getCheckedOutItems()

                    for items in checkout_list:
                        topay += float(items.getPrice())

                    print("Total payable amount is " + str(topay))
                else:
                    print("User is not logged in at this moment.")

if __name__ == '__main__':
    getmyparking = GetMyParking()
    getmyparking.start_application()

    '''
    set of commands

    SIGNUP U1 TEST ADDR PRADEEP 1990-05-22 True
    SIGNUP U2 TEST1 ADDR PRAKASH 1990-05-22 False
    LOGIN U2 TEST1
    ADD_PRODUCT U1 P1 BISCUIT FOOD 10
    ADD_PRODUCT U2 P1 BISCUIT FOOD 10
    ADD_PRODUCT U1 P2 CHOCLATE FOOD 20
    ADD_PRODUCT U1 P3 ICECREAM FOOD 30
    ADD_PRODUCT U1 P4 BRUSH HOUSEHOLD 40
    BROWSE_PRODUCTS
    DELETE_PRODUCT U1 P1
    CHECKOUT_LIST U1
    CHECKOUT_PRODUCT U1 P2
    TOPAY U1
    LOGOUT U1
    '''