number_of_orders = int(input())

total_cost = 0

for i in range(number_of_orders):
    capsule_price =  float(input())
    days = int(input())
    capsules_ammount = int(input())

    if capsule_price < 0.01 or capsule_price > 100.00:
        continue
    elif days < 1 or days > 31:
        continue
    elif capsules_ammount < 1 or capsules_ammount > 2000:
        continue

    current_cost = capsules_ammount * days * capsule_price
    total_cost += current_cost
    print(f'The price for the coffee is: ${current_cost:.2f}')

print(f'Total: ${total_cost:.2f}')
