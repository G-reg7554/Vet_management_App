from flask import Flask, render_template
from flask import Blueprint
import repositories.pet_repository as pet_repository
import repositories.vet_repository as vet_repository

pet_blueprint = Blueprint("tasks", __name__)

@pet_blueprint.route("/tasks")
def tasks():
    pets = pet_repository.select_all()
    vets = vet_repository.select_all()
    return render_template("new.html", vet_staff = vets, pet_patient = pets)

