# Vinted Price 

This repository contains a Python script that scrapes Vinted for specific items, analyzes their prices, removes outliers, calculates the average price, and saves the data to a CSV file. This is particularly useful for getting an average market price of items with a lot of listings, like popular sneaker models.

## Features

- Scrape item listings from Vinted based on a search URL.
- Extract and display item titles and prices.
- Convert the prices to a NumPy array for easy manipulation.
- Remove outlier prices using a specified standard deviation threshold.
- Calculate the average price of the items.
- Save the average price to a CSV file with a timestamp.

## Requirements

- Python 3.x
- pyVinted
- numpy
- csv (Python standard library)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/vinted-price-scraper.git
    cd vinted-price-scraper
    ```

2. Install the required packages:
    ```sh
    pip install pyVinted numpy
    ```

## Usage

1. Open the script and modify the search URL as needed:
    ```python
    items = vinted.items.search("https://www.vinted.pt/catalog?search_text=jordan%204%20bred", 100, 1)
    ```

2. Run the script:
    ```sh
    python script_name.py
    ```

3. The script will print the titles and prices of the items found, remove outliers from the prices, calculate the average price, and save this information to a CSV file named `prices.csv`.
