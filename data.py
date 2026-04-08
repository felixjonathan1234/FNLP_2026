import pandas as pd

def load_data():
    data = {"name": [], "category": [], "price": [], "features": []}

    def add(name, category, price, features):
        data["name"].append(name)
        data["category"].append(category)
        data["price"].append(price)
        data["features"].append(features)

    # ------------------
    # PHONES
    # ------------------
    add("Poco C50", "phone", 6500, "battery")
    add("Moto e13", "phone", 7000, "battery slim")
    add("Realme C30", "phone", 8000, "battery basic")
    add("Samsung Galaxy M04", "phone", 9000, "battery reliable")
    add("Redmi Note 12", "phone", 12000, "camera battery")
    add("Realme Narzo 50", "phone", 14000, "gaming performance")
    add("Samsung Galaxy M13", "phone", 13000, "battery")
    add("Apple iPhone 13", "phone", 52999, "camera performance")
    add("Apple iPhone 15 Pro", "phone", 134900, "camera gaming performance battery")
    add("Google Pixel 7a", "phone", 43999, "camera performance AI")
    add("OnePlus 11R", "phone", 39999, "gaming performance battery fast charging")
    add("Nothing Phone (2)", "phone", 44999, "camera performance design")
    add("Samsung Galaxy S23 Ultra", "phone", 124999, "camera gaming performance battery flagship")
    add("Poco X5 Pro", "phone", 22999, "gaming performance")
    add("Motorola Edge 40", "phone", 29999, "camera performance slim design")
    add("Vivo V27", "phone", 32999, "camera selfies design")
    add("Xiaomi 13 Pro", "phone", 79999, "camera gaming performance leica")

    # ------------------
    # LAPTOPS
    # ------------------
    add("HP Pavilion Gaming", "laptop", 55000, "gaming high performance")
    add("Dell Inspiron 15", "laptop", 60000, "office business")
    add("Lenovo IdeaPad Gaming 3", "laptop", 65000, "gaming performance")
    add("Apple MacBook Air M1", "laptop", 82900, "performance battery office travel")
    add("Apple MacBook Pro M3", "laptop", 169900, "gaming camera battery performance creative")
    add("Asus ROG Strix G15", "laptop", 95000, "gaming performance esports rgb")
    add("Asus TUF Gaming F15", "laptop", 58990, "gaming battery durable")
    add("Acer Nitro 5", "laptop", 63000, "gaming performance")
    add("Lenovo ThinkPad E14", "laptop", 69000, "office business battery programming")
    add("Dell XPS 13", "laptop", 115000, "performance office slim premium")
    add("MSI Katana GF66", "laptop", 74000, "gaming performance fast display")
    add("HP Victus 16", "laptop", 64500, "gaming office student")
    add("Acer Swift 3", "laptop", 54000, "battery office slim portable")

    # ------------------
    # HEADPHONES
    # ------------------
    add("Boat Rockerz 450", "headphones", 1500, "bass wireless")
    add("Sony WH-CH520", "headphones", 3000, "lightweight bluetooth")
    add("JBL Tune 510BT", "headphones", 4000, "noise cancellation")
    add("Sony WH-1000XM5", "headphones", 29990, "noise cancellation battery bass premium")
    add("Apple AirPods Pro (2nd Gen)", "headphones", 24900, "noise cancellation wireless transparent")
    add("Bose QuietComfort 45", "headphones", 28000, "noise cancellation battery comfort premium")
    add("Sennheiser Momentum 4", "headphones", 32000, "battery bass noise cancellation audiophile")
    add("OnePlus Bullets Wireless Z2", "headphones", 1999, "bass battery wireless neckband")
    add("Skullcandy Crusher Evo", "headphones", 11999, "bass wireless battery haptic")
    add("Jabra Elite 45h", "headphones", 7999, "battery bluetooth compact")
    add("Audio-Technica ATH-M50x", "headphones", 14000, "professional bass studio wired")
    add("Marshall Major IV", "headphones", 10999, "battery vintage bass classic")

    # ------------------
    # TABLETS
    # ------------------
    add("Apple iPad 9th Gen", "tablet", 29900, "office student battery")
    add("Apple iPad Air 5", "tablet", 54900, "performance office creative")
    add("Apple iPad Pro 11", "tablet", 79900, "performance gaming creative premium")
    add("Samsung Galaxy Tab A8", "tablet", 14999, "battery student budget")
    add("Samsung Galaxy Tab S9", "tablet", 72999, "performance gaming office premium")
    add("Samsung Galaxy Tab S9 Ultra", "tablet", 119999, "performance gaming creative massive premium")
    add("Lenovo Tab M10", "tablet", 11000, "battery student budget")
    add("Lenovo Tab P11 Pro", "tablet", 39999, "performance office battery")
    add("Xiaomi Pad 6", "tablet", 26999, "gaming performance office")
    add("OnePlus Pad", "tablet", 37999, "gaming performance premium")

    return pd.DataFrame(data)