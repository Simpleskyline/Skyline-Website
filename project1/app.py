#bring a toolkit that helps in building websites and APIs
from flask import Flask, render_template, jsonify

#variable app that represents the whole website
app = Flask(__name__)

#python list containing job dictionaries
JOBS = [
    {
        'id': 1,
        'title': 'Market Analyst',
        'location': 'Nairobi, Kenya',
        'salary': '$5,000'
    },
    {
    'id': 2,
    'title': 'Sales Manager',
    'location': 'Nairobi, Kenya',
    'salary': '$2,000'
    }
   ]

#whenever you open the homepage /, run the function and display the word
@app.route('/')
def hello_world():
    return render_template('index.html',
                           jobs=JOBS)

@app.route('/api/jobs')
def list_jobs():
    return jsonify(JOBS)

#start the web server
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)