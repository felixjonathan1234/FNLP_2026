import re

def extract_budget(text):
    nums = re.findall(r'\d+', text)
    return int(nums[0]) if nums else None


def extract_brand(text):
    brands = [
        "apple", "samsung", "google", "oneplus", "nothing", "poco", "motorola", "moto",
        "vivo", "xiaomi", "redmi", "realme", "hp", "dell", "lenovo", "asus", "acer",
        "lg", "msi", "boat", "sony", "jbl", "bose", "sennheiser", "skullcandy", "jabra",
        "marshall", "garmin", "fitbit", "audio-technica"
    ]
    for brand in brands:
        if brand in text:
            return brand
    return None


def extract_category(text):
    categories = ["headphones", "laptop", "phone", "tablet", "earbuds", "speaker", "smartwatch", "desktop"]
    for cat in categories:
        if cat in text:
            return cat
    return None


def extract_features(text):
    keywords = ["gaming", "camera", "battery", "performance", "bass", "noise"]
    found = []
    for word in keywords:
        if word in text:
            found.append(word)
    return found
    