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