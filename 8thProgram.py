# Develop a bike rental system that enables the customer to see 
# available bikes on the shop and hire bikes base their needs.
# Rent bikes on hourly basis Rs 100 per hour
# Rent bikes on daily basis Rs 500 per day
# Rent bikes on weekly basis Rs 2500 per week
# Family Rental, a promotional that can include from
# (3 to 5 Rentals (of any type) with a discount of 30% of

print("Welcome to Bike Shop")
bikes=["MTB","Geared","Non Geared","With Training Wheels","For Trial Riding"]

a=0
while a<4:
    bill=0
    # print("choose any of the following services:")
    print("1)view bikes on sale\n2)view bike price\n3)place order \n4)exit")
    a=int(input("choose any of survices\n"))
    if a==1:
        print("bikes which are avaivble are:")
        for el in bikes:
            print(el)
    elif a==2:
        print("prices of bikes")
        print("\n hourly --> 100 \n daily -->500 \n weekly --> 2500 \n family pack get 30% discount on 3-5 bikes ")
    elif a==3:
        print("rental types are : 1)hourly \n 2)daily \n 3)weekly \n ")
        c=int(input("please enter the choice\n"))
        d=int(input("no of bikes"))
        if c==1:
            bill+=100*d
        elif c==2:
            bill+=500*d
        elif c==3:
            bill+=2500*d
        else :
            print("choose corect one")
        if d in range(3,6):
            print("Do you wanna avail family pack discount?\n")
            dis = input("y for YES\nn for NO\n")
            print("-----------------------------") 
            if dis == "y":
                bill = bill*0.7
            else:
                bill = bill
        print("Thanks for purchasing", bill, "is your bill, pay on checkout")
    else:
        break
          