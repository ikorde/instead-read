from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Define some Python logic
    topics = ['History', 'Economics', 'Religions', 'Politics', 'Art']

    # Render an HTML template and pass data to it
    return render_template('index.html', topics=topics)

if __name__ == '__main__':
    app.run(debug=True)
