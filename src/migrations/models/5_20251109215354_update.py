from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "articles" ADD "is_favorite" BOOL NOT NULL DEFAULT False;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "articles" DROP COLUMN "is_favorite";"""


MODELS_STATE = (
    "eJztmF1P2zAUhv8KyhWT2AQdDLS7tIONAa1UyoSEUOQmbmrh2MF2oBXqf9+xkzZOmnSt1E"
    "6t4C49H8k5T4/9OnlzIh5gKr+4QhGfYuf73pvDUKQvyq6DPQfFce7QBoX6JslBaZAxor5U"
    "AvkK7ANEJQZTgKUvSKwIZ2BlCaXayH0IJCzMTQkjzwn2FA+xGmIBjodHMBMW4BHcPPsZP3"
    "kDgmlQqJYE+tnG7qlxbGyXTF2YQP20vudzmkQsD47HasjZLJowpa0hZlgghfXtlUh0+bq6"
    "rNNpR2mleUhaopUT4AFKqLLaXZKBz5nmB9VI02Con/K5cXR8enz29dvxGYSYSmaW00naXt"
    "57mmgItHvOxPiRQmmEwZhzU0Slf24RXWuIRDW7WUIJHxRdxjeFtYjf1JADzIdmTQQjNPIo"
    "ZqEaamwnJwt4/XG7rV9udx+iPuluOAxyOuHtzNVIfRqqBRGP1DzDHlhrGGbxu4JwAbHe+X"
    "1PFx1J+UxtUPs37r1hGI0zz3Wn/XMaboFtXXeaJZ5EegP0wgVRFaPZ5JxixGpWdjGzBLgP"
    "qZsivOpetzziZqdzXUDcvCwzvLtpnnf3jwxvCNLdW6s/B4sS4CG8lTbLQs6/98ztmNh1bJ"
    "taawZPlbtmymQe4gUXmITsCo8Ny0uoCTG/ahQzdb2TeLvXfG7NtU2g15kCF8cDGoS2cDp+"
    "Lfe25f44dwzIPvKfXpEIvAJR7eENXrLMYuddUSMqWxBDoSGg+9BV22grDjRT5PWnmQQiPo"
    "4yO3eU0X+buV7hNGPn7Ioa/4cDDeUhYatwnCWsB+LGR3HzCGMk5SsXFWu5nqKd886ncU58"
    "60XEkuXsNVRWnBqz1IurLqbINFkrytYr7/bxrtPlySa11MWC+MMqNc08C/UU5TEfgrpDgv"
    "oCx6BsoSy7g1kp73wDK7x2wdJYAWIWvpsAjw4PlwAIUbUAja8IEJ6oMKv4xvL7ttOuhmil"
    "lEDeMWjwISC+OtijRKrH7cS6gKLuevFHl/L3FU2BSxUKcxdzg+ZqKrt+eZn8BfcSMvM="
)
