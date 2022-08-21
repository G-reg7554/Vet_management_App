import pdb
from models.vet import Vet
from models.pet import Pet
import repositories.pet_repository as pet_repository
import repositories.vet_repository as vet_repository

pet_repository.delete_all()
vet_repository.delete_all()

pet_result = pet_repository.select_all()
vet_result = vet_repository.select_all()




vet_1 = Vet("David Miller")
vet_repository.save(vet_1)

pet_1 = Pet("Jerry", "01/05/2021", "Cat", "'07760589912'", "Needs stitches for open wound")
pet_repository.save(pet_1)

# pet_repository.delete(pet_1.id)
# vet_repository.delete(vet_1.id)

# vet_repository.select(vet_1.id)
# pet_repository.select(pet_1.id)



for task in pet_result:
    print(task.__dict__)

for task in vet_result:
    print(task.__dict__)

pdb.set_trace()