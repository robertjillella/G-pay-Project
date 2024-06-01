from User import *
 
class GpayController:
    def __init__(self):
        self.dataStore = {}
 
    def handleSignup(self):
        mobileNumber = input("Enter your mobile number: ")
        if mobileNumber in self.dataStore:
            print("Account existed with this mobile number, kindly pleas login")
            return
        otp = input("Enter the 4-digit OTP: ")
        fullName = input("Enter your fullName: ")
 
        while True:
            securityPin1 = input("Select 4-digit pin: ")
            securityPin2 = input("Re-Enter the 4-digit security Pin: ")
            if securityPin1 != securityPin2:
                print("Pin didn't matched, kindly please try again")
            else:
                print("Pin set successfully")
                break
 
        newUser = User()
        newUser.fullName = fullName 
        newUser.pin = securityPin1 
        newUser.mobileNumber = mobileNumber
        self.dataStore[mobileNumber] = newUser 
        print("Data inserted into database successfully")
 
 
    def handleLogin(self):
        mobileNumber = input("Enter your registered mobile number: ")
        if mobileNumber not in self.dataStore:
            print("User haven't registered yet on G-Pay, kindly please register first before login")
            return 
        user = self.dataStore[mobileNumber]
        availableAttempts = 3 
        while availableAttempts > 0:
            pin = input("Enter your 4-digit security pin: ")
            if user.pin != pin:
                if availableAttempts - 1 == 0:
                    print("Your account temporarily blocked for next 24 hours")
                else:
                    print("Wrong pin, you have", (availableAttempts - 1), " attempts left")
            else:
                print("Logged in successfully")
            availableAttempts -= 1