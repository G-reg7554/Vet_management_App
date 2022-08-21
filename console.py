import pdb
from models.vet import Vet
from models.pet import Pet
import repositories.pet_repository as pet_repository
import repositories.vet_repository as vet_repository


result = pet_repository.select_all()  # ADDED

for task in result:
    print(task.__dict__)

pdb.set_trace()