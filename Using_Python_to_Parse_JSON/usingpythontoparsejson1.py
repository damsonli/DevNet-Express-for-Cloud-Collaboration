var1 = {"car":"volvo", "fruit":"apple"}

print(var1["fruit"])

for f in var1:
    print("key: " + f + ", value: " + var1[f])

var2 = {"donut":["chocolate", "glazed", "sprinkled"]}

print(var2["donut"][0])

print("My favorite donut flavors are:", end=" ")
for f in var2["donut"]:
    print(f, end=" ")
