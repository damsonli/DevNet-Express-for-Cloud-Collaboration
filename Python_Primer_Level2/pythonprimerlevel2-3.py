# Nested Data Types

food={"vegetables":["carrots","kale","cucumber","tomato"],"desserts":["cake","ice cream", "donut"]}
print("My favorite vegetable is " + food["vegetables"][0])
print("My favorite dessert is " + food["desserts"][1])

cars={"sports":{"Volkswagon":"Porsche","Dodge":"Viper","Chevy":"Corvette"},"classic":{"Mercedes-Benz":"300SL","Toyota":"2000GT","Lincoln":"Continental"}}
print("My favorite sports car is a Dodge " + cars["sports"]["Dodge"])
print("My favorite classic car is a Lincoln " + cars["classic"]["Lincoln"])

#Parse datatypes with loops
for hungry in food["vegetables"]:
    print("My favorite vegetable is " + hungry)

for auto in cars["sports"]:
    print("My favorite sports car is a " + cars["sports"][auto])

for each in range (len(food["vegetables"])):
    print(food["vegetables"][each])

for each in food["desserts"]:
    print(each)