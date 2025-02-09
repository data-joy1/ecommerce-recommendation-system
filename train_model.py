from pyspark.ml.recommendation import ALS
from pyspark.ml.evaluation import RegressionEvaluator

# Train ALS model
als = ALS(userCol="UserId", itemCol="ProductId", ratingCol="Score", coldStartStrategy="drop")
model = als.fit(df)

# Evaluate Model
evaluator = RegressionEvaluator(metricName="rmse", labelCol="Score", predictionCol="prediction")
predictions = model.transform(df)
rmse = evaluator.evaluate(predictions)
print(f"Root Mean Square Error: {rmse}")
