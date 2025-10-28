# DEC MES RGB Encryption Tool

### _Beautiful console application for message encryption and decryption_

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Cryptography](https://img.shields.io/badge/Cryptography-AES--256-green.svg)](https://cryptography.io/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Русский** | [English](README_EN.md)

DEC MES RGB - это красивое консольное приложение для шифрования и дешифрования сообщений с использованием современных криптографических алгоритмов и стильным интерфейсом в стиле Linux.

![Demo](demo.png)

### 🚀 Быстрый старт

```bash
# Установка зависимостей
pip install cryptography colorama

# Запуск программы
python decompilermessages.py
```

[Скачать последнюю версию](https://github.com/yourusername/decmes-rgb/releases)

## ✨ Возможности

- 🔐 **Надежное шифрование** - AES-256 через Fernet (библиотека cryptography)
- 🎨 **Красивый интерфейс** - цветной вывод с рамками в стиле Linux
- 🌍 **Поддержка UTF-8** - шифрование сообщений на любом языке
- 📝 **Логирование** - все действия записываются в файл с timestamp
- 🔒 **Безопасность** - расшифровка возможна только через этот скрипт
- 🎭 **Уникальные символы** - зашифрованный текст состоит из микса ASCII и китайских иероглифов
- 💻 **Кроссплатформенность** - работает на Windows, Linux, macOS

## 📋 Как использовать

1. **Запустите программу:**
   ```bash
   python decompilermessages.py
   ```

2. **Выберите действие:**
   - `1` - Зашифровать сообщение
   - `2` - Расшифровать сообщение
   - `3` - Выход

3. **Шифрование:**
   - Введите текст на любом языке
   - Получите зашифрованную строку из уникальных символов

4. **Расшифровка:**
   - Вставьте зашифрованную строку
   - Получите оригинальный текст

## 📁 Структура проекта

```
decmes-rgb/
├── decompilermessages.py    # Основной скрипт
├── secret.key              # Ключ шифрования (создается автоматически)
├── decmes_log.txt          # Лог всех действий
└── README.md              # Документация
```

## 🛠 Технические детали

### Архитектура

**Основные функции:**
- `clear_screen()` - Очистка консоли (кроссплатформенно)
- `log_action(action, details="")` - Логирование действий с timestamp
- `generate_key()` / `load_key()` - Управление ключами шифрования
- `encode_message(message)` - Шифрование с представлением в виде строки символов
- `decode_message(encoded_message)` - Расшифровка из строки символов
- `display_menu()` - Отображение главного меню
- `main()` - Основной цикл программы

### Используемые технологии

- **Python 3.8+**
- **[cryptography](https://cryptography.io/)** - для AES-256 шифрования через Fernet
- **[colorama](https://pypi.org/project/colorama/)** - для цветного вывода в консоли
- **datetime** - для логирования с метками времени
- **random** - для создания уникального набора символов

### Алгоритм шифрования

1. **AES-256 через Fernet** - проверенный криптографический алгоритм
2. **Уникальный набор символов** - 256 символов (ASCII + китайские иероглифы)
3. **Перемешивание** - символы перемешиваются с фиксированным seed
4. **Однонаправленность** - расшифровка возможна только через этот скрипт

### Безопасность

- Ключ шифрования хранится локально в `secret.key`
- Все действия логируются для аудита
- Шифрование использует проверенные криптографические алгоритмы
- Расшифровка невозможна без правильного ключа и скрипта

## 🚀 Установка и запуск

### Системные требования
- Python 3.8 или выше
- pip для установки зависимостей

### Установка

1. **Клонируйте репозиторий:**
   ```bash
   git clone https://github.com/yourusername/decmes-rgb.git
   cd decmes-rgb
   ```

2. **Установите зависимости:**
   ```bash
   pip install cryptography colorama
   ```

3. **Запустите программу:**
   ```bash
   python decompilermessages.py
   ```

### Первый запуск

При первом запуске программа автоматически:
- Создаст файл `secret.key` с ключом шифрования
- Создаст файл `decmes_log.txt` для логирования
- Покажет приветственное меню

## 📄 Примеры использования

### Шифрование сообщения
```
┌─ Введите сообщение для шифрования ──────────────┐
└─> Привет, мир!

┌─ Зашифрованное сообщение ────────────────────────┐
│ 龘龙龚龛龜龝龞龟龠龡龢龣龤龥龦龧龨龩龪龫龬龭龮龯龰
└─────────────────────────────────────────────────┘
```

### Расшифровка сообщения
```
┌─ Введите зашифрованное сообщение ────────────────┐
└─> 龘龙龚龛龜龝龞龟龠龡龢龣龤龥龦龧龨龩龪龫龬龭龮龯龰

┌─ Расшифрованное сообщение ───────────────────────┐
│ Привет, мир!
└─────────────────────────────────────────────────┘
```

## 📋 Логирование

Все действия программы записываются в файл `decmes_log.txt`:

```
============================================================
[2025-10-28 21:45:30] Запуск программы
Детали: DEC MES RGB Encryption Tool запущен
============================================================
[2025-10-28 21:45:35] Шифрование выполнено
Детали: Исходное: 'Hello World' -> Зашифрованное: '龘龙龚龛...'
============================================================
```

## 🔧 Разработка

### Структура кода

Проект состоит из одного основного файла `decompilermessages.py` с чистой архитектурой:

```python
# Импорты
import os
import random
from datetime import datetime
from cryptography.fernet import Fernet

# Глобальные переменные для цветов
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

# Пути к файлам
LOG_FILE = os.path.join(os.path.dirname(__file__), 'decmes_log.txt')
KEY_FILE = os.path.join(os.path.dirname(__file__), 'secret.key')

# Набор символов для шифрования (256 уникальных символов)
symbols = ([chr(32 + i) for i in range(95)] +
           [chr(0x4E00 + i) for i in range(161)])
random.seed(42)
symbols = random.sample(symbols, len(symbols))

def log_action(action, details=""):
    """Записывает действие в лог-файл с красивым оформлением."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, 'a', encoding='utf-8') as log:
        log.write(f"\n{'='*60}\n")
        log.write(f"[{timestamp}] {action}\n")
        if details:
            log.write(f"Детали: {details}\n")
        log.write(f"{'='*60}\n")

def clear_screen():
    """Очищает экран консоли."""
    os.system('cls' if os.name == 'nt' else 'clear')

def generate_key():
    """Генерирует и сохраняет ключ шифрования."""
    key = Fernet.generate_key()
    with open(KEY_FILE, 'wb') as key_file:
        key_file.write(key)
    return key

def load_key():
    """Загружает ключ шифрования."""
    if not os.path.exists(KEY_FILE):
        return generate_key()
    with open(KEY_FILE, 'rb') as key_file:
        return key_file.read()

def encode_message(message):
    """Шифрует сообщение с помощью Fernet (AES) и представляет как строку с множеством символов."""
    key = load_key()
    f = Fernet(key)
    message_bytes = message.encode('utf-8')
    encrypted = f.encrypt(message_bytes)
    # Представляем каждый байт как символ из набора symbols
    encoded_str = ''.join(symbols[b] for b in encrypted)
    return encoded_str

def decode_message(encoded_message):
    """Дешифрует сообщение из строки с множеством символов."""
    try:
        key = load_key()
        f = Fernet(key)
        # Преобразуем строку обратно в байты, используя индекс в symbols
        encoded_bytes = bytes(symbols.index(c) for c in encoded_message)
        decrypted = f.decrypt(encoded_bytes)
        return decrypted.decode('utf-8')
    except Exception as e:
        return f"Ошибка дешифрования: {str(e)}"

def display_menu():
    """Отображает главное меню."""
    clear_screen()
    print(f"{BOLD}{CYAN}DEC MES {RED}R{RESET}{BOLD}{GREEN}G{RESET}{BOLD}{BLUE}B{RESET} {WHITE}Encryption Tool{RESET}")
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
            print(f"{BLUE}║{RESET}          {BOLD}{GREEN}ЗАШИФРОВАНИЕ СООБЩЕНИЯ{RESET}           {BLUE}║{RESET}")
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
            print(f"{BLUE}║{RESET}          {BOLD}{YELLOW}РАСШИФРОВКА СООБЩЕНИЯ{RESET}            {BLUE}║{RESET}")
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
            print(f"{GREEN}║{RESET}        {BOLD}{WHITE}Спасибо за использование программы! 👋{RESET}     {GREEN}║{RESET}")
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
```

### Добавление новых функций

1. Добавьте функцию в соответствующий раздел
2. Обновите логирование для новых действий
3. Протестируйте на разных платформах
4. Обновите документацию

## 🤝 Вклад в проект

1. Форкните репозиторий
2. Создайте ветку для вашей функции (`git checkout -b feature/AmazingFeature`)
3. Зафиксируйте изменения (`git commit -m 'Add some AmazingFeature'`)
4. Отправьте в ветку (`git push origin feature/AmazingFeature`)
5. Откройте Pull Request

## 📄 Лицензия

Этот проект распространяется под лицензией MIT. Подробности в файле [LICENSE](LICENSE).

## 🙏 Благодарности

- [cryptography](https://cryptography.io/) - для криптографических функций
- [colorama](https://pypi.org/project/colorama/) - для цветного вывода в консоль
- Сообществу Python за отличный язык программирования

---

**Создано с ❤️ для безопасного обмена сообщениями**
    import colorama
    # Определение цветов...
except ImportError:
    # Fallback для случаев без colorama

# Вспомогательные функции
def clear_screen(): ...
def log_action(action, details=""): ...

# Функции шифрования
def generate_key(): ...
def load_key(): ...
def encode_message(message): ...
def decode_message(encoded_message): ...

# Интерфейс
def display_menu(): ...
def main(): ...
```

### Добавление новых функций

1. Добавьте функцию в соответствующий раздел
2. Обновите логирование для новых действий
3. Протестируйте на разных платформах
4. Обновите документацию

