import os
import random
from datetime import datetime
from cryptography.fernet import Fernet

try:
    import colorama
    colorama.init()
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
except ImportError:
    RED = GREEN = YELLOW = BLUE = MAGENTA = CYAN = WHITE = RESET = BOLD = ''

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

LOG_FILE = os.path.join(os.path.dirname(__file__), 'decmes_log.txt')
KEY_FILE = os.path.join(os.path.dirname(__file__), 'secret.key')

def log_action(action, details=""):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, 'a', encoding='utf-8') as log:
        log.write(f"\n{'='*60}\n")
        log.write(f"[{timestamp}] {action}\n")
        if details:
            log.write(f"Детали: {details}\n")
        log.write(f"{'='*60}\n")

def generate_key():
    key = Fernet.generate_key()
    with open(KEY_FILE, 'wb') as key_file:
        key_file.write(key)
    return key

def load_key():
    if not os.path.exists(KEY_FILE):
        return generate_key()
    with open(KEY_FILE, 'rb') as key_file:
        return key_file.read()

symbols = ([chr(32 + i) for i in range(95)] +
           [chr(0x4E00 + i) for i in range(161)])
random.seed(42)
symbols = random.sample(symbols, len(symbols))

def encode_message(message):
    key = load_key()
    f = Fernet(key)
    message_bytes = message.encode('utf-8')
    encrypted = f.encrypt(message_bytes)
    encoded_str = ''.join(symbols[b] for b in encrypted)
    return encoded_str

def decode_message(encoded_message):
    try:
        key = load_key()
        f = Fernet(key)
        encoded_bytes = bytes(symbols.index(c) for c in encoded_message)
        decrypted = f.decrypt(encoded_bytes)
        return decrypted.decode('utf-8')
    except Exception as e:
        return f"Ошибка дешифрования: {str(e)}"

def display_menu():
    clear_screen()
    print(f"{BOLD}{CYAN}DEC MES {WHITE}Encryption Tool{RESET}")
    print(f"{CYAN}Decrypt Encrypt Messages{RESET}\n")
    print(f"{BOLD}{BLUE}╔═══════════════════════════════════════════════════╗{RESET}")
    print(f"{BLUE}║{RESET}                                                   {BLUE}║{RESET}")
    print(f"{BLUE}║{RESET}  {BOLD}{GREEN}➤ [1]{RESET}{WHITE} Зашифровать сообщение                 {BLUE}     ║{RESET}")
    print(f"{BLUE}║{RESET}  {BOLD}{YELLOW}➤ [2]{RESET}{WHITE} Расшифровать сообщение               {BLUE}      ║{RESET}")
    print(f"{BLUE}║{RESET}  {BOLD}{RED}➤ [3]{RESET}{WHITE} Выход                                {BLUE}      ║{RESET}")
    print(f"{BLUE}║{RESET}                                                   {BLUE}║{RESET}")
    print(f"{BOLD}{BLUE}╚═══════════════════════════════════════════════════╝{RESET}")
    print(f"{BOLD}{WHITE}┌─ Выберите действие ──────────────────────────────┐{RESET}")
    print(f"{BOLD}{WHITE}└─> {RESET}", end='')

def main():
    log_action("Запуск программы", "DEC MES RGB Encryption Tool запущен")
    while True:
        display_menu()
        choice = input().strip()

        if choice == '1':
            log_action("Выбор действия", "Пользователь выбрал шифрование сообщения")
            clear_screen()
            print(f"{BOLD}{BLUE}╔═══════════════════════════════════════════════════╗{RESET}")
            print(f"{BLUE}║{RESET}          {BOLD}{GREEN}ЗАШИФРОВАНИЕ СООБЩЕНИЯ{RESET}           {BLUE}        ║{RESET}")
            print(f"{BOLD}{BLUE}╚═══════════════════════════════════════════════════╝{RESET}")
            message = input(f"{BOLD}{WHITE}┌─ Введите сообщение для шифрования ──────────────┐{RESET}\n{BOLD}{WHITE}└─> {RESET}")
            if message:
                encoded = encode_message(message)
                log_action("Шифрование выполнено", f"Исходное: '{message}' -> Зашифрованное: '{encoded}'")
                print(f"\n{BOLD}{GREEN}┌─ Зашифрованное сообщение ────────────────────────┐{RESET}")
                print(f"{GREEN}│{RESET} {BOLD}{MAGENTA}{encoded}{RESET}")
                print(f"{BOLD}{GREEN}└─────────────────────────────────────────────────┘{RESET}")
            else:
                log_action("Ошибка шифрования", "Попытка зашифровать пустое сообщение")
                print(f"{BOLD}{RED}┌─ Ошибка ─────────────────────────────────────────┐{RESET}")
                print(f"{RED}│{RESET} Сообщение не может быть пустым.               {RED}│{RESET}")
                print(f"{BOLD}{RED}└─────────────────────────────────────────────────┘{RESET}")
            input(f"\n{BOLD}{BLUE}┌─ Нажмите Enter для продолжения ──────────────────┐{RESET}\n{BOLD}{BLUE}└─> {RESET}")

        elif choice == '2':
            log_action("Выбор действия", "Пользователь выбрал расшифровку сообщения")
            clear_screen()
            print(f"{BOLD}{BLUE}╔═══════════════════════════════════════════════════╗{RESET}")
            print(f"{BLUE}║{RESET}          {BOLD}{YELLOW}РАСШИФРОВКА СООБЩЕНИЯ{RESET}            {BLUE}        ║{RESET}")
            print(f"{BOLD}{BLUE}╚═══════════════════════════════════════════════════╝{RESET}")
            encoded_message = input(f"{BOLD}{WHITE}┌─ Введите зашифрованное сообщение ────────────────┐{RESET}\n{BOLD}{WHITE}└─> {RESET}")
            if encoded_message:
                decoded = decode_message(encoded_message)
                log_action("Расшифровка выполнена", f"Зашифрованное: '{encoded_message}' -> Расшифрованное: '{decoded}'")
                print(f"\n{BOLD}{GREEN}┌─ Расшифрованное сообщение ───────────────────────┐{RESET}")
                print(f"{GREEN}│{RESET} {BOLD}{MAGENTA}{decoded}{RESET}")
                print(f"{BOLD}{GREEN}└─────────────────────────────────────────────────┘{RESET}")
            else:
                log_action("Ошибка расшифровки", "Попытка расшифровать пустое сообщение")
                print(f"{BOLD}{RED}┌─ Ошибка ─────────────────────────────────────────┐{RESET}")
                print(f"{RED}│{RESET} Зашифрованное сообщение не может быть пустым.{RED}│{RESET}")
                print(f"{BOLD}{RED}└─────────────────────────────────────────────────┘{RESET}")
            input(f"\n{BOLD}{BLUE}┌─ Нажмите Enter для продолжения ──────────────────┐{RESET}\n{BOLD}{BLUE}└─> {RESET}")

        elif choice == '3':
            log_action("Выход из программы", "Пользователь завершил работу с программой")
            clear_screen()
            print(f"{BOLD}{GREEN}╔═══════════════════════════════════════════════════╗{RESET}")
            print(f"{GREEN}║{RESET}        {BOLD}{WHITE}Спасибо за использование программы! {RESET}     {GREEN}║{RESET}")
            print(f"{BOLD}{GREEN}╚═══════════════════════════════════════════════════╝{RESET}")
            break

        else:
            log_action("Неверный выбор", f"Пользователь ввел: '{choice}'")
            clear_screen()
            print(f"{BOLD}{RED}╔═══════════════════════════════════════════════════╗{RESET}")
            print(f"{RED}║{RESET}           {BOLD}{WHITE}Неверный выбор. Попробуйте снова.{RESET}        {RED}║{RESET}")
            print(f"{BOLD}{RED}╚═══════════════════════════════════════════════════╝{RESET}")
            input(f"{BOLD}{BLUE}┌─ Нажмите Enter для продолжения ──────────────────┐{RESET}\n{BOLD}{BLUE}└─> {RESET}")

if __name__ == "__main__":
    main()