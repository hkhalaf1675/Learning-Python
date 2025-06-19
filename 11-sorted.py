
numbersList = [2, 11, 22, 5, 7, 15, 33, 17, 20, 30, 1]
print(numbersList)

sortedNumbersListAsc = sorted(numbersList)
print(sortedNumbersListAsc)

sortedNumbersListDesc = sorted(numbersList, reverse=True)
print(sortedNumbersListDesc)

print('---------------------------------------------------')

productsList = [
    { "id": 1, "name": "car-bmw", "price": 100 },
    { "id": 2, "name": "car-merci", "price": 200 },
    { "id": 3, "name": "car-lam", "price": 150 },
    { "id": 4, "name": "motor-dyn", "price": 50 },
    { "id": 5, "name": "motor-mast", "price": 70 },
]
print(productsList)

sortedProductsListAsc = sorted(productsList, key=lambda x: x["price"])
print(sortedProductsListAsc)

sortedProductsListDesc = sorted(productsList, key= lambda x: x["price"], reverse=True)
print(sortedProductsListDesc)