# 💰 Financial Planner Bot

A personal financial management system built with Python, using a Telegram Bot for transaction input and Google Sheets as a lightweight database.

This project is designed with clean architecture principles, asynchronous processing, and modular structure to ensure scalability and maintainability.

---

## 🚀 Features

- 📲 Input transactions via Telegram Bot
- 📊 Store data in Google Sheets
- 🧠 Structured data model:
  - Date
  - Category
  - Description
  - Amount
  - Payment Instrument
  - Optional Notes
- ⚡ Async processing (non-blocking)
- 🧩 Clean architecture (Handler, Service, Repository)
- 🔐 Environment-based configuration
- 📉 Ready for future financial analysis (monthly summary, cashflow insights)

---

## 🏗️ Architecture

Telegram Bot → Handler Layer → Service Layer → Repository Layer → Google Sheets

- **Handler**: Handles Telegram interaction
- **Service**: Business logic, validation, transformation
- **Repository**: Data access (Google Sheets)

---

## 📁 Project Structure
```txt
financial-bot/
│
├── app/
│ ├── handler/
│ ├── service/
│ ├── repository/
│ ├── models/
│ └── core/
│
├── .env
├── main.py
└── requirements.txt
```

---

## ⚙️ Tech Stack

- Python 3.10+
- python-telegram-bot (async v20+)
- gspread-asyncio
- python-dotenv
- Google Sheets API

---

## 🔑 Environment Variables

Create a `.env` file:
```txt
BOT_TOKEN=your_telegram_bot_token
GOOGLE_CREDENTIALS=path_to_credentials.json
SPREADSHEET_NAME=your_sheet_name
```

---

## 📥 Installation

```bash
git clone https://github.com/your-username/financial-bot.git
```
```bash
cd financial-bot
```
```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Bot

```bash
python main.py
```

---

## 💬 Command Usage

Format:
```
/add <kategori> <nominal> <deskripsi> <instrumen>
```

Example command:
```
/add makan 15000 nasi_padang cash
```

---

## 🛡️ Validation Rules

- Nominal must be numeric
- Category must be predefined
- Invalid input will return error message

---

## ⚠️ Error Handling

- Retry mechanism for Google API failures
- Structured logging for debugging
- User feedback on failure/success

---

## 📈 Future Improvements

- Monthly financial summary
- Cashflow analysis
- Budget tracking
- Multi-user support
- Database migration (PostgreSQL / SQLite)

---

## 📌 Limitations

- Google Sheets used as database (not suitable for large scale)
- No authentication layer (single user assumption)
- Input parsing still command-based

---

## 🧠 Philosophy

This project is built as a practical financial control system, not just a coding exercise.

The goal is to create a reliable tool that helps track and manage real financial behavior consistently.

---

## 📜 License

MIT License
