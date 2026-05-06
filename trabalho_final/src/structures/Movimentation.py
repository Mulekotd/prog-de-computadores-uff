import json


class Movimentation:
    def __init__(self, uid: str, sender: str, recipient: str, amount: str, datetime: str, transaction_type: str, tags: str):
        self.uid: int = int(uid)
        self.sender: str = sender
        self.recipient: str = recipient
        self.amount: float = float(amount)
        self.datetime: str = datetime
        self.transaction_type: str = transaction_type
        self.tags: list[str] = json.loads(tags)
    
    def update(self, sender: str = None, recipient: str = None, amount: str = None, datetime: str = None, transaction_type: str = None, tags: str = None):
        self.sender: str = sender if sender is not None else self.sender
        self.recipient: str = recipient if recipient is not None else self.recipient
        self.amount: float = float(amount) if amount is not None else self.amount
        self.datetime: str = datetime if datetime is not None else self.datetime
        self.transaction_type: str = transaction_type if transaction_type is not None else self.transaction_type
        self.tags: list[str] = json.loads(tags) if tags is not None else self.tags        

    def write_content(self) -> str:
        return (
            f"TRANSACTION UID: {self.uid}\n"
            f"TYPE: {self.transaction_type}\n"
            f"DATETIME: {self.datetime}\n"
            f"SENDER: {self.sender}\n"
            f"RECIPIENT: {self.recipient}\n"
            f"AMOUNT: {self.amount}\n"
            f"TAGS: {self.tags}\n"
        )

    def get_uid(self) -> int:
        return self.uid
