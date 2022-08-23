from flask import Flask, render_template
from flask import Blueprint
import repositories.pet_repository as pet_repository
import repositories.vet_repository as vet_repository

pet_blueprint = Blueprint("pet", __name__)

@pet_blueprint.route("/pet")
def pet_list():
    pets = pet_repository.select_all()
    vets = vet_repository.select_all()
    return render_template("pet_list.html", pet_guest = pets, vet_staff = vets)


@pet_blueprint.route("/vet")
def vet_list():
    pets = pet_repository.select_all()
    vets = vet_repository.select_all()
    return render_template("vet_list.html", vet_staff = vets, pet_guest = pets)

@pet_blueprint.route("/add_new_pet")
def add_new_pet():
    pets = pet_repository.select_all()
    vets = vet_repository.select_all()
    return render_template("add_new_pet.html", vet_staff = vets, pet_guest = pets)

@pet_blueprint.route("/add_new_vet")
def add_new_vet():
    pets = pet_repository.select_all()
    vets = vet_repository.select_all()
    return render_template("add_new_vet.html", vet_staff = vets, pet_guest = pets)
