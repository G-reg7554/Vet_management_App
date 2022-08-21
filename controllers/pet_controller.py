from flask import Flask, render_template
from flask import Blueprint

pet_blueprint = Blueprint("pet", __name__)