
# Diamond Data Analysis

This project performs data analysis on a diamond dataset using Python and the pandas library.

## System Requirements

- Python 3.7 or higher
- pandas

## Installation

Before running the code, install the required packages by executing the following command:
```sh
pip install pandas
```

## Data File

Ensure that the data file (`diamonds.csv`) is in the same directory as the script or use an absolute path to the file.

## Usage

Here is a complete example of using the script to analyze diamond data:

```python
import pandas as pd

def load_data(file_path):
    return pd.read_csv(file_path)

def highest_price(data):
    return data['price'].max()

def average_price(data):
    return data['price'].mean()

def count_ideal_cut(data):
    return data[data['cut'] == 'Ideal'].shape[0]

def unique_colors(data):
    colors = data['color'].unique()
    return len(colors), colors

def median_carat_premium(data):
    return data[data['cut'] == 'Premium']['carat'].median()

def average_carat_per_cut(data):
    return data.groupby('cut')['carat'].mean()

def average_price_per_color(data):
    return data.groupby('color')['price'].mean()

# Usage example
file_path = 'diamonds.csv'  # Replace with the correct file name if different
data = load_data(file_path)

print("Highest diamond price:", highest_price(data))
print("Average diamond price:", average_price(data))
print("Number of Ideal cut diamonds:", count_ideal_cut(data))
num_colors, colors = unique_colors(data)
print("Number of unique colors:", num_colors)
print("The unique colors are:", colors)
print("Median carat of Premium cut diamonds:", median_carat_premium(data))
print("Average carat per cut:")
print(average_carat_per_cut(data))
print("Average price per color:")
print(average_price_per_color(data))
```

## Data Analysis Results

- **Highest diamond price**: 18,823
- **Average diamond price**: 3,932.80
- **Number of Ideal cut diamonds**: 21,551
- **Number of unique colors and their names**: 
  - Number of unique colors: 7
  - The unique colors are: ['E', 'I', 'J', 'H', 'F', 'G', 'D']
- **Median carat of Premium cut diamonds**: 0.86
- **Average carat per cut**:
  - Fair: 1.046
  - Good: 0.849
  - Ideal: 0.703
  - Premium: 0.892
  - Very Good: 0.806
- **Average price per color**:
  - D: 3169.95
  - E: 3076.75
  - F: 3724.89
  - G: 3999.14
  - H: 4486.67
  - I: 5091.87
  - J: 5323.82

## Notes

If you have any additional questions or if you would like to analyze more data, feel free to reach out!
