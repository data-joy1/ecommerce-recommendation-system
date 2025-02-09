from flask import Flask, jsonify, request
from recommend import recommend_products

app = Flask(__name__)

@app.route('/recommend', methods=['GET'])
def get_recommendations():
    user_id = int(request.args.get('user_id'))
    recommendations = recommend_products(user_id, model)
    return jsonify(recommendations)

if __name__ == '__main__':
    app.run(debug=True)
