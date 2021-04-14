# name: Zara 
# creation_date: 1975 
# creator_name: Amancio Ortega Gaona 
# type_of_clothes: men, women, children, home 
# international_competitors: Gap, H&M, Benetton 
# number_stores: 7000 
# major_color: France -> blue, Spain -> red, US -> pink, green 

brand = {
    'name': 'Zara', 
    'creation_date' : 1975, 
    'creator_name' : 'Amancio Ortega Gaona', 
    'type_of_clothes': ['men', 'women', 'children', 'home'], 
    'international_competitors': ['Gap', 'H&M', 'Benetton'], 
    'number_stores' : 7000, 
    'major_color' : {'France': 'blue', 'Spain': 'red' , 'US': ['pink', 'green'] },
}


# brand['number_stores'] = 2
# print(brand)
# print(brand['name'] + ' clients are men, women and children')
# brand['international_competitors'] = ['Gap', 'H&M', 'Benetton', 'Desigual']
# print(brand)

# brand.pop('creation_date')
# print(brand)

# print(brand['international_competitors'][2])

# print('the major clothes’ colors in the US are ' + str(brand['major_color']['US']))

# brand_value = brand.items()
# print(brand)

# brand.items()
# print(brand)

more_on_zara = {
    'creation_date' : 1975, 
    'number_stores' : 10000,
 }
 
brand.update(more_on_zara)
print(brand)
print(brand['number_stores'])