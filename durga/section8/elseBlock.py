cart = [10, 20, 30, 40, 50]

for item in cart:
    if item > 500:
        print('Order cannot be placed w/o insurance')
        break
    print('Processing item: ', item)
else:
    print('All items processed successfully')