
from models.vet import Vet
from models.pet import Pet
import repositories.pet_repository as pet_repository
import repositories.vet_repository as vet_repository

pet_repository.delete_all()
vet_repository.delete_all()

# {name: "David Millar", id: None}
vet_1 = Vet('David Miller')
# {name: "David Millar", id: 4}
vet_1_but_with_the_db_id = vet_repository.save(vet_1)

pet_1 = Pet('Jerry', '01/05/2021', 'Cat', '07564227790', 'Needs stitches for open wound', vet_1_but_with_the_db_id)
pet_1_but_with_the_db_id = pet_repository.save(pet_1)
print(pet_1_but_with_the_db_id.__dict__)

# vet_repository.select(vet_1.id)
# pet_repository.select(pet_1.id)

# pet_1.name_change()
# pet_repository.update()

pet_result = pet_repository.select_all()
vet_result = vet_repository.select_all()

for pet in pet_result:
    print(pet.__dict__)

for pet in vet_result:
    print(pet.__dict__)

