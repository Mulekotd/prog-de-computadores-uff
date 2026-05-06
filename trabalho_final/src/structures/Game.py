import json


class Game:
    def __init__(self, uid: str, name: str, house_edge: str, min_bet: str, max_bet: str, category: str, active: str, rules: str):
        self.uid: int = int(uid)
        self.name: str = name
        self.house_edge: float = float(house_edge)
        self.min_bet: float = float(min_bet)
        self.max_bet: float = float(max_bet)
        self.category: str = category
        self.active: bool = bool(active)
        self.rules: list[str] = json.loads(rules)

    def update(self, name: str = None, house_edge: str = None, min_bet: str = None, max_bet: str = None, category: str = None, active: str = None, rules: str = None) -> None:
        self.name: str = name if name is not None else self.name
        self.house_edge: float = float(house_edge) if house_edge is not None else self.house_edge
        self.min_bet: float = float(min_bet) if min_bet is not None else self.min_bet
        self.max_bet: float = float(max_bet) if max_bet is not None else self.max_bet
        self.category: str = category if category is not None else self.category
        self.active: bool = bool(active) if active is not None else self.active
        self.rules: list[str] = json.loads(rules) if rules is not None else self.rules
    
    def write_content(self) -> str:
        return (
            f"GAME UID: {self.uid}\n"
            f"NAME: {self.name}\n"
            f"HOUSE EDGE: {self.house_edge}\n"
            f"BET RANGE: {self.min_bet} - {self.max_bet}\n"
            f"CATEGORY: {self.category}\n"
            f"ACTIVE: {self.active}\n"
            f"RULES: {self.rules}\n"
        )

    def get_uid(self) -> int:
        return self.uid
