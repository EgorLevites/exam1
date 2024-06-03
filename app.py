import pandas as pd

# Read the data from the file
file_path = 'diamonds.csv'  # replace with the correct file name if different
data = pd.read_csv(file_path)

# 1. What is the highest diamond price?
highest_price = data['price'].max()

# 2. What is the average diamond price?
average_price = data['price'].mean()

# 3. How many diamonds of Ideal cut are there?
ideal_count = data[data['cut'] == 'Ideal'].shape[0]

# 4. How many different colors do the diamonds have? What are they?
unique_colors = data['color'].unique()
num_unique_colors = len(unique_colors)

# 5. What is the median carat of Premium cut diamonds?
median_carat_premium = data[data['cut'] == 'Premium']['carat'].median()

# 6. Create the average carat for each cut type
average_carat_per_cut = data.groupby('cut')['carat'].mean()

# 7. Create the average price for each color type
average_price_per_color = data.groupby('color')['price'].mean()

# Display the results
print(f"Highest diamond price: {highest_price}")
print(f"Average diamond price: {average_price}")
print(f"Number of Ideal cut diamonds: {ideal_count}")
print(f"Number of different diamond colors: {num_unique_colors}")
print(f"The different colors are: {unique_colors}")
print(f"Median carat of Premium cut diamonds: {median_carat_premium}")
print(f"Average carat for each cut type: \n{average_carat_per_cut}")
print(f"Average price for each color type: \n{average_price_per_color}")
