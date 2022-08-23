
from models.vet import Vet
from models.pet import Pet
import repositories.pet_repository as pet_repository
import repositories.vet_repository as vet_repository

pet_repository.delete_all()
vet_repository.delete_all()

# {name: "David Millar", id: None}
vet_1 = Vet('David Miller')
vet_1_but_with_the_db_id = vet_repository.save(vet_1)

vet_2 = Vet('Bruce Stuart')
vet_2_but_with_the_db_id = vet_repository.save(vet_2)

vet_3 = Vet('Ross Davies')
vet_3_but_with_the_db_id = vet_repository.save(vet_3)

vet_4 = Vet('Dan Murray')
vet_4_but_with_the_db_id = vet_repository.save(vet_4)




pet_1 = Pet('Jerry', '01/05/2021', 'Cat', '07564227790', 'Needs stitches for open wound', vet_1_but_with_the_db_id)
pet_1_but_with_the_db_id = pet_repository.save(pet_1)
print(pet_1_but_with_the_db_id.__dict__)

pet_2 = Pet('Bobo', '18/06/2022', 'Cat', '07365486633', 'Needs to be neutered ouch!', vet_2_but_with_the_db_id)
pet_2_but_with_the_db_id = pet_repository.save(pet_2)
print(pet_2_but_with_the_db_id.__dict__)

pet_3 = Pet('Thumper', '02/10/2019', 'Rabbit', '07558458450', 'Needs cast for sprained paw', vet_3_but_with_the_db_id)
pet_3_but_with_the_db_id = pet_repository.save(pet_3)
print(pet_3_but_with_the_db_id.__dict__)

pet_4 = Pet('Steve', '15/01/2021', 'Dog', '07543853498', 'Needs shots', vet_4_but_with_the_db_id)
pet_4_but_with_the_db_id = pet_repository.save(pet_4)
print(pet_4_but_with_the_db_id.__dict__)

# vet_repository.select(vet_1.id)
# pet_repository.select(pet_1.id)

# pet_1.name_change()
# pet_repository.update()

pet_result = pet_repository.select_all()
vet_result = vet_repository.select_all()

for pet in pet_result:
    print(pet.__dict__)

for vet in vet_result:
    print(vet.__dict__)

