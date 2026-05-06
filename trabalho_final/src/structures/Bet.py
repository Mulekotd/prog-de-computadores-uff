import json

class Bet:
    def __init__(self, uid: str, client_id: str, game_id: str, amount: str, outcome: str, payout: str, datetime: str, odds_breakdown: str):
        self.uid: int = int(uid)
        self.client_id: int = int(client_id)
        self.game_id: int = int(game_id)
        self.amount: float = float(amount)
        self.outcome: str = outcome
        self.payout: float = float(payout)
        self.datetime: str = datetime
        self.odds_breakdown: list[float] = json.loads(odds_breakdown)
    
    def update(self, client_id: str = None, game_id: str = None, amount: str = None, outcome: str = None, payout: str = None, datetime: str = None, odds_breakdown: str = None) -> None:
        self.client_id: int = int(client_id) if client_id is not None else self.client_id
        self.game_id: int = int(game_id) if game_id is not None else self.game_id
        self.amount: float = float(amount) if amount is not None else self.amount
        self.outcome: str = outcome if outcome is not None else self.outcome
        self.payout: float = float(payout) if payout is not None else self.payout
        self.datetime: str = datetime if datetime is not None else self.datetime
        self.odds_breakdown: list[float] = json.loads(odds_breakdown) if odds_breakdown is not None else self.odds_breakdown

    def write_content(self) -> str:
        return (
            f"BET UID: {self.uid}\n"
            f"CLIENT: {self.client_id}\n"
            f"GAME: {self.game_id}\n"
            f"AMOUNT: {self.amount}\n"
            f"OUTCOME: {self.outcome}\n"
            f"PAYOUT: {self.payout}\n"
            f"DATETIME: {self.datetime}\n"
            f"ODDS BREAKDOWN: {self.odds_breakdown}\n"
        )

    def get_uid(self) -> int:
        return self.uid
