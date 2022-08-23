from flask import Flask, render_template
from flask import Blueprint
import repositories.pet_repository as pet_repository
import repositories.vet_repository as vet_repository

pet_blueprint = Blueprint("pet", __name__)

@pet_blueprint.route("/pet")
def pet_list():
    pets = pet_repository.select_all()
    vets = vet_repository.select_all()
    return render_template("pet_list.html", vet_staff = vets, pet_patient = pets)


@pet_blueprint.route("/vet")
def vet_list():
    pets = pet_repository.select_all()
    vets = vet_repository.select_all()
    return render_template("vet_list.html", vet_staff = vets, pet_patient = pets)
