catalog = {"Product A":20 , "Product B":40 , "Product C":50}


discount_rules = {"flat_10_discount":(200,10),"bulk_5_discount":(10,0.05),"bulk_10_discount":(20,0.10),"tiered_50_discount":(30,0.50)}

gift_wrap_fee = 1
shipping_fee_per_package = 5
items_per_package = 10


def product_totals(quantity,price,discount_rule,applied_discounts):
    total = quantity * price
    if discount_rule[0] <= quantity:
        discount_amount = total * discount_rule[1]
        applied_discounts[discount_rule[0]] = discount_amount
        total -= discount_amount
    return total


def apply_discounts(total,applied_discounts):
    if applied_discounts:
        max_discount = max(applied_discounts.values())
        total -= max_discount
        discount_name = [name for name,discount in applied_discounts.items() if discount == max_discount][0]
        return total,discount_name,max_discount
    return total,"No discount applied",0

def shipping_fees(total_quantity):
    return (total_quantity - 1) // items_per_package + 1


quantities = {}
gift_wraps = {}

for product in catalog:
    quantity = int(input(f"Enter the quantity of {product}: "))
    quantities[product] = quantity
    gift_wrap = input(f"Is {product} wrapped as a gift? (yes/no): ").lower()
    gift_wraps[product] = gift_wrap == "yes"


subtotal = 0
applied_discounts = {}
for product,quantity in quantities.items():
    price = catalog[product]
    subtotal += product_totals(quantity,price,discount_rules["bulk_5_discount"],applied_discounts)

total_quantity = sum(quantities.values())
shipping_fee = shipping_fees(total_quantity)
gift_wrap_fee_total = sum([quantities[product] * gift_wrap_fee for product, gift_wrap in gift_wraps.items() if gift_wrap])

total,discount_name,discount_amount = apply_discounts(subtotal,applied_discounts)
grand_total = total + shipping_fee + gift_wrap_fee_total


print("Product Details:")
for product,quantity in quantities.items():
    price = catalog[product]
    product_total = product_totals(quantity,price,discount_rules["bulk_5_discount"],applied_discounts)
    print(f"{product}: {quantity} - ${product_total}")

print(f"Subtotal: ${subtotal}")
print(f"Discount Applied: {discount_name} - ${discount_amount}")
print(f"Shipping Fee: ${shipping_fee}")
print(f"Gift Wrap Fee: ${gift_wrap_fee_total}")
print(f"Total: ${grand_total}")
