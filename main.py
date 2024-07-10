from flask import Flask
from UI import UI

# Create Flask application here, which allows cross-access between modules
# Initialize the app, locate the folders to serve templates and static content.
app = Flask(__name__,
            template_folder='UI/templates',
            static_folder='UI/static')

# Launch UI Layer
UI.create_UI(app)

if __name__ == '__main__':
    app.run(debug=True)