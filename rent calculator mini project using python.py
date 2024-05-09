rent=int(input("enter the rent of the room"))
food=int(input("enter the food charges"))
electricity=int(input("enter the electricity bill anount"))
persons=int(input("enter the number of people living together"))
total_bill=(rent+food+electricity)//persons
print(f"each person have to pay {total_bill} rupees")