sale_cost = float(input("enter sale cost"))
actual_cost = float(input("enter actual cost"))

if sale_cost>actual_cost :
    profit = sale_cost - actual_cost
    print (" you have a profit = {0}".format(profit))

else :
    loss = actual_cost - sale_cost
    print("you have loss = {0}".format(loss))
   