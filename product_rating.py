products = [
    {"sku": "SKU1", "sales": 120, "return_rate": 0.05, "margin": 0.30},
    {"sku": "SKU2", "sales": 40, "return_rate": 0.20, "margin": 0.45},
    {"sku": "SKU3", "sales": 200, "return_rate": 0.02, "margin": 0.25},
    {"sku": "SKU4", "sales": 75, "return_rate": 0.10, "margin": 0.35},
    {"sku": "SKU5", "sales": 150, "return_rate": 0.08, "margin": 0.28},
    {"sku": "SKU6", "sales": 60, "return_rate": 0.15, "margin": 0.40},
    {"sku": "SKU7", "sales": 300, "return_rate": 0.03, "margin": 0.22},
    {"sku": "SKU8", "sales": 90, "return_rate": 0.12, "margin": 0.33},
    {"sku": "SKU9", "sales": 45, "return_rate": 0.18, "margin": 0.50},
    {"sku": "SKU10", "sales": 210, "return_rate": 0.04, "margin": 0.27},
    {"sku": "SKU11", "sales": 130, "return_rate": 0.06, "margin": 0.31},
    {"sku": "SKU12", "sales": 80, "return_rate": 0.09, "margin": 0.36},
    {"sku": "SKU13", "sales": 170, "return_rate": 0.07, "margin": 0.29},
    {"sku": "SKU14", "sales": 55, "return_rate": 0.14, "margin": 0.42},
    {"sku": "SKU15", "sales": 260, "return_rate": 0.02, "margin": 0.24},
    {"sku": "SKU16", "sales": 110, "return_rate": 0.11, "margin": 0.38},
    {"sku": "SKU17", "sales": 95, "return_rate": 0.13, "margin": 0.34},
    {"sku": "SKU18", "sales": 140, "return_rate": 0.05, "margin": 0.30},
]
for item in products:

    sku = item["sku"]
    sales = item["sales"]
    return_rate = item["return_rate"]
    margin = item["margin"]

    score = int(item["sales"] * item["margin"] - (item["return_rate"] * 100))
    item["score"] = score

    if score >= 50:
        segment = "A"
        item["segment"] = segment

    elif score >= 29 and score <= 49:
        segment = "B"
        item["segment"] = segment

    elif score <= 20:
        segment = "C"
        item["segment"] = segment

sorted_list = sorted(products, key=lambda x: x["score"], reverse=True)
print(sorted_list)