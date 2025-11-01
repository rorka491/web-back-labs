from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "basemodel" (
    "id" SERIAL NOT NULL PRIMARY KEY
);
CREATE TABLE IF NOT EXISTS "user" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "username" VARCHAR(255) NOT NULL,
    "password" VARCHAR(255) NOT NULL
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """


MODELS_STATE = (
    "eJztlWFP2zAQhv9KlU9MYhN0ZaB9aytN2zSKxMY0CaHISa6JVccO9mWAUP87Pidp0qSNQE"
    "KiCL657722756cr/deqiIQ5tOEGTilpfd1cO9JloJddIP7A49lWR0iAVkgnDuwtnRlCwxq"
    "FqINzJkwYKUITKh5hlxJq8pcCBJVaI1cxrWUS36dg48qBkxA28DllZW5jOAWTPUzW/hzDi"
    "JaS5hHdLfTfbzLnPZD4jdnpNsCP1QiT2Vtzu4wUXLl5hJJjUGCZgh0POqc0qfsylKriopM"
    "a0uRYmNPBHOWC2yU+0gGoZLEz2ZjXIEx3fJxeDg6Hp18/jI6sRaXyUo5Xhbl1bUXGx2B2R"
    "9v6eIMWeFYYZwvWkLAwsUN05Hfiaih2ubthtJh2laYZLGDQzVSOmV7XRj3kTtt5/Tejssr"
    "x3uz7Xyz1dzoq7l1h940YXozvuaeFkSbehtihayPYiXUGOvWeSaOKbv1BcgYE4J3dNRD7e"
    "/4fPp9fL5nXR+oGmXbuejxWRkaFjFCW6PMmDE3Sm9oxO0om3veOModGYBj0DxMNo3AMtI7"
    "BFnteR+Dr2gM/gdtKKUnPN3Gljf+cptDkJ7GEyCW9tcJ8PDg4BEArWsrQBdbB2hvRCje4D"
    "rEn7/PZpshNra0QF5IW+BlxEPcHwhu8Go3sfZQpKop6dSYa9GEt3c6/tfmOv11NnEUlMFY"
    "u1PcAZOX/ntZPgChIWok"
)
