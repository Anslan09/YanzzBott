class Config(object):
    LOGGER = True

  # Get this value from my.telegram.org/apps
    API_ID = 28014393
    API_HASH = "4be13450374f7b2b1b1781d3c82516c4"

    CASH_API_KEY = "JGI67Y9D1LGXYFSB"  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = "postgres://xhnliewf:3VHSFPaicnDlLZ6RT20aXxwTeXr4ohHq@floppy.db.elephantsql.com/xhnliewf"  # A sql database url from elephantsql.com

    EVENT_LOGS = (-1001538760013)  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb+srv://nana:nana@cluster0.nelglmz.mongodb.net/?retryWrites=true&w=majority"

  # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://te.legra.ph/file/c8050140d444e13884b18.jpg"

    SUPPORT_CHAT = "dlksyz"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "5838506109:AAH0lyUPBKrYXFRI80fSE2D5weYlf3d7vl8"

    TIME_API_KEY = "7WMA3YLV6OEB"  # Get this value from https://timezonedb.com/api

    OWNER_ID = 1885301683  # User id of your telegram account (Must be integer)

  # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = [1885301683]  # User id of sudo users
    DEV_USERS = [1885301683]  # User id of dev users
    DEMONS = [1885301683]  # User id of support users
    TIGERS = [1885301683]  # User id of tiger users
    WOLVES = [1885301683]  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = (8)

class Production(Config):
    LOGGER = True

class Development(Config):
    LOGGER = True
