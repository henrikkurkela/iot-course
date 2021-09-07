# Write a function that converts from kilograms to pounds. Use the scalar conversion of 2.2 lbs per kilogram to make your conversion. Lastly, print the resulting array of weights in pounds in the main program.

def convert_to_kg(pounds):
    return 2.2 * pounds


weights = [1.0, 2.0, 3.0, 4.0, 5.0]
weights_in_kg = []

for i in weights:
    weights_in_kg.append(convert_to_kg(i))

print('Weights in kilograms:', weights_in_kg)
