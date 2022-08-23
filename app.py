from flask import Flask, render_template, redirect
from controllers.pet_controller import pet_blueprint

app = Flask(__name__)
app.register_blueprint(pet_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)




