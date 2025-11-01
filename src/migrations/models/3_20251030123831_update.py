from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "user" RENAME TO "users";"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "users" RENAME TO "user";"""


MODELS_STATE = (
    "eJztlW9P2zAQxr9KlVdMYhN0ZaC9K5UmmLYisYGQEIquiZtYdexgXwYI9bvjc9LaTf+ISq"
    "ANsXfpc8/Fd7/6co9RoVImzKcLw3T0tfMYSSiYfVjQdzsRlKVXSUAYCWesrMMpMDKoIUEr"
    "jkEYZqWUmUTzErmSVpWVECSqxBq5zLxUSX5bsRhVxjB3hVzfWJnLlN0zM/tZTuIxZyJdqJ"
    "OndLbTY3wonXYq8Zsz0mmjOFGiKqQ3lw+YKzl3c4mkZkwyDcjo9agrKp+qa9qcdVRX6i11"
    "iUFOysZQCQzafSaDREniZ6sxrsGMTvnY3e8d9o4+f+kdWYurZK4cTuv2fO91oiMw/B1NXR"
    "wQaofD6LnR3+ael+gNctCr8YU5LYi29DbEGbJNFGeCx+ivzgtxLOA+FkxmmBO8g4MN1C77"
    "54OT/vmOdX2gbpS9zvUlHzahbh0jtB6lUBmX23CcJ7wMxFe/iq+PsARj7pReMcvrKYY57/"
    "w20tdxPAnmnIQRJJM70Gm8FFFdtc67HCq6RVsBCZnDQ01SB82y6DPNk3zVGmkiGxcJeM//"
    "TfKGNskfu/+ppC1GN0h555MbfgRpNLaA2NjfJsD9vb1nALSutQBdbBGgPRFZPYOLEL//Oh"
    "uuhhiktEBeSNvgdcoT3O0IbvDm38S6gSJ1TUUXxtyKEN7Oz/5Vm+vgx9mxo6AMZtq9xb3g"
    "+G+vl+kToXMGJg=="
)
