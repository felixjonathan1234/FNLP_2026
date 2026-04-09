def recommend_products(df, category, budget, features, brand=None):
    results = df.copy()

    if category:
        results = results[results["category"] == category]

    if budget:
        results = results[results["price"] <= budget]

    if brand:
        results = results[results["name"].str.lower().str.contains(brand.lower())]

    if features:
        results = results[
            results["features"].apply(
                lambda x: any(f in x for f in features)
            )
        ]

    return results