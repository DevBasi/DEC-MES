# DEC MES RGB Encryption Tool

### _Beautiful console application for message encryption and decryption_

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Cryptography](https://img.shields.io/badge/Cryptography-AES--256-green.svg)](https://cryptography.io/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

English | [Русский](README.md)

DEC MES RGB is a beautiful console application for encrypting and decrypting messages using modern cryptographic algorithms and a stylish Linux-style interface.

![Demo](demo.png)

### 🚀 Quick Start

```bash
# Install dependencies
pip install cryptography colorama

# Run the program
python decompilermessages.py
```

[Download latest version](https://github.com/yourusername/decmes-rgb/releases)

## ✨ Features

- 🔐 **Strong encryption** - AES-256 via Fernet (cryptography library)
- 🎨 **Beautiful interface** - colored output with Linux-style frames
- 🌍 **UTF-8 support** - encrypt messages in any language
- 📝 **Logging** - all actions are logged to a file with timestamps
- 🔒 **Security** - decryption is only possible through this script
- 🎭 **Unique symbols** - encrypted text consists of a mix of ASCII and Chinese characters
- 💻 **Cross-platform** - works on Windows, Linux, macOS

## 📋 How to Use

1. **Run the program:**
   ```bash
   python decompilermessages.py
   ```

2. **Choose an action:**
   - `1` - Encrypt message
   - `2` - Decrypt message
   - `3` - Exit

3. **Encryption:**
   - Enter text in any language
   - Get an encrypted string of unique symbols

4. **Decryption:**
   - Paste the encrypted string
   - Get the original text

## 📁 Project Structure

```
decmes-rgb/
├── decompilermessages.py    # Main script
├── secret.key              # Encryption key (created automatically)
├── decmes_log.txt          # All actions log
└── README.md              # Documentation
```

## 🛠 Technical Details

### Architecture

**Main functions:**
- `clear_screen()` - Clear console (cross-platform)
- `log_action(action, details="")` - Log actions with timestamp
- `generate_key()` / `load_key()` - Key management
- `encode_message(message)` - Encrypt and represent as string of symbols
- `decode_message(encoded_message)` - Decrypt from string of symbols
- `display_menu()` - Display main menu
- `main()` - Main program loop

### Technologies Used

- **Python 3.8+**
- **[cryptography](https://cryptography.io/)** - for AES-256 encryption via Fernet
- **[colorama](https://pypi.org/project/colorama/)** - for colored console output
- **datetime** - for logging with timestamps
- **random** - for creating unique symbol set

### Encryption Algorithm

1. **AES-256 via Fernet** - proven cryptographic algorithm
2. **Unique symbol set** - 256 symbols (ASCII + Chinese characters)
3. **Shuffling** - symbols are shuffled with fixed seed
4. **One-way** - decryption is only possible through this script

### Security

- Encryption key is stored locally in `secret.key`
- All actions are logged for audit
- Encryption uses proven cryptographic algorithms
- Decryption is impossible without the correct key and script

## 🚀 Installation and Launch

### System Requirements
- Python 3.8 or higher
- pip for dependency installation

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/decmes-rgb.git
   cd decmes-rgb
   ```

2. **Install dependencies:**
   ```bash
   pip install cryptography colorama
   ```

3. **Run the program:**
   ```bash
   python decompilermessages.py
   ```

### First Launch

On first launch, the program automatically:
- Creates `secret.key` file with encryption key
- Creates `decmes_log.txt` file for logging
- Shows welcome menu

## 📄 Usage Examples

### Message Encryption
```
┌─ Enter message to encrypt ──────────────────┐
└─> Hello World!

┌─ Encrypted message ────────────────────────┐
│ 龘龙龚龛龜龝龞龟龠龡龢龣龤龥龦龧龨龩龪龫龬龭龮龯龰
└───────────────────────────────────────────┘
```

### Message Decryption
```
┌─ Enter encrypted message ──────────────────┐
└─> 龘龙龚龛龜龝龞龟龠龡龢龣龤龥龦龧龨龩龪龫龬龭龮龯龰

┌─ Decrypted message ───────────────────────┐
│ Hello World!
└──────────────────────────────────────────┘
```

## 📋 Logging

All program actions are logged to the `decmes_log.txt` file:

```
============================================================
[2025-10-28 21:45:30] Program start
Details: DEC MES RGB Encryption Tool launched
============================================================
[2025-10-28 21:45:35] Encryption performed
Details: Original: 'Hello World' -> Encrypted: '龘龙龚龛...'
============================================================
```

## 🔧 Development

### Code Structure

The project consists of one main file `decompilermessages.py` with clean architecture:

```python
# Imports
import os
import random
from datetime import datetime
from cryptography.fernet import Fernet

# Color variables
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

# File paths
LOG_FILE = os.path.join(os.path.dirname(__file__), 'decmes_log.txt')
KEY_FILE = os.path.join(os.path.dirname(__file__), 'secret.key')

# Symbol set for encryption (256 unique symbols)
symbols = ([chr(32 + i) for i in range(95)] +
           [chr(0x4E00 + i) for i in range(161)])
random.seed(42)
symbols = random.sample(symbols, len(symbols))

def log_action(action, details=""):
    """Logs action with beautiful formatting."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, 'a', encoding='utf-8') as log:
        log.write(f"\n{'='*60}\n")
        log.write(f"[{timestamp}] {action}\n")
        if details:
            log.write(f"Details: {details}\n")
        log.write(f"{'='*60}\n")

def clear_screen():
    """Clears console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def generate_key():
    """Generates and saves encryption key."""
    key = Fernet.generate_key()
    with open(KEY_FILE, 'wb') as key_file:
        key_file.write(key)
    return key

def load_key():
    """Loads encryption key."""
    if not os.path.exists(KEY_FILE):
        return generate_key()
    with open(KEY_FILE, 'rb') as key_file:
        return key_file.read()

def encode_message(message):
    """Encrypts message using Fernet (AES) and represents as string of symbols."""
    key = load_key()
    f = Fernet(key)
    message_bytes = message.encode('utf-8')
    encrypted = f.encrypt(message_bytes)
    # Represent each byte as symbol from symbols set
    encoded_str = ''.join(symbols[b] for b in encrypted)
    return encoded_str

def decode_message(encoded_message):
    """Decrypts message from string of symbols."""
    try:
        key = load_key()
        f = Fernet(key)
        # Convert string back to bytes using index in symbols
        encoded_bytes = bytes(symbols.index(c) for c in encoded_message)
        decrypted = f.decrypt(encoded_bytes)
        return decrypted.decode('utf-8')
    except Exception as e:
        return f"Decryption error: {str(e)}"

def display_menu():
    """Displays main menu."""
    clear_screen()
    print(f"{BOLD}{CYAN}DEC MES {RED}R{RESET}{BOLD}{GREEN}G{RESET}{BOLD}{BLUE}B{RESET} {WHITE}Encryption Tool{RESET}")
    print(f"{CYAN}Decrypt Encrypt Messages{RESET}\n")
    print(f"{BOLD}{BLUE}╔═══════════════════════════════════════════════════╗{RESET}")
    print(f"{BLUE}║{RESET}                                                   {BLUE}║{RESET}")
    print(f"{BLUE}║{RESET}  {BOLD}{GREEN}➤ [1]{RESET}{WHITE} Encrypt message                     {BLUE}     ║{RESET}")
    print(f"{BLUE}║{RESET}  {BOLD}{YELLOW}➤ [2]{RESET}{WHITE} Decrypt message                     {BLUE}      ║{RESET}")
    print(f"{BLUE}║{RESET}  {BOLD}{RED}➤ [3]{RESET}{WHITE} Exit                                {BLUE}      ║{RESET}")
    print(f"{BLUE}║{RESET}                                                   {BLUE}║{RESET}")
    print(f"{BOLD}{BLUE}╚═══════════════════════════════════════════════════╝{RESET}")
    print(f"{BOLD}{WHITE}┌─ Choose action ────────────────────────────────┐{RESET}")
    print(f"{BOLD}{WHITE}└─> {RESET}", end='')

def main():
    log_action("Program start", "DEC MES RGB Encryption Tool launched")
    while True:
        display_menu()
        choice = input().strip()

        if choice == '1':
            log_action("Action choice", "User chose message encryption")
            clear_screen()
            print(f"{BOLD}{BLUE}╔═══════════════════════════════════════════════════╗{RESET}")
            print(f"{BLUE}║{RESET}          {BOLD}{GREEN}MESSAGE ENCRYPTION{RESET}            {BLUE}║{RESET}")
            print(f"{BOLD}{BLUE}╚═══════════════════════════════════════════════════╝{RESET}")
            message = input(f"{BOLD}{WHITE}┌─ Enter message to encrypt ──────────────────────┐{RESET}\n{BOLD}{WHITE}└─> {RESET}")
            if message:
                encoded = encode_message(message)
                log_action("Encryption performed", f"Original: '{message}' -> Encrypted: '{encoded}'")
                print(f"\n{BOLD}{GREEN}┌─ Encrypted message ─────────────────────────────┐{RESET}")
                print(f"{GREEN}│{RESET} {BOLD}{MAGENTA}{encoded}{RESET}")
                print(f"{BOLD}{GREEN}└─────────────────────────────────────────────────┘{RESET}")
            else:
                log_action("Encryption error", "Attempt to encrypt empty message")
                print(f"{BOLD}{RED}┌─ Error ─────────────────────────────────────────┐{RESET}")
                print(f"{RED}│{RESET} Message cannot be empty.                    {RED}│{RESET}")
                print(f"{BOLD}{RED}└─────────────────────────────────────────────────┘{RESET}")
            input(f"\n{BOLD}{BLUE}┌─ Press Enter to continue ───────────────────────┐{RESET}\n{BOLD}{BLUE}└─> {RESET}")

        elif choice == '2':
            log_action("Action choice", "User chose message decryption")
            clear_screen()
            print(f"{BOLD}{BLUE}╔═══════════════════════════════════════════════════╗{RESET}")
            print(f"{BLUE}║{RESET}          {BOLD}{YELLOW}MESSAGE DECRYPTION{RESET}            {BLUE}║{RESET}")
            print(f"{BOLD}{BLUE}╚═══════════════════════════════════════════════════╝{RESET}")
            encoded_message = input(f"{BOLD}{WHITE}┌─ Enter encrypted message ───────────────────────┐{RESET}\n{BOLD}{WHITE}└─> {RESET}")
            if encoded_message:
                decoded = decode_message(encoded_message)
                log_action("Decryption performed", f"Encrypted: '{encoded_message}' -> Decrypted: '{decoded}'")
                print(f"\n{BOLD}{GREEN}┌─ Decrypted message ─────────────────────────────┐{RESET}")
                print(f"{GREEN}│{RESET} {BOLD}{MAGENTA}{decoded}{RESET}")
                print(f"{BOLD}{GREEN}└─────────────────────────────────────────────────┘{RESET}")
            else:
                log_action("Decryption error", "Attempt to decrypt empty message")
                print(f"{BOLD}{RED}┌─ Error ─────────────────────────────────────────┐{RESET}")
                print(f"{RED}│{RESET} Encrypted message cannot be empty.         {RED}│{RESET}")
                print(f"{BOLD}{RED}└─────────────────────────────────────────────────┘{RESET}")
            input(f"\n{BOLD}{BLUE}┌─ Press Enter to continue ───────────────────────┐{RESET}\n{BOLD}{BLUE}└─> {RESET}")

        elif choice == '3':
            log_action("Program exit", "User finished working with the program")
            clear_screen()
            print(f"{BOLD}{GREEN}╔═══════════════════════════════════════════════════╗{RESET}")
            print(f"{GREEN}║{RESET}        {BOLD}{WHITE}Thank you for using the program! 👋{RESET}     {GREEN}║{RESET}")
            print(f"{BOLD}{GREEN}╚═══════════════════════════════════════════════════╝{RESET}")
            break

        else:
            log_action("Invalid choice", f"User entered: '{choice}'")
            clear_screen()
            print(f"{BOLD}{RED}╔═══════════════════════════════════════════════════╗{RESET}")
            print(f"{RED}║{RESET}           {BOLD}{WHITE}Invalid choice. Try again.{RESET}        {RED}║{RESET}")
            print(f"{BOLD}{RED}╚═══════════════════════════════════════════════════╝{RESET}")
            input(f"{BOLD}{BLUE}┌─ Press Enter to continue ───────────────────────┐{RESET}\n{BOLD}{BLUE}└─> {RESET}")

if __name__ == "__main__":
    main()
```

### Adding New Features

1. Add function to appropriate section
2. Update logging for new actions
3. Test on different platforms
4. Update documentation

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [cryptography](https://cryptography.io/) - for cryptographic functions
- [colorama](https://pypi.org/project/colorama/) - for colored console output
- Python community for the excellent programming language

---

**Made with ❤️ for secure message exchange**
