

class bank_account:
    def __init__(self,balance, log_file = None):
        self.balance = balance
        self.log_file = log_file
        self._log_transaction('cuenta creada')

    def _log_transaction(self,message):
        if self.log_file:
            with open (self.log_file, 'a') as f:
                f.write(f"{message}\n")


    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            self._log_transaction(f"Deposito de {amount}, nuevo balance: {self.balance}")
        return self.balance

    def withdraw(self,amount):
        if amount >= 0:
            self.balance -= amount
            self._log_transaction(f"Retiro de {amount}, nuevo balance: {self.balance}")
        return  self.balance

    def check_balance(self):
        self._log_transaction(f"el balance es: {self.balance}")
        return self.balance

    def transfer(self,amount):
        if self.balance >= amount:
            self.balance -= amount
            self._log_transaction(f"transaccion hecha, del monto: {amount}, nuevo balance: {self.balance}")
            return self.balance
        else:
            self._log_transaction(f"transaccion no se pudo ejecutar, saldo insuficiente, balance: {self.balance}")
            raise ValueError("no se pudo ejecutar la transferencia, fondos insuficientes")

