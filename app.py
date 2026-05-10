from flask import Flask, render_template
from models import db
from routes import routes

# =========================================================
# CREATE FLASK APP
# =========================================================

app = Flask(__name__)

# =========================================================
# CONFIGURATION
# =========================================================

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.secret_key = 'library_secret_key'

# =========================================================
# INITIALIZE DATABASE
# =========================================================

db.init_app(app)

with app.app_context():
    db.create_all()

# =========================================================
# HOME PAGE
# =========================================================

@app.route('/')
def home():
    return render_template("index.html")

# =========================================================
# REGISTER BLUEPRINT
# =========================================================

app.register_blueprint(routes)

# =========================================================
# RUN APPLICATION
# =========================================================

if __name__ == '__main__':

    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )