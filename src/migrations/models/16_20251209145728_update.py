from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "gifts" RENAME COLUMN "is_unpucked" TO "is_opened";"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "gifts" RENAME COLUMN "is_opened" TO "is_unpucked";"""


MODELS_STATE = (
    "eJztm21P2zoUgP9K1U9caXeihb3ofktLGb2DdoKyO22aIjdxUgvHzhwHqCb++7Wd9zTJGk"
    "YhWfOJcl4Sn6c+Pid2+rPvUBNi77XGODIw7P/T+9knwJEf8qpXvT5w3UQhBRwslVMfBEZK"
    "CJYeZ8DgQm4B7EEhMqFnMORyRImQEh9jKaSGMETETkQ+QT98qHNqQ76CTCi+fRdiREx4Ly"
    "4e/uve6BaC2MyMFpny3kqu87WrZFPCT5WhvNtSNyj2HZIYu2u+oiS2RoRLqQ0JZIBDeXnO"
    "fDl8Obow0iiiYKSJSTDElI8JLeBjngp3SwYGJZKfGI2nArTlXf4eDo7fHb8/env8Xpiokc"
    "SSdw9BeEnsgaMiMFv0H5QecBBYKIwJN4548OVm0Y1XgBWzix1y+MSg8/giWFX8IkECMJk0"
    "T0TQAfc6hsTmK4ntzZsKXp+1y/GZdnkgrP6S0VAxkYMZPgtVw0AnoaYgwnu+yXAhpCUMQ/"
    "u2IKwgtph8WchBO573A6dBHVxoXxRDZx1qzuezD5F5Cuz4fD7K8USeboFbyhAvmJojSjEE"
    "pCSzs545wEvhuivCdde67RGP5vPzDOLRNM/w+mI0uTwYKN7CSEafyv4MWNdfYmTUx5r4PQ"
    "5quC7+eUyBL3AwvVYByvj8ug41YxV4ilIk67d1U1iJAiabEE8pg8gmH+FasZyKMQFiFKV3"
    "2LFce7DZ62giTfKCgbu4q8lODxGgCAsG02+sXY21k0lfgVwC4+YOMFPPEJUaOqQ5SWy7qX"
    "KGTl4CCLAVARmHHHWI9hRhp1/QJCp5ZYdoCYuuPezaw8bl5HO0h5KJzvzaHEOfDmWMcg1B"
    "QYkozeTIfJ9KbBpXehg1Jl/OraXz7/DwcJsJKMzKZ6BSFrQtL1N+PyCLF5VfJa8sv7aw6M"
    "pv68qvz7DuriindbI349TO3D3aLnePqnL3KMzd9HoobmqLuL06ONM+7aS5k0qMPJ26IvCC"
    "zP7VVkLi1+3PNKa2nPlCVVRcAkVldVnFJl11aVF1UX9rrISR/Z6vgg1J2LllIaPwyC7UVK"
    "YsVTZdS9i6pH3mHZnHbNs3MmtzvYtoNW7kKGo3LynHrnvJYnVZuOxsmdWx/b5uz3BIAOH1"
    "jo4yPo8C9wIpvduTowDJ850cPT/AbQ+OMpOjSQdHimxBqxIRL29UfGHRtSmta1Pk11b3+S"
    "Lts+fPGOkqgamNam3fxw5PA3HnU3H3CF3geXeUFeRyOcW0z57PxhpPvKn3OcJ3Qgs2W0eh"
    "6+nHS4hByTHT5vunzeNdVpczky981P5NDslDfWu6k4dddhSfkQlpUUsRKCp7iltp0jUVrW"
    "sq9u1tlMFWp2CDikOwweYZmIXE9Wt2ZmmfdqLcSVvhu5gCE5o6KHj6PBE0OHJgSa+bdc1B"
    "NUPf19GHhiJmEJhzgtdJ2St9T3x6MblaaBefMntNJ9piIjVDJV3npAdvc19GfJHef9PFWU"
    "/+2/s6n00UQepxm6k7JnaLr305JuBzqhN6pwMztepF0ghMUzb2NciQsSoqbaGmsraBxKar"
    "bS2qbbeQeTVf00q5dIty8twhUqMGxNC8nQB30iCIO3JYtJ/679V8VvqOTOSSA3lNRIDfTG"
    "TwVz2MPP69mVgrKMqoM0Vr4xdO+R8z5aqRvMDopc+NH/4HL4x/kQ=="
)
