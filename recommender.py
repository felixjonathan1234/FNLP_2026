def recommend_products(df, category, budget, features):
    results = df.copy()

    if category:
        results = results[results["category"] == category]

    if budget:
        results = results[results["price"] <= budget]

    if features:
        results = results[
            results["features"].apply(
                lambda x: any(f in x for f in features)
            )
        ]

    return results