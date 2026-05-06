from typing import Callable
from src.utils import get_breakline

from .File import File
from .Bet import Bet
from .Client import Client
from .Game import Game
from .Movimentation import Movimentation


# === CONSTANTS ===
ENTITY_MAP = {
    "Apostas": "bets",
    "Clientes": "clients",
    "Jogos": "games",
    "Movimentações": "movimentations",
}

ACTIONS_MAP = {
    1: "list",
    2: "read",
    3: "create",
    4: "update",
    5: "delete",
}

options = list(ENTITY_MAP.keys()) + ["Sair"]
sub_options = ["Listar", "Visualizar", "Adicionar", "Editar", "Excluir", "Voltar"]


class Program:
    def __init__(self):
        # collections
        self.bets: list[Bet] = []
        self.clients: list[Client] = []
        self.games: list[Game] = []
        self.movimentations: list[Movimentation] = []

        # states
        self.is_running = True
        self.selected_type = None
        self.selected_action = None

        # output paths
        self.output_paths = {
            "bets": "output/bets.txt",
            "clients": "output/clients.txt",
            "games": "output/games.txt",
            "movimentations": "output/movimentations.txt",
        }

        # metadata
        self.entity_configs = {
            "bets": {
                "file": "database/bets.txt",
                "cls": Bet,
                "parser": lambda b: Bet(*b)
            },
            "clients": {
                "file": "database/clients.txt",
                "cls": Client,
                "parser": lambda c: Client(*c)
            },
            "games": {
                "file": "database/games.txt",
                "cls": Game,
                "parser": lambda g: Game(*g)
            },
            "movimentations": {
                "file": "database/movimentations.txt",
                "cls": Movimentation,
                "parser": lambda m: Movimentation(*m)
            }
        }

    # ========== INITIALIZATION ==========
    def init(self):
        for key, config in self.entity_configs.items():
            setattr(self, key, self.load_entities(config["file"], config["parser"]))

    def load_entities(self, filepath: str, parser: Callable):
        file = File(filepath)
        entities = []

        for line in file.get_lines():
            parts = line.split(";")
            entities.append(parser(parts))

        return entities

    def close(self):
        for entity_name, output_path in self.output_paths.items():
            entity_list: list[Bet | Client | Game | Movimentation] = getattr(self, entity_name)

            with open(output_path, "w", encoding="utf-8") as f:
                    for e in entity_list:
                        f.write(e.write_content() + "\n")

    # ========== UI UTILITIES ==========
    def display_menu(self, items: list[str]):
        for i, item in enumerate(items, 1):
            breakline = get_breakline("TWO_LINES") if i == len(items) else get_breakline("NEW_LINE")
            print(f"{i} - {item}", end=breakline)

    def choose_option(self, max_option: int) -> int:
        try:
            choose = int(input("Escolha uma opção pelo número: "))
            if 1 <= choose <= max_option:
                return choose
        except ValueError:
            pass

        print("Opção inválida.\n")
        return -1

    # ========== MAIN LOOP ==========
    def loop(self):
        while self.is_running:
            self.display_menu(options)
            choose = self.choose_option(len(options))
            self.actions(choose)

    # ========== MENU ACTIONS ==========
    def actions(self, choose: int):
        if choose == len(options):
            print("Programa finalizado com sucesso.")
            self.is_running = False
            return

        if choose <= 0:
            return

        self.selected_type = options[choose - 1]
        print(f"\n--- {self.selected_type} ---\n")

        self.submenu_loop()

    def submenu_loop(self):
        while True:
            self.display_menu(sub_options)
            sub = self.choose_option(len(sub_options))

            if sub == len(sub_options):
                print("\nRetornando ao menu principal...\n")
                return

            if sub not in ACTIONS_MAP:
                print("Opção inválida.\n")
                continue

            self.selected_action = ACTIONS_MAP[sub]
            self.perform_action()

    # ========== ACTION HANDLER ==========
    def perform_action(self):
        entity_name = ENTITY_MAP[self.selected_type]
        entity_list = getattr(self, entity_name)

        handler_map = {
            "list":   self.handle_list,
            "read":   self.handle_read,
            "create": self.handle_create,
            "update": self.handle_update,
            "delete": self.handle_delete,
        }

        handler = handler_map.get(self.selected_action)

        if handler:
            handler(entity_list)
        else:
            print("Ação não implementada.\n")

    # ========== CRUD IMPLEMENTATIONS ==========

    # ------- LIST -------
    def handle_list(self, entity_list: list[Bet | Client | Game | Movimentation]):
        if not entity_list:
            print("Nenhum registro encontrado.\n")
            return

        print("\nPressione ENTER para avançar, ou 'q' para sair.\n")

        for i, entity in enumerate(entity_list, 1):
            print(entity.write_content())
            print(f"[{i}/{len(entity_list)}]")

            if input().lower().strip() == "q":
                break

    # ------- READ -------
    def handle_read(self, entity_list: list[Bet | Client | Game | Movimentation]):
        pk = int(input("Digite a chave primária: ").strip())

        found = next((e for e in entity_list if e.get_uid() == pk), None)
        print()

        if not found:
            print("Nenhum registro encontrado.\n")
        else:
            print(found.write_content())

    # ------- CREATE -------
    def handle_create(self, entity_list: list[Bet | Client | Game | Movimentation]):
        user_input = input("Digite os campos separados por espaço: ").split()
        next_uid = entity_list[-1].get_uid() + 1

        entity_name = ENTITY_MAP[self.selected_type]
        cls = self.entity_configs[entity_name]["cls"]

        entity_list.append(cls(next_uid, *user_input))

    # ------- UPDATE -------
    def handle_update(self, entity_list: list[Bet | Client | Game | Movimentation]):
        pk = int(input("Digite a chave primária: ").strip())
        found = next((e for e in entity_list if e.get_uid() == pk), None)

        if not found:
            print("Nenhum registro encontrado.\n")
        else:
            user_input = input("Novos valores separados por espaço: ").split()
            found.update(*user_input)

    # ------- DELETE -------
    def handle_delete(self, entity_list: list[Bet | Client | Game | Movimentation]):
        pk = int(input("Digite a chave primária: ").strip())
        found = next((e for e in entity_list if e.get_uid() == pk), None)

        if not found:
            print("Nenhum registro encontrado.\n")
        else:
            entity_list.remove(found)
            print("\nRegistro excluído com sucesso!\n")        
