from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "gifts" RENAME COLUMN "congarts" TO "congrats";"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "gifts" RENAME COLUMN "congrats" TO "congarts";"""


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
    "do02/j0q9Pbc1dEkaqRG/KqZmxe7Rd7B6Vxe5RGLvqfMhfavF+e1Vwqj7NpLmTTIw8zceu"
    "r69gTmz/bjNB9Wz3aGqTX859rspLMIGiNMMsY5M2wzQow8i/FWbDyH7PZ8KaBOzMNJGee2"
    "wXakpDlkibtixsXNA+867MY7buaxm1mfqFlxor0YrK5Yvi2FYvaawuDaedLaM6tt/XLRoG"
    "McCs2vFRyudR4F4gpHd7ehQgeb7To+cHuO3hUWpw1OnwSJLNKVUi4sWFis8t2jKlcWWK+N"
    "qqri9Unz1fY6hZwiYWqrSFHzs8DcSdD8XdI3SB590RmhPLxRRVnz0fjRVWvMqdjvBeaM6G"
    "6zB0Pft0BW1QcNS0eQe1fryL8nJq8IVL7T/kkCzqG1OdPOyyoviCDEjySopAUVpT3AqTtq"
    "hoXFGxbzdSeludhPVKDsJ6m+dgJuLPr1iZqT7NRLmTssJ3bQIMaGggZ/V5ymkw5MCCWjft"
    "moFqhL5vog81RUwhMGbYXidpr/Cu+ORyfD0fXH5O7TWdDuZjoelL6TojPXiX+TLih3T+m8"
    "zPO+LfzrfZdCwJEo9ZVL4xsZt/64o2AZ8RDZM7DRjKrBdJIzB12dgfQIr0ZV5qCzWluQ0k"
    "Nm1ua1Buu4XUq3hVS3FpJ+Vk3cFDowLE0LyZAHdSIPA3Mpi3n/rxejYtvCcTuWRA3mDewe"
    "8G0tmrjo089qOeWEsoil6nktbGr5yyP2jKZCPxgOFLnxs//A8RlIFZ"
)
