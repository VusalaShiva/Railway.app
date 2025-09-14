# Railway System

This is a console-based railway ticketing system in Python using a remote MySQL database.

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/VusalaShiva/Railway.app.git
   cd railway-system
   ```
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Create a `.env` file (see below).
4. Run the project:
   ```
   python main.py
   ```

## .env Example
```
DB_HOST=containers-us-west-54.railway.app
DB_USER=root
DB_PASSWORD=yourpassword
DB_NAME=railway
```

## Notes
- Do NOT push your `.env` file to GitHub.
- The project will use the remote MySQL database specified in `.env`.

