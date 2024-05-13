# De�ne a dictionary called agencies that stores a mapping of acronyms CBI, FBI, NIA, SSB, WPA (the keys) to Indian government agencies ‘Centrak Bureau of Investigation’, ‘Foreign Direct Investment’, ‘National Investion Agency’, ‘Service Selection Board’, and ‘Works Progress Administration’(the values) created by Prime Minister during the New Deal.
# Then:
# • Add the map of acronym BSE ‘Bombay Stock Exchange’.
# • Change the value of the key SSB to ‘Social Security Administration’.
# • Remove the (key value) pairs with keys CBI and WPA.


dictionary={
    "CBI":"Centrak Bureau of Investigation",
    "FBI":"Foreign Direct Investment",
    "NIA":"National Investion Agency",
    "SSB":"Service Selection Board",
    "WPA":"Works Progress Administration"    
}
print(dictionary)
print(type(dictionary))
print("**********************************************")

dictionary["BSE"]="Bombay Stock Exchange"

print(dictionary)
print("**********************************************")
# dictionary["SSB"]="Social Security Administration"
dictionary.update({"SSB":"Social Security Administration"})

print(dictionary)
print("**********************************************")

dictionary.pop("CBI")
dictionary.pop("WPA")
print(dictionary)

