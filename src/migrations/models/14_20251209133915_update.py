from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "gifts" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "url_photo" VARCHAR(3000) NOT NULL,
    "congarts" VARCHAR(255) NOT NULL,
    "is_opened" BOOL NOT NULL DEFAULT False
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "gifts";"""


MODELS_STATE = (
    "eJztm21P2zoUgP9K1U9caZtoYRu639pSRjdoJyi706YpchMntZrYmeMA1cR/v7bz5qRJ1j"
    "AKyZpPlPOS2E99fI5f+qvrEAPa3psBZUi3Yfffzq8uBo74kFW96nSB6yYKIWBgIZ26IDCS"
    "QrDwGAU643IT2B7kIgN6OkUuQwRzKfZtWwiJzg0RthKRj9FPH2qMWJAtIeWK7z+4GGED3v"
    "OHh/+6K81E0DZSrUWGeLeUa2ztStkEszNpKN620HRi+w5OjN01WxIcWyPMhNSCGFLAoHg8"
    "o75ovmhd2NOoR0FLE5OgiYqPAU3g20zp7pYMdIIFP94aT3bQEm953e8dvz8+OXp3fMJNZE"
    "tiyfuHoHtJ3wNHSWA67z5IPWAgsJAYE24MseDLTaMbLQHNZxc7ZPDxRmfxRbDK+EWCBGAy"
    "aJ6IoAPuNRtiiy0FtrdvS3h9GVyNzgdXB9zqH9EbwgdyMMKnoaof6ARUBSK8Z5sM51xawD"
    "C0bwrCEmLz8de5aLTjeT9tFdTB5eCrZOisQ83FbPohMlfAji5mwwxP5GkmuCUUsZyhOSTE"
    "hgAXRHbaMwN4wV13RbjqXLc94uFsdpFCPJxkGd5cDsdXBz3JmxuJ3ivRnwLr+gsb6dWxJn"
    "6PgxrOi38fU+BzHFSrlIBSPr/PQ/WYBZ4iFYn8ba5yM1HAZBPiGaEQWfgTXEuWE94mgPW8"
    "8A4rlhsP1nseTaRJXFBwF1c16eHBO8i7BYPhNxpcjwan464EuQD66g5QQ0sRFRrSJxlJbL"
    "upcvpOVgIwsCQB0Q/R6hDtGbKdbk6RKOWlFaLJLdrysC0PaxeTz1EeCiYa9StzDH1alDHK"
    "NQQ5KaIwkiPzfUqxKi61GRUGX8atoePv8PBwmwHIzYpHoFTmlC0vk34/IJPlpV8pL02/Fr"
    "do02/j0q9Pbc1dEkaqRG/KqZmxe7Rd7B6Vxe5RGLvqfMhfagEaRMK2OFWfZtLcSSZGnuZj"
    "19dXMCe2f7eZoHq2ezS1yS/nPlflJZhAUZphlrFJm2EalGHk3wqzYWS/5zNhTQJ2ZppIzz"
    "22CzWlIUukTVsWNi5on3lX5jFb97WM2kz9wkuNlWhF5fJFcWyrlzRWl4bTzpZRHdvv6xYN"
    "gxhgVu34KOXzKHAvENK7PT0KkDzf6dHzA9z28Cg1OOp0eCTJ5pQqEfHiQsXnFm2Z0rgyRX"
    "xtVdcXqs+erzHULGETC1Xawo8dngbizofi7hG6wPPuCM2J5WKKqs+ej8YKK17lTkd4LzRn"
    "w3UYup59uoI2KDhq2ryDWj/eRXk5NfjCpfYfckgW9Y2pTh52WVF8QQYkeSVFoCitKW6FSV"
    "tUNK6o2LcbKb2tTsJ6JQdhvc1zMBPx51eszFSfZqLcSVnhuzYBBjQ0kLP6POU0GHJgQa2b"
    "ds1ANULfN9GHmiKmEBgzbK+TtFd4V3xyOb6eDy4/p/aaTgfzsdD0pXSdkR68y3wZ8UM6/0"
    "3m5x3xb+fbbDqWBInHLCrfmNjNv3VFm4DPiIbJnQYMZdaLpBGYumzsDyBF+jIvtYWa0twG"
    "Eps2tzUot91C6lW8qqW4tJNysu7goVEBYmjeTIA7KRD4GxnM20/9eD2bFt6TiVwyIG8w7+"
    "B3A+nsVcdGHvtRT6wlFEWvU0lr41dO2R80ZbKReMDwpc+NH/4HEXKBWQ=="
)
