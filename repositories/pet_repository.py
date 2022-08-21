from models.pet import Pet
from db.run_sql import run_sql


def select_all():  
    pets = []  

    sql = "SELECT * FROM pets"
    pet_results = run_sql(sql)

    for row in pet_results:
        pet = Pet(row['pets_name'], row['date_of_birth'], row['pet_type'], row['contact_number'], ['treatment_notes'], row['id'] )
        pets.append(pet)
    return pets

# This save function will store a object from the pet class,
# and store it in the vet_management database
def save(pet):
    sql = "INSERT INTO pets (pets_name, date_of_birth, pet_type, contact_number, treatment_notes) VALUES (%s, %s, %s, %s, %s) RETURNING *"
    values = [pet.pets_name, pet.date_of_birth, pet.pet_type, pet.contact_number, pet.treatment_notes]
    results = run_sql(sql, values)
    id = results[0]['id']           
    pet.id = id                    
    return pet           

def select(id):
    pet = None
    sql = "SELECT * FROM pets WHERE id = %s"  
    values = [id] 
    results = run_sql(sql, values)

    if results:
        result = results[0]
        pet = Pet(result['pets_name'], result['date_of_birth'], result['pet_type'], result['contact_number'], result['treatment_notes'], result['id'] )
    return pet     

def delete_all():
    sql = "DELETE FROM pets" 
    run_sql(sql)

def delete(id):
    sql = "DELETE  FROM pets WHERE id = %s" 
    values = [id]
    run_sql(sql, values)

