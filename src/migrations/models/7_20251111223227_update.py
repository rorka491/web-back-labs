from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "human" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(255) NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "human";"""


MODELS_STATE = (
    "eJztmVtP4kAUgP8K6RObuEZZb9m3griyCmywukZjmqEdysTpTG2nIjH8952Z3kvbpYlEiD"
    "wB59Ke83XmnNPhXbGpCbG3r7oMGRgqPxvvCgG2+JJX7TUU4DiJQggYGEsnBQRGUgjGHnOB"
    "wbh8ArAHuciEnuEihyFKuJT4GAshNbghIlYi8gl68aHOqAXZFLpc8fjExYiY8I1fPPzpPO"
    "sTBLGZiRaZ4t5SrrO5I2U9wi6kobjbWDco9m2SGDtzNqUktkaECakFCXQBg+LyzPVF+CK6"
    "MNMooyDSxCQIMeVjwgnwMUuluyIDgxLBj0fjyQQtcZfvrcOj06OzHydHZ9xERhJLThdBek"
    "nugaMkMNCUhdQDBgILiTHhxhALHm4WXWcK3GJ2sUMOHw86jy+CVcUvEiQAk0XzQQRt8KZj"
    "SCw2FdiOjyt43amjzqU6anKrbyIbyhdysMIHoaoV6ATUFET4xpYZalxawjC03xaEFcS07r"
    "0mgrY97wWnQTX76r1kaM9DzfVw8CsyT4HtXA/bOZ7I0yfglbqIFSzNNqUYAlKys7OeOcBj"
    "7rouwnVr3eqI28PhdQZxu5dneNtvd0fNQ8mbG4nsU7s/AQt8zsPVaxXLjM//a+ZmrNiPKJ"
    "ui10yeC6tmwGQZ4gV1IbLIFZxLlj0eEyBG0VIMu+utBzd7zyfSpLe5YBZ34Ozy4AnytGCw"
    "/DrqTUc97yoS5BgYzzPgmnqGqNDQFs1JYttlld2y8xJAgCUJiDxE1CHaS5+riiaaQFE5z0"
    "xjk90ws2G7smqYkZ81ZpnIflv68JpGmaVC9zkbVtbCgv0a1cjy7epzi927x9ZtV/HY6m7Z"
    "tM8X37bpwQ5TC5E6HGOHj4G49qW4foQO8LwZdQv2cjnFtM8XX401mkhqjg7PjbyC17zQ9e"
    "JqBDGQSZZO0akzqs3jXTZIL9bZS++QCWlRMw0Uld30VZjs2unWtdOvdpR3eHCwQuniVqWl"
    "S+qyXWCC+PVrziRpn+1EuZaG6juYAhOaOig4HD3nNBiyYcmUl3XNQTVD3/3oy4YidiEwhw"
    "TPo4JfTljr9bs3mtr/kznnO1e1rtC0MseokbR5knsY8UUaf3vaZUP8bDwMB11JkHrMcuUd"
    "EzvtQRExAZ9RndCZDsxU1YukEZhNeUtUoYuMaVFrCzWVvQ0kNrvetkW97ZW/4Icj4KpVOe"
    "WyK8rJxM23Rg2Iofl2AlzLgMDvyCAp6Gi/b4aDYogplxzIW8ITfDSRwfYaGHnsaTOxVlAU"
    "WVf//5f/qy/XjcQF2p99CLn4BzIojfc="
)
