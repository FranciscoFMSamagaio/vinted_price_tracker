# %%
import numpy as np
from pyVinted import Vinted
from datetime import datetime
import csv

# %%
vinted = Vinted()

# search(url, number_of_items, page_number)
items = vinted.items.search("https://www.vinted.pt/catalog?search_text=jordan%204%20bred",100,1)
#returns a list of objects: item

# %%
for item in items:
    print(f"Title: {item.title}, Price: {item.price}")

# Convert the list of item prices to a NumPy array, ensuring prices are floats
prices = np.array([float(item.price) for item in items])


# %%
def remove_outliers(prices, m=1):
    data = np.array(prices)
    return data[abs(data - np.mean(data)) < m * np.std(data)]

# %%
def get_average(prices):
    return np.mean(prices)

# %%
def save_to_file(prices):
    fields=[datetime.today().strftime("%B-%D-%Y"),np.around(get_average(prices),2)]
    with open('prices.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(fields)

# %%
save_to_file(remove_outliers(prices))


