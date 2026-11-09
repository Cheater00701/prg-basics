truepin = "0805"
tries = 2
while True:
    pin = input("Enter the PIN code: ")
    if tries == 0:
        print("Sorry, your payment card has been blocked.")
        break
    if pin == truepin:
        print("Successful Operation Completed;; PIN code approved")
        break
    else:
        print("Incorrect...") 
        tries += -1