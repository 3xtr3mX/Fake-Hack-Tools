import random
import time
import os
from colorama import Fore, Style, init

# Initialisation de Colorama
init(autoreset=True)

def clear_screen():
    """Efface l'écran."""
    os.system('cls' if os.name == 'nt' else 'clear')

def show_intro():
    intro_text = r"""
  ________  ________  ________  ________  ________  ________  ________  ________  ________  ________
 |\   __  \|\   __  \|\   __  \|\   __  \|\   __  \|\   __  \|\   __  \|\   __  \|\   __  \|\   __  \
 \ \  \|\  \ \  \|\  \ \  \|\  \ \  \|\  \ \  \|\  \ \  \|\  \ \  \|\  \ \  \|\  \ \  \|\  \ \  \|\  \
  \ \   ____\ \   __  \ \   __  \ \   ____\ \   __  \ \   __  \ \   __  \ \   __  \ \   ____\ \   __  \
   \ \  \___|\ \  \ \  \ \  \ \  \ \  \___|\ \  \ \  \ \  \ \  \ \  \ \  \ \  \ \  \ \  \___|\ \  \ \  \
    \ \__\    \ \__\ \__\ \__\ \__\ \__\    \ \__\ \__\ \__\ \__\ \__\ \__\ \__\ \__\    \ \__\ \__\
     \|__|     \|__|\|__|\|__|\|__|\|__|     \|__|\|__|\|__|\|__|\|__|\|__|\|__|\|__|     \|__|\|__|
    """
    print(intro_text)

def random_string(size):
    """Génère une chaîne aléatoire de caractères."""
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_-+=<>?/|{}[]~'
    return ''.join(random.choices(chars, k=size))

def generate_fake_ip():
    """Génère une adresse IP aléatoire."""
    return f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"

def generate_fake_database_result():
    """Génère des résultats de bases de données."""
    username = random_string(8)
    password = random_string(10)
    return f"[USER] {username} | [PASS] {password}"

def fake_processing_step(step_name, min_delay=2.5, max_delay=4.5):
    """Simule une étape avec des logs aléatoires."""
    print(f"{Fore.YELLOW}{step_name}")
    time.sleep(random.uniform(min_delay, max_delay))
    for _ in range(random.randint(5, 10)):  # Plus de logs aléatoires
        print(f"{Fore.GREEN}[INFO] {random_string(random.randint(15, 40))}")
        time.sleep(random.uniform(0.5, 1))

def loading_animation():
    """Affiche une animation de chargement avec des points."""
    for _ in range(3):
        print(f"{Fore.YELLOW}Chargement", end="")
        for _ in range(3):
            time.sleep(0.5)
            print(".", end="", flush=True)
        print()  # Saute une ligne après l'animation
        time.sleep(1)

def manual_selection_menu():
    """Menu interactif pour sélectionner une option."""
    print(f"{Fore.CYAN}\nMenu HackerTool3.0")
    print(f"{Fore.YELLOW}1. Scanner un réseau")
    print(f"{Fore.YELLOW}2. Lancer une attaque brute force")
    print(f"{Fore.YELLOW}3. Rechercher des bases de données")
    print(f"{Fore.YELLOW}4. Générer des clés SSH")
    print(f"{Fore.YELLOW}5. Quitter")
    choice = input(f"{Fore.CYAN}Sélectionnez une option (1-5) : ")
    return choice

def scan_network():
    """Effectue un scan de réseau et affiche les cibles détectées."""
    print(f"{Fore.MAGENTA}\n[SCAN RÉSEAU] Détection des cibles...\n")
    loading_animation()
    for _ in range(8):  # Plus de résultats pour une simulation plus complète
        ip = generate_fake_ip()
        open_ports = random.sample([21, 22, 80, 443, 3306, 8080], random.randint(2, 5))
        print(f"{Fore.GREEN}[TARGET] IP : {ip} | Ports ouverts : {open_ports}")
        time.sleep(2)
    input(f"{Fore.CYAN}\nAppuyez sur Entrée pour continuer...")
    clear_screen()

def brute_force():
    """Effectue une attaque brute force."""
    print(f"{Fore.MAGENTA}\n[BRUTE FORCE] Démarrage de l'attaque...\n")
    loading_animation()
    fake_processing_step("[INFO] Tentatives en cours...", 3, 4)
    print(f"{Fore.GREEN}[SUCCÈS] Accès obtenu pour l'utilisateur root!")
    print(f"{Fore.YELLOW}[DETAILS] IP : {generate_fake_ip()} | Password : {random_string(12)}")
    input(f"{Fore.CYAN}\nAppuyez sur Entrée pour continuer...")
    clear_screen()

def search_databases():
    """Recherche des bases de données accessibles."""
    print(f"{Fore.MAGENTA}\n[RECHERCHE DE BASES DE DONNÉES] En cours...\n")
    loading_animation()
    fake_processing_step("[INFO] Exploration des serveurs...", 3, 4)
    print(f"{Fore.CYAN}[RÉSULTATS] Bases de données trouvées :")
    for _ in range(8):  # Plus de résultats pour une meilleure immersion
        print(f"{Fore.YELLOW}{generate_fake_database_result()}")
        time.sleep(2)
    input(f"{Fore.CYAN}\nAppuyez sur Entrée pour continuer...")
    clear_screen()

def generate_ssh_keys():
    """Génère des clés SSH."""
    print(f"{Fore.MAGENTA}\n[GÉNÉRATION DE CLÉS SSH] En cours...\n")
    loading_animation()
    fake_processing_step("[INFO] Création de clés...", 2.5, 3.5)
    print(f"{Fore.GREEN}[CLÉ PUBLIQUE] ssh-rsa AAAAB3NzaC1yc2E...{random_string(10)}")
    print(f"{Fore.GREEN}[CLÉ PRIVÉE] {random_string(64)}")
    input(f"{Fore.CYAN}\nAppuyez sur Entrée pour continuer...")
    clear_screen()

def main():
    show_intro()
    while True:
        choice = manual_selection_menu()
        if choice == "1":
            scan_network()
        elif choice == "2":
            brute_force()
        elif choice == "3":
            search_databases()
        elif choice == "4":
            generate_ssh_keys()
        elif choice == "5":
            print(f"{Fore.RED}\nFermeture de HackerTool3.0...")
            break
        else:
            print(f"{Fore.RED}\nOption invalide. Veuillez réessayer.")
        input(f"{Fore.CYAN}\nAppuyez sur Entrée pour continuer...")

if __name__ == "__main__":
    main()
