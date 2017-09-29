myvar = {"donut":{"flavors":["chocolate", "jelly", "maple", "plain"]}}

print(myvar["donut"]["flavors"][0])

print("My favorite donut flavors are:", end=" ")
for f in myvar["donut"]["flavors"]:
    print(f, end=" ")

print("\n")

myvar1 = {"type":"donut","flavors":{"flavor":[{"type":"chocolate","id":"1001"}, {"type":"glazed","id":"1002"},{"type":"sprinkled","id":"1003"}]}}

print("Id is: " + str(myvar1["flavors"]["flavor"][0]["id"]) + " type: " + myvar1["flavors"]["flavor"][0]["type"])

for f in myvar1["flavors"]["flavor"]:
    print("Id is: " + str(f["id"]) + " type is: " + f["type"])

# JSON structure validation website: https://jsonlint.com