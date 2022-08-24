from flask import Flask, render_template, request, redirect
from flask import Blueprint
import repositories.pet_repository as pet_repository
import repositories.vet_repository as vet_repository
from repositories.vet_repository import Vet
from models.pet import Pet 

pet_blueprint = Blueprint("pet", __name__)

@pet_blueprint.route("/pet")
def pet_list():
    pets = pet_repository.select_all()
    vets = vet_repository.select_all()
    return render_template("/pets/pet_list.html", pet_guest = pets, vet_staff = vets)


@pet_blueprint.route("/vet_list")
def vet_list():
    pets = pet_repository.select_all()
    vets = vet_repository.select_all()
    return render_template("vet_list.html", vet_staff = vets, pet_guest = pets)

@pet_blueprint.route("/add_new_pet")
def add_pet():
    pets = pet_repository.select_all()
    vets = vet_repository.select_all()
    return render_template("add_new_pet.html", vet_staff = vets, pet_guest = pets)

@pet_blueprint.route("/add_new_vet")
def add_new_vet():
    pets = pet_repository.select_all()
    vets = vet_repository.select_all()
    return render_template("add_new_vet.html", vet_staff = vets, pet_guest = pets)


@pet_blueprint.route("/add_new_pet", methods=['POST'])
def add_pet_db():
    pets_name = request.form['pets_name']
    pets_dob = request.form['date_of_birth']
    pet_type = request.form['pet_type']
    contact_number = request.form['contact_number']
    treatment_notes = request.form['treatment_notes']
    vet_id = request.form['vet_id']
    vet       = vet_repository.select(vet_id)
    pet_class = Pet(pets_name, pets_dob, pet_type, contact_number, treatment_notes, vet)
    pet_repository.save(pet_class)
    return redirect('/pet')



@pet_blueprint.route('/add_new_vet', methods=['POST'])
def add_vet_db():
    full_name = request.form['full_name']
    vet_class = Vet(full_name)
    vet_repository.save(vet_class)
    return redirect("/vet_list")


@pet_blueprint.route('/delete_pet')
def dump_pet():
    pet = pet_repository.select_all()
    return render_template("/pets/pet_list.html", pets = pet)


@pet_blueprint.route('/pet/<id>/delete', methods=['POST'])
def delete_pet(id):
    pet_repository.delete(id)
    return redirect('/pet')









# @pet_blueprint.route("/pet<id>", methods=['POST'])
# def add_pet_update():
#     pets_name = request.form['pets_name']
#     pets_dob = request.form['date_of_birth']
#     pet_type = request.form['pet_type']
#     contact_number = request.form['contact_number']
#     treatment_notes = request.form['treatment_notes']
#     vet_id = request.form['vet_id']
#     vet       = vet_repository.select(vet_id)
#     pet_class = Pet(pets_name, pets_dob, pet_type, contact_number, treatment_notes, vet)
#     pet_repository.update(pet_class)
#     return redirect('/pet')








