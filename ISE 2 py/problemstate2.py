import pandas as pd


# highest-paid employee
def highest_paid_employee(df):
    highest = df.loc[df["Salary"].idxmax()]
    return highest


 # department-wise average salary
def department_average_salary(df):
    return df.groupby("Department")["Salary"].mean().sort_values(ascending=False)


# rank employees by salary
def salary_ranking(df):
    df = df.copy()
    df["Salary Rank"] = df["Salary"].rank(
        method="dense",
        ascending=False
    ).astype(int)

    return df.sort_values("Salary Rank")


# Employee data
data = {
    "Employee": [
        "Raj","Amit","Parth"
    ],
    "Department": [
        "IT", "HR","Manager"
    ],
    "Salary": [
        60000, 50000, 80000 
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

print("EMPLOYEE DATA ")
print(df)

highest = highest_paid_employee(df)

print("\nHIGHEST PAID EMPLOYEE ")
print("Employee   :", highest["Employee"])
print("Department :", highest["Department"])
print("Salary     :", highest["Salary"])



avg_salary = department_average_salary(df)

print("\nDEPARTMENT-WISE AVERAGE SALARY ")
print(avg_salary)


# Salary Ranking
ranking = salary_ranking(df)

print("\nSALARY RANKING")
print(ranking)
