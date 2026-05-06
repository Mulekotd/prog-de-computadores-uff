import json


class Client:
    def __init__(self, uid: str, first_name: str, last_name: str, country: str, balance: str, vip_level: str, payment_methods: str):
        self.uid: int = int(uid)
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.country: str = country
        self.balance: float = float(balance)
        self.vip_level: int = int(vip_level)   
        self.payment_methods: list[str] = json.loads(payment_methods) # ["PIX", "CREDIT_CARD", "BTC"]

    def update(self, first_name: str = None, last_name: str = None, country: str = None, balance: str = None, vip_level: str = None, payment_methods: str = None):
        self.first_name: str = first_name if first_name is not None else self.first_name
        self.last_name: str = last_name if last_name is not None else self.last_name
        self.country: str = country if country is not None else self.country
        self.balance: float = float(balance) if balance is not None else self.balance
        self.vip_level: int = int(vip_level) if vip_level is not None else self.vip_level
        self.payment_methods: list[str] = json.loads(payment_methods) if payment_methods is not None else self.payment_methods

    def write_content(self) -> str:
        return (
            f"CLIENT UID: {self.uid}\n"
            f"NAME: {self.first_name} {self.last_name}\n"
            f"COUNTRY: {self.country}\n"
            f"BALANCE: {self.balance}\n"
            f"VIP LEVEL: {self.vip_level}\n"
            f"PAYMENT METHODS: {self.payment_methods}\n"
        )

    def get_uid(self) -> int:
        return self.uid
