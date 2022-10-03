"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, salary, pay, contract_len, comm, bonus, comm_contract, comm_contract_len):
        self.name = name
        self.salary = salary
        self.pay = pay
        self.contract_len = contract_len
        self.comm = comm
        self.bonus = bonus
        self.comm_contract = comm_contract
        self.comm_contract_len = comm_contract_len

    def get_pay(self):
        total_pay = 0
        if self.salary:
            total_pay += self.pay
        else:
            total_pay += self.pay * self.contract_len

        if self.comm:
            total_pay += self.bonus
            total_pay += self.comm_contract * self.comm_contract_len
        return total_pay

    def __str__(self):
        full_str = ''
        pay_str = ''
        comm_str = ''

        pay_type = ''
        pay = ''
        contract_length = ''
        bonus = ''
        comm_contract = ''
        comm_contract_len = ''
        #print(self.get_pay())
        total_pay = str(self.get_pay())

        pay = str(self.pay)
        if self.salary:
            pay_type = 'monthly salary'
            pay_str = pay_type + ' of ' + pay
        else:
            pay_type = 'contract'
            contract_length = str(self.contract_len)
            pay_str = pay_type + ' of ' + contract_length + ' hours at ' + pay + '/hour'
        
        if self.comm:
            comm_str = ' and receives a '
            if self.bonus > 0:
                bonus = str(self.bonus) 
                comm_str += 'bonus commission of ' + bonus
            elif self.comm_contract > 0:
                comm_contract = str(self.comm_contract)
                comm_contract_len = str(self.comm_contract_len)
                comm_str += 'commission for ' + comm_contract_len + ' contract(s) at ' + comm_contract + '/contract'
        full_str = self.name + ' works on a ' + pay_str + comm_str + '.  Their total pay is ' + total_pay + '.'
        #print(full_str)
        return full_str




# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', True, 4000, 0, False, 0, 0, 0)
#billie.__str__()

#def __init__(self, name, salary, pay, contract_len, comm, bonus, comm_contract, comm_contract_len):

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', False, 25, 100, False, 0, 0, 0)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', True, 3000, 0, True, 0, 200, 4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', False, 25, 150, True, 0 , 220, 3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', True, 2000, 0, True, 1500, 0, 0)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', False, 30, 120, True, 600, 0, 0)

'''
print(str(billie))
print(str(charlie))
print(str(renee))
print(str(jan))
print(str(robbie))
print(str(ariel))
'''