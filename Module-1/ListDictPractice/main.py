carList = ["Toyota", "Jaguar", "Ford"]
print(carList)

carList.append("Honda")
print(carList)

print(carList[0])

carList.insert(1, "Porsche")
print(carList)

carList.remove("Ford")
print(carList)

for car in carList:
    print(car)

carDict = {
    "brand": "Jaguar",
    "model": "F-Type",
    "drivetrain": "rear-wheel"
}

print(carDict["model"])
print(carDict["drivetrain"])
print(carDict)

model = carDict.get("model")
print(model)

model2 = carDict["model"]
print(model2)

print(carDict.keys())

carDict["drivetrain"] = "all-wheel"
print(carDict["drivetrain"])

carDict["Year"] = 2018
print(carDict.keys())
print(carDict["Year"])