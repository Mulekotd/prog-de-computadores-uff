from pathlib import Path
from src.utils import calculate_execution_time

import random
import json


# sizes
MOV_LINES = 25_000
BET_LINES = 5_000
CLIENT_LINES = 500

# fixed games
GAMES_LIST = [
    ("Bilhar americano", "table"),
    ("Pôquer", "table"),
    ("Bacará", "table"),
    ("Blackjack", "table"),
    ("Roleta", "table"),
    ("Caça-níquel", "slot"),
    ("Pachinko", "slot"),
    ("Keno", "random"),
    ("Bingo", "random")
]

root = Path("database")
mov_path = root / "movimentations.txt"
bet_path = root / "bets.txt"
client_path = root / "clients.txt"
games_path = root / "games.txt"


def generate_movimentations():
    with open(mov_path, "w", encoding="utf-8") as f:
        for i in range(1, MOV_LINES + 1):
            sender = random.choice(["casino", f"{random.randint(1, CLIENT_LINES)}"])
            recipient = random.choice(["casino", f"{random.randint(1, CLIENT_LINES)}"])
            amount = round(random.uniform(5, 250_000), 2)
            dt = f"2025-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}"
            ttype = random.choice(["deposit","withdraw","bet","payout"])
            tags = ["AUTO","BR","FAST"] if random.random() < 0.4 else ["AUTO"]
            f.write(f"{i};{sender};{recipient};{amount};{dt};{ttype};{json.dumps(tags)}\n")

def generate_bets():
    with open(bet_path,"w",encoding="utf-8") as f:
        for i in range(1, BET_LINES + 1):
            uuid = f"{random.randint(1, 250)}"
            game_id = random.randint(1, len(GAMES_LIST))
            amount = round(random.uniform(1, 1_000), 2)
            outcome = random.choice(["win","lose","push"])
            payout = round(amount*random.uniform(0.1, 2.5), 2)
            dt = f"2025-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}"
            odds = [round(random.uniform(1.1, 2.7), 2) for _ in range(3)]
            f.write(f"{i};{uuid};{game_id};{amount};{outcome};{payout};{dt};{json.dumps(odds)}\n")

def generate_clients():
    names = ["Ana","Pedro","João","Thiago","Lara","Beatriz","Yuri","Carlos","Daniel","Arthur"]
    ln = ["Silva","Pereira","Lima","Castro","Moraes","Alcantara"]
    
    with open(client_path,"w",encoding="utf-8") as f:
        for i in range(1, CLIENT_LINES + 1):
            fn = random.choice(names)
            ln2 = random.choice(ln)
            country = random.choice(["BR","US","JP","AR","CL"])
            balance = round(random.uniform(0, 1_000_000), 2)
            v = random.randint(0, 5)
            pm = random.sample(["PIX","CREDIT_CARD","BTC","PAYPAL"], random.randint(1, 3))
            f.write(f"{i};{fn};{ln2};{country};{balance};{v};{json.dumps(pm)}\n")

def generate_games():
    with open(games_path,"w",encoding="utf-8") as f:
        for i,(n,cat) in enumerate(GAMES_LIST, start=1):
            house = round(random.uniform(0.01, 0.12), 3)
            minb = round(random.uniform(1, 10), 2)
            maxb = round(random.uniform(50, 5000), 2)
            active = random.choice([True, False])
            rules = random.sample(["RULE1", "RULE2", "RULE3", "RULE4", "RULE5", "RULE6"], 2)
            f.write(f"{i};{n};{house};{minb};{maxb};{cat};{active};{json.dumps(rules)}\n")

tm,_ = calculate_execution_time(generate_movimentations)
tb,_ = calculate_execution_time(generate_bets)
tc,_ = calculate_execution_time(generate_clients)
tg,_ = calculate_execution_time(generate_games)

print("| File               | Time     |")
print("| ------------------ | -------- |")
print(f"| movimentations.txt | {tm:.2f}ms |")
print(f"| bets.txt           | {tb:.2f}ms  |")
print(f"| clients.txt        | {tc:.2f}ms   |")
print(f"| games.txt          | {tg:.2f}ms   |")
