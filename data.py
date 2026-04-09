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
    add("Apple iPhone SE (3rd Gen)", "phone", 43900, "compact affordable performance")
    add("Apple iPhone 11", "phone", 37999, "camera reliable")
    add("Apple iPhone 12", "phone", 49999, "camera performance")
    add("Apple iPhone 13 mini", "phone", 59900, "compact performance camera")
    add("Apple iPhone 13", "phone", 52999, "camera performance")
    add("Apple iPhone 14", "phone", 69900, "camera battery performance")
    add("Apple iPhone 14 Plus", "phone", 79900, "large battery camera")
    add("Apple iPhone 14 Pro", "phone", 119900, "camera performance display")
    add("Apple iPhone 14 Pro Max", "phone", 127999, "camera battery display heavy")
    add("Apple iPhone 15", "phone", 79900, "camera performance usb-c")
    add("Apple iPhone 15 Plus", "phone", 89900, "large battery camera usb-c")
    add("Apple iPhone 15 Pro", "phone", 134900, "camera gaming performance battery")
    add("Apple iPhone 15 Pro Max", "phone", 159900, "camera gaming battery flagship")
    add("Google Pixel 7a", "phone", 43999, "camera performance AI")
    add("Google Pixel 8", "phone", 75999, "camera AI compact")
    add("Google Pixel 8 Pro", "phone", 106999, "camera AI display")
    add("OnePlus 11R", "phone", 39999, "gaming performance battery fast charging")
    add("OnePlus 12", "phone", 64999, "performance camera battery flagship")
    add("Nothing Phone (2)", "phone", 44999, "camera performance design")
    add("Samsung Galaxy S23 FE", "phone", 59999, "camera performance student")
    add("Samsung Galaxy S23", "phone", 74999, "compact camera flagship")
    add("Samsung Galaxy S23 Ultra", "phone", 124999, "camera gaming performance battery flagship")
    add("Samsung Galaxy S24", "phone", 79999, "AI compact flagship")
    add("Samsung Galaxy S24 Ultra", "phone", 129999, "AI camera performance flagship")
    add("Samsung Galaxy Z Flip 5", "phone", 99999, "foldable compact stylish")
    add("Samsung Galaxy Z Fold 5", "phone", 154999, "foldable productivity premium")
    add("Poco X5 Pro", "phone", 22999, "gaming performance")
    add("Motorola Edge 40", "phone", 29999, "camera performance slim design")
    add("Vivo V27", "phone", 32999, "camera selfies design")
    add("Xiaomi 13 Pro", "phone", 79999, "camera gaming performance leica")
    add("Xiaomi 14", "phone", 69999, "camera compact performance leica")

    # ------------------
    # LAPTOPS
    # ------------------
    add("HP Pavilion Gaming", "laptop", 55000, "gaming high performance")
    add("Dell Inspiron 15", "laptop", 60000, "office business")
    add("Lenovo IdeaPad Gaming 3", "laptop", 65000, "gaming performance")
    add("Apple MacBook Air M1", "laptop", 82900, "performance battery office travel")
    add("Apple MacBook Air M2 13-inch", "laptop", 104900, "performance design lightweight battery")
    add("Apple MacBook Air M2 15-inch", "laptop", 124900, "large display performance battery")
    add("Apple MacBook Air M3 13-inch", "laptop", 114900, "performance AI modern battery")
    add("Apple MacBook Air M3 15-inch", "laptop", 134900, "large AI performance battery")
    add("Apple MacBook Pro M3 14-inch", "laptop", 169900, "gaming camera battery performance creative")
    add("Apple MacBook Pro M3 Pro 14-inch", "laptop", 199900, "creative professional heavy performance")
    add("Apple MacBook Pro M3 Pro 16-inch", "laptop", 249900, "creative large heavy performance")
    add("Apple MacBook Pro M3 Max 16-inch", "laptop", 319900, "flagship power heavy creative modeling")
    add("Asus ROG Strix G15", "laptop", 95000, "gaming performance esports rgb")
    add("Asus TUF Gaming F15", "laptop", 58990, "gaming battery durable")
    add("Acer Nitro 5", "laptop", 63000, "gaming performance")
    add("Lenovo ThinkPad E14", "laptop", 69000, "office business battery programming")
    add("Lenovo ThinkPad X1 Carbon", "laptop", 145000, "premium office programming portable")
    add("Dell XPS 13", "laptop", 115000, "performance office slim premium")
    add("Dell XPS 15", "laptop", 185000, "creative performance premium")
    add("MSI Katana GF66", "laptop", 74000, "gaming performance fast display")
    add("HP Victus 16", "laptop", 64500, "gaming office student")
    add("HP Omen 16", "laptop", 125000, "gaming heavy performance")
    add("Acer Swift 3", "laptop", 54000, "battery office slim portable")
    add("LG Gram 16", "laptop", 85000, "lightweight big display battery")

    # ------------------
    # HEADPHONES & AUDIO
    # ------------------
    add("Boat Rockerz 450", "headphones", 1500, "bass wireless")
    add("Sony WH-CH520", "headphones", 3000, "lightweight bluetooth")
    add("JBL Tune 510BT", "headphones", 4000, "noise cancellation")
    add("Sony WH-1000XM4", "headphones", 22990, "noise cancellation battery bass premium")
    add("Sony WH-1000XM5", "headphones", 29990, "noise cancellation battery bass premium")
    add("Sony WF-1000XM5", "earbuds", 24990, "compact noise cancellation premium")
    add("Apple AirPods (2nd Gen)", "earbuds", 12900, "wireless compact standard")
    add("Apple AirPods (3rd Gen)", "earbuds", 19900, "wireless spatial audio compact")
    add("Apple AirPods Pro (2nd Gen)", "earbuds", 24900, "noise cancellation wireless transparent")
    add("Apple AirPods Max", "headphones", 59900, "premium noise cancellation design heavy")
    add("Apple HomePod", "speaker", 32900, "smart home audio bass premium")
    add("Apple HomePod mini", "speaker", 9900, "smart home audio compact smart")
    add("Bose QuietComfort 45", "headphones", 28000, "noise cancellation battery comfort premium")
    add("Bose QuietComfort Ultra", "headphones", 35900, "noise cancellation spatial audio premium")
    add("Sennheiser Momentum 4", "headphones", 32000, "battery bass noise cancellation audiophile")
    add("OnePlus Bullets Wireless Z2", "headphones", 1999, "bass battery wireless neckband")
    add("Skullcandy Crusher Evo", "headphones", 11999, "bass wireless battery haptic")
    add("Jabra Elite 45h", "headphones", 7999, "battery bluetooth compact")
    add("Audio-Technica ATH-M50x", "headphones", 14000, "professional bass studio wired")
    add("Marshall Major IV", "headphones", 10999, "battery vintage bass classic")
    add("Samsung Galaxy Buds 2 Pro", "earbuds", 15999, "noise cancellation compact 360 audio")

    # ------------------
    # TABLETS
    # ------------------
    add("Apple iPad 9th Gen", "tablet", 29900, "office student battery")
    add("Apple iPad 10th Gen", "tablet", 39900, "student creative colorful")
    add("Apple iPad mini (6th Gen)", "tablet", 49900, "compact reading portable")
    add("Apple iPad Air 5", "tablet", 54900, "performance office creative")
    add("Apple iPad Air M2 11-inch", "tablet", 59900, "performance student travel")
    add("Apple iPad Air M2 13-inch", "tablet", 79900, "large student media")
    add("Apple iPad Pro 11", "tablet", 79900, "performance gaming creative premium")
    add("Apple iPad Pro 11 M4", "tablet", 99900, "ultra thin performance oled premium")
    add("Apple iPad Pro 13 M4", "tablet", 129900, "ultra thin massive performance oled premium")
    add("Samsung Galaxy Tab A8", "tablet", 14999, "battery student budget")
    add("Samsung Galaxy Tab S9 FE", "tablet", 39999, "student writing media")
    add("Samsung Galaxy Tab S9", "tablet", 72999, "performance gaming office premium")
    add("Samsung Galaxy Tab S9 Ultra", "tablet", 119999, "performance gaming creative massive premium")
    add("Lenovo Tab M10", "tablet", 11000, "battery student budget")
    add("Lenovo Tab P11 Pro", "tablet", 39999, "performance office battery")
    add("Xiaomi Pad 6", "tablet", 26999, "gaming performance office")
    add("OnePlus Pad", "tablet", 37999, "gaming performance premium")

    # ------------------
    # WEARABLES / SMARTWATCHES
    # ------------------
    add("Apple Watch SE (2nd Gen)", "smartwatch", 29900, "fitness tracking affordable ios")
    add("Apple Watch Series 8", "smartwatch", 39900, "fitness health tracking ios")
    add("Apple Watch Series 9", "smartwatch", 41900, "fitness health bright double tap ios")
    add("Apple Watch Ultra", "smartwatch", 89900, "rugged extreme sports long battery ios")
    add("Apple Watch Ultra 2", "smartwatch", 89900, "rugged heavy extreme titanium bright ios")
    add("Samsung Galaxy Watch 4", "smartwatch", 12999, "fitness tracking affordable android")
    add("Samsung Galaxy Watch 6", "smartwatch", 29999, "fitness health sleep android")
    add("Samsung Galaxy Watch 6 Classic", "smartwatch", 36999, "rotating bezel health style android")
    add("Garmin Forerunner 265", "smartwatch", 45000, "running sports fitness gps battery")
    add("Fitbit Charge 6", "smartband", 14999, "fitness sleep small health")

    # ------------------
    # DESKTOPS
    # ------------------
    add("Apple iMac 24-inch M3", "desktop", 134900, "all-in-one minimal family office")
    add("Apple Mac mini M2", "desktop", 59900, "affordable compact office base")
    add("Apple Mac Studio M2 Max", "desktop", 199900, "professional heavy creator powerful")
    add("Apple Mac Pro M2 Ultra", "desktop", 699900, "ultimate power professional maximum workstation")

    return pd.DataFrame(data)