from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "articles" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "title" VARCHAR(255) NOT NULL,
    "text" TEXT NOT NULL,
    "author_id" INT NOT NULL REFERENCES "users" ("id") ON DELETE CASCADE
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "articles";"""


MODELS_STATE = (
    "eJztmNFu2jAUhl8F5aqTuqlldK12F1jZunYgUTpVqqrIJCZYOHZqOwNU8e6znZA4IclAgg"
    "nU3sF/zknO+bD9k7xaAfUg5p9sJpCLofW18WoREKgPxdBpwwJhmAWUIMBIF1kgTtIiGHHB"
    "gCukPgaYQyl5kLsMhQJRIlUSYaxE6spERPxMigh6iaAjqA/FBDIZeHqWMiIenMuLJ1/DqT"
    "NGEHu5bpGn7q11RyxCrd0Q0dWJ6m4jx6U4CkiWHC7EhJI0GxGhVB8SyICA6vKCRap91V0y"
    "6WqiuNMsJW7RqPHgGERYGONuyMClRPGT3XA9oK/u8rF53rpsXX3+0rqSKbqTVLlcxuNls8"
    "eFmkBvaC11HAgQZ2iMGTeBRPzj5tF1JoCVs0sLCvhk00V8K1h1/FZCBjBbNDsiGIC5gyHx"
    "xURhu7io4fXbHnR+2IMTmfVBTUPlQo5XeC8JNeOYgmpAhHOxznAo1QqGSf6xIKwhNrx+HK"
    "qmA85fsAnq5Jf9qBkGiyRy1+99X6UbYDt3/XaBJ4gkF+ZstadzNf/e2ocBdhe7Wx2J42np"
    "5o6ZrEPsUgaRT27hQrO8kT0B4pbt6sQEHjg87KWZqdkRzMAsNYr88pADyrGgiI86+75jf7"
    "u2NMgRcKczwDwnR1RFaJMWlDR3PRQ0g6ICCPA1ATWH6tpEW+K7K+TVphvJjHfHPTrHVT+b"
    "/ryF6Zo1x2Ia/8F3MfUR2YZjWrAbiHtfivtHGALOZ5SV7OVqimbNG1+Na+ZbbSKGLSdPS3"
    "wdejsp7d4OIAZ6yEpTNp7MDo93lS8v9+mlNmTInZS5aRKp9VOQ5bwb6hEZ6h/5NyjZKJue"
    "YEbJGz/Aco9dcmtsATFJP06A52dnGwCUWZUAdSwPUN5RQFLyKuDnfb9XDtEoKYB8IHLAJw"
    "+54rSBERfPh4m1hqKauv7dQPE1gKJAufCZvoq+QHs7l929vSz/AnYexHU="
)
