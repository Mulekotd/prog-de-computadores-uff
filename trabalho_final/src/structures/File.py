import os


class File:
    def __init__(self, path: str):
        self.path: str = path
        os.makedirs(os.path.dirname(path), exist_ok=True)

    def get_lines(self) -> list[str]:
        if not os.path.exists(self.path):
            return []
        
        lines = self.read()

        if not lines:
            return []

        return [line.strip() for line in lines if line.strip()]
    
    def write(self, content: str) -> None:
        with open(self.path, "w", encoding="utf-8") as f:
            f.write(content)

    def read(self) -> list[str]:
        with open(self.path, encoding="utf-8") as f:
            return f.readlines()

    def append(self, new_line: str) -> None:
        with open(self.path, "a", encoding="utf-8") as f:
            f.write(new_line + "\n")
