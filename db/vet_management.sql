DROP TABLE IF EXISTS pets;
DROP TABLE IF EXISTS vets;

CREATE TABLE vets (
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(255)
);

CREATE TABLE pets (
    id SERIAL PRIMARY KEY,
    pets_name VARCHAR(255),
    date_of_birth VARCHAR(255),
    pet_type VARCHAR(255),
    contact_number VARCHAR(255),
    treatment_notes VARCHAR(255)
);

INSERT INTO pets (pets_name, date_of_birth, pet_type, contact_number, treatment_notes )
VALUES ('Jerry', '01/05/2021', 'Cat', '07760589912', 'Needs stitches for small open wound');

