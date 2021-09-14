# Week 3 Pandas Exercises

import pandas

cars = pandas.read_csv('Automobile_data.csv', index_col=0)

# 1. From given data set print first and last five rows

print('First five rows:')
print(cars.head())
print('Last five rows:')
print(cars.tail())

# 2. Find the most expensive car company name

priciest = cars[cars['price'] == cars['price'].max()].iloc[0]
print('Most expensive car manufactured by:')
print(priciest['company'])

# 3. Print all Toyota cars details

print('All Toyota cars details:')
print(cars[cars['company'] == 'toyota'])

# 4. Count total cars per company

print('Total cars for each company:')
print(cars.groupby('company').size())

# 5. Find each company’s highest priced car

companies = cars['company'].unique().tolist()
for i in companies:
    selection = cars[cars['company'] == i]
    print('Most expensive', i, 'costs', selection['price'].max())

# 6. Find the average mileage of each car making company

companies = cars['company'].unique().tolist()
for i in companies:
    selection = cars[cars['company'] == i]
    print('Mean mileage of', i, 'is', selection['average-mileage'].mean())

# 7. Sort all cars by price column

print('All cars sorted by price:')
print(cars.sort_values(by=['price']))
