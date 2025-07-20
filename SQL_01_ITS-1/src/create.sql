CREATE TABLE patients (
	patient_id SERIAL PRIMARY KEY,
	"name" VARCHAR(100),
	age INTEGER,
	gender VARCHAR(10),
	"condition" VARCHAR(100)
);

COMMENT ON COLUMN patients.patient_id IS 'Первичный ключ (Primary Key)';
COMMENT ON COLUMN patients."name" IS 'Имя пациента';
COMMENT ON COLUMN patients.age IS 'Возраст пациента';
COMMENT ON COLUMN patients.gender IS 'Пол пациента (Male/Female)';
COMMENT ON COLUMN patients."condition" IS 'Основное заболевание пациента';


CREATE TABLE trials (
    trial_id SERIAL PRIMARY KEY,
    trial_name VARCHAR(100),
    "start_date" DATE,
    end_date DATE
);

COMMENT ON COLUMN trials.trial_id IS 'Первичный ключ (Primary Key)';
COMMENT ON COLUMN trials.trial_name IS 'Название исследования';
COMMENT ON COLUMN trials.start_date IS 'Дата начала исследования';
COMMENT ON COLUMN trials.end_date IS 'Дата окончания исследования';


CREATE TABLE measurements (
    measurement_id SERIAL PRIMARY KEY,
    patient_id INTEGER,
    trial_id INTEGER,
    measurement_date DATE,
    drug VARCHAR(100),
    condition_score INTEGER,
    FOREIGN KEY (patient_id) REFERENCES patients (patient_id),
    FOREIGN KEY (trial_id) REFERENCES trials (trial_id)
);

COMMENT ON COLUMN measurements.measurement_id IS 'Первичный ключ (Primary Key)';
COMMENT ON COLUMN measurements.patient_id IS 'Внешний ключ (Foreign Key), ссылается на patients.patient_id';
COMMENT ON COLUMN measurements.trial_id IS 'Внешний ключ (Foreign Key), ссылается на trials.trial_id';
COMMENT ON COLUMN measurements.measurement_date IS 'Дата проведения измерения';
COMMENT ON COLUMN measurements.drug IS 'Название препарата (например, «Плацебо» или «Аспирин»)';
COMMENT ON COLUMN measurements.condition_score IS 'Оценка самочувствия пациента по 100-бальной шкале';