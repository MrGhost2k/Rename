# Don't Remove Credit @MaviMods
# Subscribe YouTube Channel For Amazing Bot @MaviMods
# Ask Doubt on telegram @MaviMods


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "16406981")

API_HASH = os.environ.get("API_HASH", "a1e673b44dca859b4d408884d7de7c49")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6590505743:AAEbOPDqGBhgmRhifStM2LtTQurDKTsLnvY") 

FORCE_SUB = os.environ.get("FORCE_SUB", "-1001913988417") 

             # Don't Remove Credit @MaviMods
             # Subscribe YouTube Channel For Amazing Bot @MaviMods
             # Ask Doubt on telegram @MaviMods

DB_NAME = os.environ.get("DB_NAME", "ab")     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://ab:ab@cluster0.xgqrenn.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/119729ea3cdce4fefb6a1.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '1146283167').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @MaviMods
# Subscribe YouTube Channel For Amazing Bot @MaviMods
# Ask Doubt on telegram @MaviMods
