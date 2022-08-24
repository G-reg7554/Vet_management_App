from models.pet import Pet
from db.run_sql import run_sql
import repositories.vet_repository as vet_repository



def save(pet):
    sql = "INSERT INTO pets (pets_name, date_of_birth, pet_type, contact_number, treatment_notes, vet_id) VALUES (%s, %s, %s, %s, %s, %s) RETURNING *"
    values = [pet.pets_name, pet.date_of_birth, pet.pet_type, pet.contact_number, pet.treatment_notes, pet.vet.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    pet.id = id
    return pet

def select_all():
    pets = []

    sql = "SELECT * FROM pets"
    results = run_sql(sql)

    for row in results:
        vet = vet_repository.select(row['vet_id'])
        pet = Pet(row['pets_name'], row['date_of_birth'], row['pet_type'],row['contact_number'], row['treatment_notes'],vet, row['id'])
        pets.append(pet)
    return pets


    

def select(id):
    pet = None
    sql = "SELECT * FROM pets WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)

    if result:
        result = result[0]
        vet = vet_repository.select(result['vet_id'])
        pet = Pet(result['pets_name'], result['date_of_birth'], result['pet_type'], result['contact_number'], result['treatment_notes'], vet, result['id'])
    return pet


def delete_all():
    sql = "DELETE  FROM pets"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM pets WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(pet):
    sql = "UPDATE tasks SET (pets_name, date_of_birth, pet_type, contact_number, treatment_notes, vet_id) = (%s, %s, %s, %s, %s, %s) WHERE id = %s" # MODIFIED
    values = [pet.pets_name, pet.date_of_birth, pet.pet_type, pet.contact_number, pet.treatment_notes, pet.vet.id] # MODIFIED
    run_sql(sql, values)
