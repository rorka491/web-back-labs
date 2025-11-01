from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "user" ADD "login" VARCHAR(255) NOT NULL;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "user" DROP COLUMN "login";"""


MODELS_STATE = (
    "eJztlW9r2zAQxr9K8KsOutFm6Vr2LgmMbawpdOsYlGJkW7FFZMmVzmtLyXevTv4jx05MA4"
    "WmNO+U556T7n4+RY9eKiPK9acJ0fQcl97XwaMnSErNohs8HHgky1wIBSABt+7A2NLaFmhQ"
    "JAQTmBOuqZEiqkPFMmBSGFXknKMoQ2NkInZSLthtTn2QMYWEKhO4vjEyExG9p7r6mS38Oa"
    "M8WimYRXi21X14yKz2Q8A3a8TTAj+UPE+FM2cPkEhRu5kAVGMqqCJAcXtQOZaP1ZWtVh0V"
    "lTpLUWIjJ6JzknNotPtMBqEUyM9Uo22DMZ7ycXg8Oh2dff4yOjMWW0mtnC6L9lzvRaIlMP"
    "vjLW2cACkcNcb5oiUEJFzcERX5nYgcyk3ebigdpm2FCBJbONgjllOO15W2H7kzdlbvnbi8"
    "cuyHbeeHzXHDr2bXHXrThKj1+Jo5LYim9DbEClkfxUpwGN3ovBDHlNz7nIoYEoR3ctJD7e"
    "/4cvp9fHlgXB+wG2nGuZjxWRkaFjFE61ByGTOxDcc6YQ+xhpgRre+kWnObN3Ns5rxzlDvy"
    "ioypYmGy7h0pI70vCXGe/Vvyht6S/1RpLGmLq9tIeec3t/kniFdjC4il/W0CPD46egZA49"
    "oI0MZWAZoTgRZ3cBXiz98Xs/UQGyktkFfCNHgdsRAOB5xpuNlNrD0UsWssOtX6ljfhHZyP"
    "/7W5Tn9dTCwFqSFWdhe7weS1n5flE1fI0RQ="
)
