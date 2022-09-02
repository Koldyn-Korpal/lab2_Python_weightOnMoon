"""
Koldyn Korpal
9/2/22

This code will calculate weight on the Moon.
"""

#Calculates weight on the moon from lbs to oz
objectEarthlbs = float(input("Enter an objects weight on Earth (in lbs): "))
objectMoonlbs = ((objectEarthlbs/9.81)*1.622)
objectMoonOz = objectMoonlbs % 1 * 16

#Calculates weight on the moon from lbs to kg to g
objectMoonKg = objectMoonlbs * 0.453592
objectMoonG = objectMoonKg % 1 * 1000

#Calculates weight on Pythoid from earth lbs to Pythoid lbs to oz
objectPythoidWeight = (4 * ((((objectEarthlbs ** 2) - 13) / 8) + 22) **.5)
objectPythoidlbs = int(objectPythoidWeight//1)
objectPythoidOz = int(((objectPythoidWeight % 1) * 16) + .5)

#Prints out all the weights
print("The objects weight on the Moon is", objectMoonlbs//1, "lbs", round(objectMoonOz, 0), "oz")
print("The objects weight on the Moon is", objectMoonKg//1, "kg", round(objectMoonG, 0) ,"g")
print("The objects weight on the planet Pythoid", objectPythoidlbs//1, "lbs", objectPythoidOz//1, "oz")
