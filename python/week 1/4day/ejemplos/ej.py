# EX 3
brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": "blue",
        "Spain": "red",
        "US": ["pink", "green"]
    }
}
brand["number_stores"] = 2
print("Our customers are:", ", ".join(brand["type_of_clothes"][:3]))
brand["country_creation"] = "Spain"
if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")
else:
    brand["international_competitors"] = ["Desigual"]
# EX 4
users = ["Mickey", "Minnie", "Donald","Ariel","Pluto"]
for name in users:
    if "i" in name and name[0] in ["M","P"]:
        print(name)