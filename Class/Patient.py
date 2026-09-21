class Patient:
    def __init__(self, patient_id, name, age, disease, fee):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.disease = disease
        self.fee = fee
    def display(self):
        print("Patient ID:", self.patient_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Disease:", self.disease)
        print("Consultation Fee:", self.fee)
    def total_bill(self):
        return self.fee
p = Patient(101, "Rony", 20, "Fever", 500)
p.display()
print("Total Bill:", p.total_bill())