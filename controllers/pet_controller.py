from flask import Flask, render_template, request, redirect
from flask import Blueprint
import repositories.pet_repository as pet_repository
import repositories.vet_repository as vet_repository
from models.pet import Pet 

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



# @tasks_blueprint.route("/tasks",  methods=['POST'])
# def create_task():
#     description = request.form['description']
#     user_id     = request.form['user_id']
#     duration    = request.form['duration']
#     completed   = request.form['completed']
#     user        = user_repository.select(user_id)
#     task        = Task(description, user, duration, completed)
#     task_repository.save(task)
#     return redirect('/tasks')