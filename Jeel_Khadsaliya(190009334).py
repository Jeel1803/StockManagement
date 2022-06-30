#creating a global 2D list to store detail of products
inventory = ["DH03G",["Lewis Tshirt","Tshirt","Large","45","26"],"YUW04",["Skinny Jeans","Jeans","32","75","14"],"OP3ER",["H&M Shorts","Shorts","28","25","40"]]
 

#defining function to add products        
def add_product():
    
    code = input("Please enter cloth code: ")
    # defining function to check the code, if it exist or not    
    def check_product(code):
        if code in inventory:
            print("This code is not available for this option. Please use other OPTION or CODE")
            return add_product()
        else:
            inventory.append(code)
            
            #creating empty list to store the attributes
            data_table = []
                    
            name = input("Enter Clothing Brand Name: ")
            cat = input("Enter Clothing Category: ")
            size = input("Enter Clothing Size: ")
            price = float(input("Enter Clothing Price: $"))
            
            #function that makes sure quantity is entered between of 10 and 50
            def check_quant():                
                quant = int(input("Enter Clothing Quantity: "))
                        
                if quant < 10 or quant > 50:
                    print("Please enter quantity between 10 and 50")
                    return check_quant()
                else:
                    print("Product added successfully.....!")
                            
                    data_table.extend([name,cat,size,price,quant])
                    inventory.append(data_table)
                            
                re_choice = input("Do you want to add more products? Enter Yes or No: ")
                while(re_choice.upper() !="YES" or re_choice.upper() !="NO" ):
                        if re_choice.upper() == "YES":
                            print("-----------------------------------------------------------------------")
                            return add_product()
                        elif re_choice.upper() == "NO":
                            print("-----------------------------------------------------------------------")
                            return main_program()
                        else:
                            print("INVAILD INPUT")
                            re_choice = input("Do you want to add more products? Enter Yes or No: ")
                            
                            

                            
            check_quant()
    check_product(code)
            
    
# defining function for searching product        
def search_product(code):
                   
    def check_code(code):
        
        #checking if code exist in inventory, if exist print details
        if code in  inventory:
            ind = inventory.index(code) + 1
            print("Yes the product with this code exist")
            print("-----------------------------------------------------------------------")
            print("Product Brand Name:",inventory[ind][0])
            print("Product Caterogy:",inventory[ind][1])
            print("Product Size:",inventory[ind][2])
            print("Product Price: $",inventory[ind][3])
            print("Product Quantity available:",inventory[ind][4])
            print("-----------------------------------------------------------------------")
        else:
            print("This code doesn't exist. Please enter VALID code.....")
            code = input("Please enter the code of product to be searched:  ")
            return search_product(code)
                     
        return main_program()
    check_code(code)    

#defining function that let user to update product details        
def update_product(code):
            
    
    #validating code in inventory
    if code in  inventory:
        print("Yes this product exist")
        ind = inventory.index(code) + 1
        
        print("Product Brand Name:",inventory[ind][0])
        print("Product Caterogy:",inventory[ind][1])
        print("Product Size:",inventory[ind][2])
        print("Product Price: $",inventory[ind][3])
        print("Product Quantity available:",inventory[ind][4])
        print("-----------------------------------------------------------------------")
        
        #asking user's choice to update attributes one by one
        updateName = input("Do you want to update product Brand Name? Please enter Yes or No:  ")
        if updateName.upper() == "YES":
            update_name = input("Please enter new Brand Name:  ")
            inventory[ind][0] = update_name
        
        updateCategory = input("Do you want to update product category? Please enter Yes or No:  ")
        if updateCategory.upper() == "YES":
            update_cat = input("Please enter new category:  ")
            inventory[ind][1] = update_cat
                                      
        updateSize = input("Do you want to update product Size? Please enter Yes or No:  ")
        if updateSize.upper() == "YES":
            update_size = input("Please enter new Size:  ")
            inventory[ind][2] = update_size
                                    
        updatePrice = input("Do you want to update product Price? Please enter Yes or No:  ")
        if updatePrice.upper() == "YES":
            update_price = float(input("Please enter new Price: $ "))
            inventory[ind][3] = update_price
                                    
        updateQuantity = input("Do you want to update product Quantity? Please enter Yes or No:  ")
        
        #again a function that makes sure that the quantity is entered between 10 and 50
        def check_quant():
                    
            if updateQuantity.upper() == "YES":
                update_quantity = int(input("Please enter new quantity:  "))
                if update_quantity < 10 or update_quantity > 50:
                    print("Please enter quantity between 10 and 50")
                    return check_quant()
                else:
                    inventory[ind][4] = update_quantity
        check_quant()
        print("-----------------------------------------------------------------------")
                        
    else:
        print("This code doesn't exist. Please enter VALID code.....")
        code = input("Please enter the code of product to update:  ")
        return update_product(code)
        print("-----------------------------------------------------------------------")
    return main_program()
    
#defining function that let user to buy products        
def buy_product():
    
    code = input("Please enter the code of cloth you want to buy:  ")
    #validating code w.r.t to inventory
    def check_code(code):
        
        
        if code not in inventory:
            print("Invalid code. Please enter valid code")
            
            return buy_product()
        else:
            index = inventory.index(code)
        
        
        quantity = int(input("Please enter the quantity: "))
        
        #checking if entered quantity is available for sell           
        def check_quantity(quantity):
            lst_quantity = int(inventory[index+1][4])
            lst_name = (inventory[index+1][0])
            lst_price = int(inventory[index+1][3])
            
            #code to make sure there are atleast 10 product available all times
            available = lst_quantity - 10
            lst_quantity  = available
            if lst_quantity <= 0:
                lst_quantity = 0
            
            if (quantity>lst_quantity):                   
                print("There is only", lst_quantity,"of the " , lst_name,"availabe for sale" )
                quantityChoice = input("Do you want to enter new quantity? Enter yes or no:  ")
                while(quantityChoice.upper() !="YES" or quantityChoice.upper() !="NO" ):
                    if quantityChoice.upper() == "YES":
                        quantity = int(input("Please enter the quantity: "))
                        return check_quantity(quantity)
                    elif quantityChoice.upper() == "NO":
                        print("-----------------------------------------------------------------------")
                        return main_program()
                    else:
                        print("INVAILD INPUT")
                        quantityChoice = input("Do you want to enter new quantity? Enter yes or no:  ")
                    
            #calulating price for the products bought        
            else:
                
                if quantity >=10 and quantity <=20:
                    gst_inclusive = (quantity * lst_price + (quantity * lst_price * 0.15 ))
                    discount = gst_inclusive * 0.10
                    price = gst_inclusive - discount
                            
                elif quantity >=20 and quantity <=30:
                    gst_inclusive = (quantity * lst_price + (quantity * lst_price * 0.15 ))
                    discount = gst_inclusive * 0.20
                    price = gst_inclusive - discount
                            
                elif quantity >=30:
                    gst_inclusive = (quantity * lst_price + (quantity * lst_price * 0.15 ))
                    discount = gst_inclusive * 0.30
                    price = gst_inclusive - discount
                            
                else:
                    price = (quantity * lst_price)
                    
                    
            print("The total price to pay is: ", price)
            print("-----------------------------------------------------------------------")
            
            
            #managing stock 
            available_quantity = lst_quantity - quantity
            inventory[index+1][4] = available_quantity
            
            
        check_quantity(quantity)                    
    check_code(code)

    return main_program()
    
#function to exit program
def exit_program():
    print("Good Bye")
    exit(0)
    

print("=======================================================================")
print("              Welcome to the 'FASHION SWAG' Shopping                   ")
print("=======================================================================")

def main_program():
    
    print("Please select one of the following options:")
    print("1. Add Product \n2. Search Product \n3. Update Product \n4. Buy Product \n5. Exit")
    
    choice = int(input("Please enter 1, 2, 3, 4 or 5: "))
    print("-----------------------------------------------------------------------")

    if choice == 1:
        add_product()
    elif choice == 2:
        code = input("Please enter the code of product to be searched:  ")
        search_product(code)
    elif choice == 3:
        code = input("Please enter the code of product to update:  ")
        update_product(code)
    elif choice == 4:
        buy_product()
    elif choice == 5:
        exit_program()
        
        
    else:
        print("INVALID INPUT")
        reChoice = input("Do you want to return to main program. Enter yes or no:  ")
        if reChoice == "yes":
            print("-----------------------------------------------------------------------")
            return main_program()
        else:
            print("Good Bye")
            exit(0)
   
 
main_program()



