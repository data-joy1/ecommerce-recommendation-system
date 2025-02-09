# ecommerce-recommendation-system
Goal:
Build a product recommendation system using collaborative filtering on large-scale e-commerce data.

⚙️ Tech Stack
PySpark (MLlib) – Machine learning on Big Data
Hadoop HDFS – Distributed storage
Spark SQL – Data querying and processing
Flask API (Optional) – To serve recommendations

🛠️ Setup & Installation
Step 1: Setup Hadoop & Spark
Install Hadoop
Follow the official Hadoop Installation Guide to set up Hadoop.

Install Spark
Follow the Apache Spark Installation Guide to install Apache Spark.

For Windows users, install WSL2 (Ubuntu) for smooth Hadoop/Spark execution.

📝 How to Run
Step 1: Load & Process Data
Run data_preprocessing.py to load and clean the data:
python src/data_preprocessing.py

Step 2: Train Recommendation Model
Train the ALS (Alternating Least Squares) model:
python src/train_model.py

Step 3: Generate Recommendations
To generate product recommendations for a user, run:
python src/recommend.py

Step 4: Deploy as Flask API (Optional)
If you want to deploy the model as a REST API, run:
python src/app.py
Visit http://127.0.0.1:5000/recommend?user_id=12345 to get recommendations for a specific user.

🗄️ Store Data in Hadoop HDFS
To store your dataset in HDFS:
hdfs dfs -mkdir /user/data
hdfs dfs -put data/amazon_reviews.csv /user/data/

To check the uploaded data:
hdfs dfs -ls /user/data/

