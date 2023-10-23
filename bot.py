from flask import Flask, render_template, request, jsonify
import json
import random

app = Flask(__name)

# Load movie data from JSON
with open('movies.json', 'r') as file:
    movie_data = json.load(file)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend_movie():
    user_message = request.form['user_message'].lower()
    movies = movie_data['movies']

    # Simple recommendation logic (random movie)
    recommended_movie = random.choice(movies)

    return jsonify({'message': f'I recommend "{recommended_movie["title"]}"'})

if __name__ == '__main__':
    app.run(debug=True)
