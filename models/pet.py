class Pet:
    def __init__(self, pets_name, date_of_birth, pet_type, contact_number, treatment_notes, id = None):
        self.pets_name = pets_name
        self.date_of_birth = date_of_birth
        self.pet_type = pet_type
        self.contact_number = contact_number
        self.treatment_notes = treatment_notes
        self.id = id

    def name_change(self):
        self.pets_name = 'Jasper'