from database import Database
from writeAJson import writeAJson

db = Database(database="mercado", collection="produtos")
db.resetDatabase()