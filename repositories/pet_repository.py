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

def save(pet):
    sql = "INSERT INTO pets (pets_name, date_of_birth, pet_type, contact_number, treatment_notes) VALUES (%s, %s, %s, %s, %s) RETURNING *"
    values = [pet.pets_name, pet.date_of_birth, pet.pet_type, pet.contact_number, pet.treatment_notes]
    results = run_sql(sql, values)
    id = results[0]['id']           
    pet.id = id                    
    return pet                

