# shopping_cart.py

import datetime as datetime 

def to_usd(my_price):
    return "${0:,.2f}".format(my_price)

def product_match(selected_id, products):
    matching_products = [p for p in products if str(p["id"]) == str(selected_id)]
    matching_product = matching_products[0]
    return matching_product


now = datetime.datetime.now()

if __name__ == "__main__":
    

    products = [  
        {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
        {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
        {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
        {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
        {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
        {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
        {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
        {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
        {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
        {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
        {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
        {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
        {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
        {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
        {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
        {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
        {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
        {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
        {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
        {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
    ] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017


    # Gather our inputs

    total_price = 0
    selected_ids = []
    # checkout_at = datetime.datetime.now()


    while True:
            selected_id = input("Please input a product identifier: ")
            if selected_id == "DONE":
                    break
            else:
                    selected_ids.append(selected_id)


    # Placing our outputs

    print("Selected Products:")

    for selected_id in selected_ids:
        matching_product = product_match(selected_id, products)
        total_price = total_price + matching_product["price"]
        print(" -- " + matching_product["name"] + " (" + to_usd(matching_product["price"]) + ")")
                  
    TAX_RATE = .06
    tax = total_price * TAX_RATE
    You_Pay = total_price + tax




    print("-----------------------------------")
    print(" PRICE: " + to_usd(total_price)) 
    print(" TAX: " + to_usd(tax))
    print(" YOU PAY: " + to_usd(You_Pay))
    print("-----------------------------------")

    

    print(now.strftime("%Y-%m-%d %H:%M:%S"))
    print("-----------------------------------")
    print(" George's Corner Grocery Store")
    print(" www.georgescorner.com")
    print(" Thank you for shopping at George's. Please come again.")
    print("-----------------------------------")
