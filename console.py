import pdb
from models.vet import Vet
from models.pet import Pet
import repositories.pet_repository as pet_repository
import repositories.vet_repository as vet_repository


pet_result = pet_repository.select_all()
vet_result = vet_repository.select_all()

pet_1 = Pet("Jerry", "01/05/2021", "Cat", "'07760589912'", "Needs stitches for open wound")
pet_repository.save(pet_1)

for task in pet_result:
    print(task.__dict__)

for task in vet_result:
    print(task.__dict__)

pdb.set_trace()