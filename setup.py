from dash import Dash, html

app = Dash(__name__)

# Define your layout
app.layout = html.Div("Hello Dash!")

# Run the app
if __name__ == "__main__":
    # Use the server attribute to configure the server
    app.server.run(debug=False, port=int(os.environ.get("PORT", 8080)))
