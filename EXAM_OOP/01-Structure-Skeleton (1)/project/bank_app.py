from project.loans.student_loan import StudentLoan
from project.loans.mortgage_loan import MortgageLoan
from project.clients.student import Student
from project.clients.adult import Adult


class BankApp:
    VALID_TYPE_LOANS = ["StudentLoan", "MortgageLoan"]
    VALID_TYPE_CLIENTS = ["Student", "Adult"]

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loans = []
        self.clients = []

    def add_loan(self, loan_type: str):
        if loan_type not in self.VALID_TYPE_LOANS:
            raise Exception("Invalid loan type!")

        current_loan = None
        if loan_type == "StudentLoan":
            current_loan = StudentLoan()
        if loan_type == "MortgageLoan":
            current_loan = MortgageLoan()

        self.loans.append(current_loan)
        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        if client_type not in self.VALID_TYPE_CLIENTS:
            raise Exception("Invalid client type!")

        if self.capacity <= 0:
            return "Not enough bank capacity."
        self.capacity -= 1

        current_client = None
        if client_type == "Student":
            current_client = Student(client_name, client_id, income)
        if client_type == "Adult":
            current_client = Adult(client_name, client_id, income)

        self.clients.append(current_client)
        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str):
        current_client = None
        for client in self.clients:
            if client.client_id == client_id:
                current_client = client

        if current_client.__class__.__name__ == "Student" and not loan_type == "StudentLoan":
            raise Exception("Inappropriate loan type!")

        if current_client.__class__.__name__ == "Adult" and not loan_type == "MortgageLoan":
            raise Exception("Inappropriate loan type!")

        current_loan = [x for x in self.loans if x.__class__.__name__ == loan_type][0]
        current_client.loans.append(current_loan)
        self.loans.remove(current_loan)
        return f"Successfully granted {loan_type} to {current_client.name} with ID {client_id}."

    def remove_client(self, client_id: str):
        current_client = None

        for client in self.clients:
            if client.client_id == client_id:
                current_client = client

        if not current_client:
            raise Exception("No such client!")

        if len(current_client.loans) > 0:
            raise Exception("The client has loans! Removal is impossible!")

        self.clients.remove(current_client)
        return f"Successfully removed {current_client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str):
        all_loans_by_type = []
        for loan in self.loans:
            if loan.__class__.__name__ == loan_type:
                all_loans_by_type.append(loan)

        for l in all_loans_by_type:
            l.increase_interest_rate()

        return f"Successfully changed {len(all_loans_by_type)} loans."

    def increase_clients_interest(self, min_rate: float):
        all_clients_by_rate = []
        for client in self.clients:
            if client.interest < min_rate:
                all_clients_by_rate.append(client)

        for c in all_clients_by_rate:
            c.increase_clients_interest()

        return f"Number of clients affected: {len(all_clients_by_rate)}."

    def get_statistics(self):
        total_clients_count = len(self.clients)
        total_clients_income = 0
        loans_count_granted_to_clients = 0
        granted_sum = 0
        sum_interest_rate = 0
        for client in self.clients:
            total_clients_income += client.income
            loans_count_granted_to_clients += len(client.loans)
            sum_interest_rate += client.interest
            for loan in client.loans:
                granted_sum += loan.amount

        not_granted_sum = 0
        loans_count_not_granted = len(self.loans)
        for loan in self.loans:
            not_granted_sum += loan.amount

        try:
            avg_client_interest_rate = sum_interest_rate / len(self.clients)

        except ZeroDivisionError:
            avg_client_interest_rate = 0.00

        return (f"Active Clients: {total_clients_count}\n"
                f"Total Income: {total_clients_income:.2f}\n"
                f"Granted Loans: {loans_count_granted_to_clients}, Total Sum: {granted_sum:.2f}\n"
                f"Available Loans: {loans_count_not_granted}, Total Sum: {not_granted_sum:.2f}\n"
                f"Average Client Interest Rate: {avg_client_interest_rate:.2f}")
