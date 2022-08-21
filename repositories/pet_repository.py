from models.pet import Pet
from db.run_sql import run_sql




def select_all():  
    pets = []  

    sql = "SELECT * FROM pets"
    results = run_sql(sql)

    for row in results:
        pet = Pet(row['pets_name'], row['date_of_birth'], row['pet_type'], row['contact_number'], ['treatment_notes'], row['id'] )
        pets.append(pet)
    return pets