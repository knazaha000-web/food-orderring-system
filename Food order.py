# Food ordering sytem

MENU = 
      ("Burger", MVR 50),
      ("Pizza", MVR 100),
      ("Coffee", MVR 20),
      ("Tea", MVR 15),
      ("Sandwhich", MVR 40),
      ("Juice", MVR 30)


  print("=== MY CAFE MENU ===")
  for item in menu:
     print(item[0]), "- MVR", item[1])

     order = []
     total = 0

# Ask the user for 3 items
for i in range (3):
    choice = input ("\nEnter item name: ")

    found = False

    for item in menu:
        if choice.lower() == item[0].lower():
           order.append (item)
           total += item [1]
           found = True
           break

           if not found:
           print("Item Not Found In Menu.")

      #Receipt
      print ("\n=== RECEIPT ===")

      for item in order:
        print(item[0]), "- MVR", item[1])
        print("\nTotal Price: MVR", total)

     # Discount
if total > 100:
      dicoount = total * 0.10
      discounted_total = total - discount
      
      print("10% Discount Applied : MVR", discount)
      print("Discounted Total: MVR", discounted_total)


