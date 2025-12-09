from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "offices" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "title" VARCHAR(255),
    "is_booking" BOOL NOT NULL DEFAULT False,
    "price" INT NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "offices";"""


MODELS_STATE = (
    "eJztmltP4kAUgP8K6RObuBtlvWXfCuLKKrDR6hqNaYZ2KBOnM7WdisT433dmei9tlyay0s"
    "gTcC7tOR8z55yhvCo2NSH2vqkuQwaGyo/Wq0KALd7kVTstBThOohACBibSSQGBkRSCicdc"
    "YDAunwLsQS4yoWe4yGGIEi4lPsZCSA1uiIiViHyCnnyoM2pBNoMuV9w/cDEiJnzhFw8/Oo"
    "/6FEFsZqJFpri3lOts4UjZgLBTaSjuNtENin2bJMbOgs0oia0RYUJqQQJdwKC4PHN9Eb6I"
    "Lsw0yiiINDEJQkz5mHAKfMxS6a7IwKBE8OPReDJBS9zla2dv/2j/+Pvh/jE3kZHEkqO3IL"
    "0k98BREhhpypvUAwYCC4kx4cYQC77cLLreDLjF7GKHHD4edB5fBKuKXyRIACaL5p0I2uBF"
    "x5BYbCawHRxU8LpRL3tn6mWbW30R2VC+kIMVPgpVnUAnoKYgwhe2zFDj0hKGoX1TEFYQ0/"
    "q3mgja9rwnnAbVHqq3kqG9CDUX49HPyDwFtncx7uZ4Ik+fgmfqIlawNLuUYghIyc7OeuYA"
    "T7jrugjXrXWrI+6OxxcZxN1BnuH1sNu/bO9J3txIZJ/a/Rmwjj/ByKiPNfHbQs1CBT7n4e"
    "q1OlDG59+NaDPKwHv0ItHAp4+FrShgsgzxlLoQWeQcLiTLAY8JEKNof4cjy7UHN7uQJtJk"
    "YHDBPB5rssuDJ8jTgsHy66lXPfWkr0iQE2A8zoFr6hmiQkM7NCeJbZdVdsfOSwABliQg8h"
    "BRh2jPfK5SCsbEQFE5JM5ik+2EuGG7smpClK81BsTIvinDzZrmw6VC9zEbdjydIqPwYBdq"
    "KrcslTbbY13jNu1/PtaFdJq/a3PDMp9tH0UUtafllON2XM5iddyw7Ky4q2P7Tz0mf0z3kJ"
    "N0Qe+IJuzyzuFzi23faFzfEF9b3YEv7fPJh750ncPUQqQOx9jhfSCufSmuH6EDPG9O3YK9"
    "XE4x7fPJV2ONJpL6FSZ8lOMVDD2h6+n5JcRAJrkMefmx0ebxLvsZ5m2dvfQGmZAWNdNAUd"
    "lNn4XJtp02rp1+tqdre7u7K5QublVauqQu2wWmiF+/5kyS9mkmyrU0VN/BFJjQ1EHB88oT"
    "ToMhG5ZMeVnXHFQz9P0WvdlQxC4E5pjgRVTwywlrg2H/SlOHvzPH3hNV6wtNJ/NkM5K2D3"
    "NfRnyR1p+BdtYSH1t341FfEqQes1x5x8ROu1NETMBnVCd0rgMzVfUiaQRmU06JKuRH9FlR"
    "aws1lb0NJDbb3tag3vbMD/jhCLhqVU65bItyMnHzrVEDYmjeTIBrGRD4HRkkBR3t19V4VA"
    "wx5ZIDeU14gvcmMthOCyOPPWwm1gqKIutM01r6S07+3ze5biQu0P3oHyHf/gIj1fXc"
)
