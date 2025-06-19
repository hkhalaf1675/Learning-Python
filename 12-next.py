
numbersList = [2, 4, 3, 5, 1]
founded = next((item for item in numbersList if item == 14), None)
print(founded)
founded = next((item for item in numbersList if item == 5), None)
print(founded)

print('-----------------------------')
productsList = [
    { "id": 1, "name": "car-bmw", "price": 100 },
    { "id": 2, "name": "car-merci", "price": 200 },
    { "id": 3, "name": "car-lam", "price": 150 },
    { "id": 4, "name": "motor-dyn", "price": 50 },
    { "id": 5, "name": "motor-mast", "price": 70 }
]

founded = next((product for product in productsList if product["name"] == "car-suk"), None)
print(founded)
founded = next((product for product in productsList if product["name"] == "car-bmw"), None)
print(founded)