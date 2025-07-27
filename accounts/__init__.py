-- 1. UserProfile (kết nối với Django User)
CREATE TABLE UserProfile (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES auth_user(id) ON DELETE CASCADE,
    phone_number VARCHAR(20),
    id_number VARCHAR(20),
    university VARCHAR(100),
    major VARCHAR(100),
    graduation_year INTEGER,
    birth_date DATE,
    role VARCHAR(50),
    is_manager BOOLEAN DEFAULT FALSE
);

-- 2. MedicalSupply
CREATE TABLE MedicalSupply (
    id SERIAL PRIMARY KEY,
    code VARCHAR(50) UNIQUE,
    name VARCHAR(255),
    quantity INTEGER,
    unit VARCHAR(50),
    expiration_date DATE,
    description TEXT,
    supplier VARCHAR(255),
    threshold INTEGER,
    unit_price DECIMAL(10, 2)
);

-- 3. InventoryTransaction
CREATE TABLE InventoryTransaction (
    id SERIAL PRIMARY KEY,
    supply_id INTEGER REFERENCES MedicalSupply(id) ON DELETE CASCADE,
    transaction_type VARCHAR(50),
    quantity INTEGER,
    note TEXT,
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 4. Patient
CREATE TABLE Patient (
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(255),
    gender VARCHAR(10),
    birth_date DATE,
    address TEXT,
    phone_number VARCHAR(20),
    id_card VARCHAR(20),
    has_insurance BOOLEAN DEFAULT FALSE,
    insurance_code VARCHAR(50),
    symptoms TEXT,
    allergy TEXT,
    medical_history TEXT,
    current_medications TEXT,
    old_test_results TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 5. TreatmentRecord
CREATE TABLE TreatmentRecord (
    id SERIAL PRIMARY KEY,
    patient_id INTEGER REFERENCES Patient(id) ON DELETE CASCADE,
    symptoms TEXT,
    blood_pressure_systolic INTEGER,
    blood_pressure_diastolic INTEGER,
    pulse INTEGER,
    spo2 INTEGER,
    temperature FLOAT,
    current_medications TEXT,
    old_test_results TEXT,
    treatment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 6. TestResult
CREATE TABLE TestResult (
    id SERIAL PRIMARY KEY,
    patient_id INTEGER REFERENCES Patient(id) ON DELETE CASCADE,
    test_type VARCHAR(100),
    result_value FLOAT,
    unit VARCHAR(20),
    ecg_result TEXT,
    ultrasound_result TEXT,
    price DECIMAL(10, 2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 7. Invoice
CREATE TABLE Invoice (
    id SERIAL PRIMARY KEY,
    patient_id INTEGER REFERENCES Patient(id) ON DELETE CASCADE,
    total_amount DECIMAL(10, 2),
    issued_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    details TEXT
);
