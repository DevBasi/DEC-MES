# DEC MES Encryption Tool

### _Beautiful console application for message encryption and decryption_

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Cryptography](https://img.shields.io/badge/Cryptography-AES--256-green.svg)](https://cryptography.io/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

English | [Русский](README.md)

DEC MES is a beautiful console application for encrypting and decrypting messages using modern cryptographic algorithms and a stylish interface.


### 🚀 Quick Start

```bash
# Install dependencies
pip install cryptography colorama

# Run the program
python decompilermessages.py
```


## ✨ Features

- 🔐 **Strong encryption** - AES-256 via Fernet (cryptography library)
- 🎨 **Beautiful interface** - colored output with Linux-style frames
- 🌍 **UTF-8 support** - encrypt messages in any language
- 📝 **Logging** - all actions are logged to a file with timestamp
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
dec-mes/
├── decompilermessages.py    # Main script
├── secret.key              # Encryption key (created automatically)
├── decmes_log.txt          # All actions log
└── README.md              # Documentation
```

## 🛠 Технические детали

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

## 🚀 Установка и запуск

### System Requirements
- Python 3.8 or higher
- pip for dependency installation

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/DevBasi/DEC-MES.git
   cd dec-mes
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

## 📄 Примеры использования

### Message Encryption
```
┌─ Enter message to encrypt ───────────────────────┐
└─> Hello World!

┌─ Encrypted message ──────────────────────────────┐
│ 龘龙龚龛龜龝龞龟龠龡龢龣龤龥龦龧龨龩龪龫龬龭龮龯龰
└─────────────────────────────────────────────────┘
```

### Message Decryption
```
┌─ Enter encrypted message ────────────────────────┐
└─> 龘龙龚龛龜龝龞龟龠龡龢龣龤龥龦龧龨龩龪龫龬龭龮龯龰

┌─ Decrypted message ──────────────────────────────┐
│ Hello World!
└─────────────────────────────────────────────────┘
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

### Adding New Features

1. Add function to appropriate section
2. Update logging for new actions
3. Test on different platforms
4. Update documentation

**Made with ❤️ for secure message exchange**
