def first_N_primes(N):
  x=2
  count_primes=0
  primes=[]
  while count_primes<N:
    for i in range(2,x):
      if x%i==0:
        break
    else:
      primes.append(x)
      count_primes+=1
    x+=1
  return primes


class Employees:
  def __call__(self,name, employee_id, position, salary, department):
    self.name=name
    self.employee_id=employee_id
    self.position=position
    self.salary=salary
    self.department=department
  
  def display_details(self):
    print(f"Name: {self.name}")
    print(f"Employee ID: {self.employee_id}")
    print(f"Position: {self.position}")
    print(f"Salary: {self.salary}")
    print(f"Department: {self.department}")

  def calculate_annual_salary(self):
    return self.salary*12
