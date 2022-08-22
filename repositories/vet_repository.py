
from db.run_sql import run_sql
from models.vet import Vet

def save(vet):
    # the sql that we want to send to our db this sql returns just the id 
    sql = "INSERT INTO vets (full_name) VALUES (%s) RETURNING id"
    #  takes the information from the instance of our vet class that we need to save to the database, in this case just the name
    values = [vet.full_name]
    # runs the sql with the substituited infomration from our instance of our vet class and returns the id
    results = run_sql(sql, values)
    # sets the id of the vet as assigned by the database
    vet.id = results[0]['id']                            
    return vet  


def select_all():  
    vets = []  
    sql = "SELECT * FROM vets"
    vet_results = run_sql(sql)

    for row in vet_results:
        vet = Vet(row['full_name'], row['id'] )
        vets.append(vet)
    return vets


def select(id):
    vet = None
    sql = "SELECT * FROM vets WHERE id = %s"  
    values = [id] 
    results = run_sql(sql, values)

    if results:
        result = results[0]
        vet = Vet(result['full_name'], result['id'])
        return vet


def delete_all():
    sql = "DELETE  FROM vets" 
    run_sql(sql)

def delete(id):
    sql = "DELETE  FROM vets WHERE id = %s" 
    values = [id]
    run_sql(sql, values) 


# def update(vet):
#     sql = "UPDATE pets SET (full_name) = (%s) WHERE id = %s"
#     values = [vet.full_name, vet,id]
#     run_sql(sql, values) 