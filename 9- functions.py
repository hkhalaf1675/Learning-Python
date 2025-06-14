
def hello():
    print("hello world")
hello()

print('-----------------------')
def welcomeVisitor(visitorName):
    print('Hello Mr.' + visitorName)

welcomeVisitor('Hassan')
welcomeVisitor('Ahmed')

print('-----------------------')
def setDefualtValueToFunctionPatameter(value = 'World'):
    print('Hello ' + value)

setDefualtValueToFunctionPatameter()
setDefualtValueToFunctionPatameter('Alex')

print('-----------------------')
def sayHelloToManyVisitors(*visitors):
    for visitor in visitors:
        print("Hello Mr." + visitor)

sayHelloToManyVisitors("Hassan", "Ahmed", "Mhmd")

print('-----------------------')
def passParameterByKey(key3, key2, key1):
    print(key1)
    print('---')
    print(key2)
    print('---')
    print(key3)

passParameterByKey(key1= 'One', key2 = 'Two', key3 = 'Three')

print('-----------------------')
def passManyParameters(**params):
    print(params)
    print('---')
    print(params['key1'])
    print('---')
    print(params['key2'])

passManyParameters(key1 = 'One', key2 = 'Two', key3 = 'Three')

print('-----------------------')
def calculateCirculeArea(radius):
    return 3.14 * (radius * 2)
print(calculateCirculeArea(2))

print('-----------------------')
squareLambdaFun = lambda x: x * x
print(squareLambdaFun(25))

print('-----------------------')
sumTwoNumbersLambdaFun = lambda x, y: x + y
print(sumTwoNumbersLambdaFun(1, 55))
