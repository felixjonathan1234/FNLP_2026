import pandas as pd

def load_data():
    data = {
        "name": [
            "Redmi Note 12", "Realme Narzo 50", "Samsung Galaxy M13",
            "HP Pavilion Gaming", "Dell Inspiron 15", "Lenovo IdeaPad Gaming",
            "Boat Rockerz 450", "Sony WH-CH520", "JBL Tune 510BT"
        ],
        "category": [
            "phone", "phone", "phone",
            "laptop", "laptop", "laptop",
            "headphones", "headphones", "headphones"
        ],
        "price": [
            12000, 14000, 13000,
            55000, 60000, 65000,
            1500, 3000, 4000
        ],
        "features": [
            "camera battery", "gaming performance", "battery",
            "gaming high performance", "office business", "gaming performance",
            "bass wireless", "lightweight bluetooth", "noise cancellation"
        ]
    }

    return pd.DataFrame(data)