from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "basemodel";
        CREATE UNIQUE INDEX IF NOT EXISTS "uid_user_login_a18ea9" ON "user" ("login");"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "user" DROP CONSTRAINT IF EXISTS "user_login_key";
        DROP INDEX IF EXISTS "uid_user_login_a18ea9";"""


MODELS_STATE = (
    "eJztlW9r2zAQxr9K8KsOutFm6Vr2Lg2MbWwpdOsYlGIU+2KLyJIrndeWku9enWxHivOHBl"
    "q20r1znnvOuvtF57uPCpWCMO8uDOjoY+8+kqwA+7Ck7/ciVpZeJQHZRDhj1TomBjVL0GpT"
    "JgxYKQWTaF4iV9KqshKCRJVYI5eZlyrJryuIUWWAuavj8srKXKZwC6b9Wc7iKQeRLpXJUz"
    "rb6THelU77IvGTM9JpkzhRoiqkN5d3mCu5cHOJpGYgQTMEej3qisqn6pou247qSr2lLjHI"
    "SWHKKoFBu49kkChJ/Gw1xjWY0Slv+4eD48HJ+w+DE2txlSyU43ndnu+9TnQExj+juYszZL"
    "XDYfTc6F9zzyv0RjnT6/GFOR2ItvQuxBbZNoqt4DH6q/NEHAt2GwuQGeYE7+hoC7Vfw/PR"
    "5+H5nnW9oW6Uvc71HR83oX4dI7QepVAZl7twXCQ8DcRnv4rPj7BkxtwovWaWN1MMc175ba"
    "Sv43QWzDkJE5bMbphO45WI6qtN3tVQ0S+6CpMsc3ioSeqg2RVD0DzJ122RJrJ1jzDv+b9J"
    "XtAm+QPaUEk7jG6Q8sonN/wI0mjsALGxv0yAhwcHjwBoXRsButgyQHsiQj2DyxC//jgbr4"
    "cYpHRAXkjb4GXKE9zvCW7w6t/EuoUidU1FF8ZcixDe3vfh7y7X0bezU0dBGcy0e4t7wenf"
    "Xi/zB/zSBbM="
)
