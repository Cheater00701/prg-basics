prev_price = int(200)
curr_price = int(140)
discount = int(100 - (curr_price / prev_price * 100))
if discount > 10:
    print("Buy the produc!!")
    print(f"Product price reduced by {discount}%")