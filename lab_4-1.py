#author CJP 11/12/2021
colors = ["red", "yellow", "blue", "green"]
print(colors)

colors.extend(["orange", "black", "white"])
print(colors)

print(colors.count("yellow"))

colors.insert(3, "pink")
print(colors)

colors.clear()
print(colors)

print(colors.count("red"))
