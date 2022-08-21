from flask import Flask, render_template
from controllers.pet_controller import pet_blueprint

app = Flask(__name__)
app.register_blueprint(pet_blueprint)


if __name__ == '__main__':
    app.run(debug=True)
