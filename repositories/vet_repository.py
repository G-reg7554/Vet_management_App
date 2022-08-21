from models.vet import Vet
from db.run_sql import run_sql


def select_all():  
    vets = []  

    sql = "SELECT * FROM vets"
    vet_results = run_sql(sql)

    for row in vet_results:
        vet = Vet(row['full_name'], row['id'] )
        vets.append(vet)
    return vets

def save(vet):
    sql = "INSERT INTO vets (full_name) VALUES (%s) RETURNING *"
    values = [vet.full_name]
    results = run_sql(sql, values)
    id = results[0]['id']           
    vet.id = id                    
    return vet  

# def select(id):
#     vet = None
#     sql = "SELECT * FROM vets WHERE id = %s"  
#     values = [id] 
#     results = run_sql(sql, values)

#     if results:
#         result = results[0]
#         vet = Vet(result['full_name'], result['id'])
#     return vet

def delete_all():
    sql = "DELETE  FROM vets" 
    run_sql(sql)

# def delete(id):
#     sql = "DELETE  FROM vets WHERE id = %s" 
#     values = [id]
#     run_sql(sql, values)

# def update(vet):
#     sql = "UPDATE pets SET (full_name) = (%s) WHERE id = %s"
#     values = [vet.full_name, vet,id]
#     run_sql(sql, values)