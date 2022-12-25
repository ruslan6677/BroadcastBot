import os

BOT_TOKEN = os.environ.get("BOT_TOKEN", "5644214136:AAEtonzQn7-yr4XphA86zKgXNRSEEU-T52w")
API_ID = int(os.environ.get("API_ID", "10300036"))
API_HASH = os.environ.get("API_HASH", "79c295e05c970ddd724f0762ba275104")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001844421317"))
AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "2124305832").split())
DB_URL = os.environ.get("DB_URL", "mongodb+srv://Ruslan:Ruslan@cluster0.ieadn36.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DB_NAME", "Cluster0")
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
