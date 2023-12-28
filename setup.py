from flask import Flask, render_template
from dash import html

app = Flask(__name__)

@app.route('/')
def home():
    return html.Div("Hello Flask!")

if __name__ == '__main__':
    app.run(debug=True)
