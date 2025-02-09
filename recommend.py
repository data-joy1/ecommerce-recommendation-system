def recommend_products(user_id, model, num_recommendations=5):
    user_df = spark.createDataFrame([(user_id,)], ["UserId"])
    recommendations = model.recommendForUserSubset(user_df, num_recommendations)
    return recommendations

# Example usage
print(recommend_products(12345, model))
