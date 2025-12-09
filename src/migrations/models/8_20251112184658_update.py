from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "articles" ADD "is_public" BOOL NOT NULL DEFAULT False;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "articles" DROP COLUMN "is_public";"""


MODELS_STATE = (
    "eJztmVtP4kAUgP8K6RObuEZZb9m3griyCmywukZjmqEdysTpTG2nIjH8952Z3kvbpYlEiD"
    "wB59Ke83XmnNPhXbGpCbG3r7oMGRgqPxvvCgG2+JJX7TUU4DiJQggYGEsnBQRGUgjGHnOB"
    "wbh8ArAHuciEnuEihyFKuJT4GAshNbghIlYi8gl68aHOqAXZFLpc8fjExYiY8I1fPPzpPO"
    "sTBLGZiRaZ4t5SrrO5I2U9wi6kobjbWDco9m2SGDtzNqUktkaECakFCXQBg+LyzPVF+CK6"
    "MNMooyDSxCQIMeVjwgnwMUuluyIDgxLBj0fjyQQtcZfvrcOj06OzHydHZ9xERhJLThdBek"
    "nugaMkMNCUhdQDBgILiTHhxhALHm4WXWcK3GJ2sUMOHw86jy+CVcUvEiQAk0XzQQRt8KZj"
    "SCw2FdiOjyt43amjzqU6anKrbyIbyhdysMIHoaoV6ATUFET4xpYZalxawjC03xaEFcS07r"
    "0mgrY97wWnQTX76r1kaM9DzfVw8CsyT4HtXA/bOZ7I0yfglbqIFSzNNqUYAlKys7OeOcBj"
    "7rouwnVr3eqI28PhdQZxu5dneNtvd0fNQ8mbG4nsU7s/A9bxxxgZ9bEmfjuoWajA5zxcvV"
    "YHyvj8vxFtRhn4iF4kGvjkubAVBUyWIV5QFyKLXMG5ZNnjMQFiFO3vcGS59eBmF9JEmgwM"
    "LpjFY012efAEeVowWH4d9aajnncVCXIMjOcZcE09Q1RoaIvmJLHtsspu2XkJIMCSBEQeIu"
    "oQ7aXPVUrBmBgoKofEaWyymxA3bFdWTYjys8aAGNlvy3CzpvlwqdB9zoaVtbBgv0Y1sny7"
    "+txi90K3ddtVPLa6Wzbt88W3bXqww9RCpA7H2OFjIK59Ka4foQM8b0bdgr1cTjHt88VXY4"
    "0mkpqjw8M4r+AlL3S9uBpBDGSSpVN06uBv83iXDdKLdfbSO2RCWtRMA0VlN30VJrt2unXt"
    "9Kudjx4eHKxQurhVaemSumwXmCB+/ZozSdpnO1GupaH6DqbAhKYOCk6czzkNhmxYMuVlXX"
    "NQzdB3P/qyoYhdCMwhwfOo4JcT1nr97o2m9v9kzvnOVa0rNK3M2XQkbZ7kHkZ8kcbfnnbZ"
    "ED8bD8NBVxKkHrNcecfETntQREzAZ1QndKYDM1X1ImkEZlPeElXoImNa1NpCTWVvA4nNrr"
    "dtUW975S/44Qi4alVOueyKcjJx861RA2Jovp0A1zIg8DsySAo62u+b4aAYYsolB/KW8AQf"
    "TWSwvQZGHnvaTKwVFEXW1X+q5v8/zXUjcYH2Zx9CLv4Bn9D6pA=="
)
