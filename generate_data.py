import pandas as pd
import numpy as np

# Set fixed random seed
np.random.seed(2026)

n_rows = 1000

order_ids = [f"DUKA-{1000 + i}" for i in range(n_rows)]
start_date = pd.Timestamp("2026-01-01")
end_date = pd.Timestamp("2026-06-30")
random_days = np.random.randint(0, (end_date - start_date).days + 1, size=n_rows)
order_dates = [start_date + pd.Timedelta(days=int(d)) for d in random_days]

branches = ["Nairobi Central", "Mombasa", "Kisumu", "Nakuru", "Eldoret"]
branch_weights = [0.35, 0.25, 0.15, 0.15, 0.10]
assigned_branches = np.random.choice(branches, size=n_rows, p=branch_weights)

channels = ["In-store", "Online"]
assigned_channels = np.random.choice(channels, size=n_rows, p=[0.6, 0.4])

products = {
    "Smart TV 55\"": 65000,
    "Laptop Core i5": 58000,
    "Smartphone 128GB": 24000,
    "Microwave Oven": 14500,
    "Bluetooth Speaker": 6500,
    "Electric Kettle": 3200
}

product_names = list(products.keys())
product_weights = [0.15, 0.20, 0.30, 0.15, 0.10, 0.10]
assigned_products = np.random.choice(product_names, size=n_rows, p=product_weights)

unit_prices = [products[p] for p in assigned_products]
quantities = np.random.choice([1, 2, 3, 4], size=n_rows, p=[0.70, 0.20, 0.07, 0.03])

df = pd.DataFrame({
    "order_id": order_ids,
    "order_date": order_dates,
    "branch": assigned_branches,
    "channel": assigned_channels,
    "product": assigned_products,
    "unit_price": unit_prices,
    "quantity": quantities
})

df.to_csv("duka_sales.csv", index=False)
print("duka_sales.csv generated successfully with 1,000 orders (seed 2026).")
