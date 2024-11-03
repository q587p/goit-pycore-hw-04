import sys
from pathlib import Path
from colorama import init, Fore, Style

# Ініціалізація colorama
init()

def print_directory_structure(path: Path, indent: str = ""):
    if not path.is_dir():
        print(f"{Fore.RED}Помилка: {path} не є директорією{Style.RESET_ALL}")
        return

    # Перебір вмісту директорії
    for item in path.iterdir():
        if item.is_dir():
            print(f"{indent}{Fore.BLUE}📂 {item.name}{Style.RESET_ALL}")
            # Рекурсивний виклик для піддиректорій
            print_directory_structure(item, indent + "    ")
        else:
            print(f"{indent}{Fore.GREEN}📜 {item.name}{Style.RESET_ALL}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"{Fore.RED}Використання: python task3.py /шлях/до/директорії{Style.RESET_ALL}")
        sys.exit(1)

    directory_path = Path(sys.argv[1])
    print_directory_structure(directory_path)