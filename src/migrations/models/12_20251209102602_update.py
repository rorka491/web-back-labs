from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "films" ALTER COLUMN "title_ru" DROP NOT NULL;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "films" ALTER COLUMN "title_ru" SET NOT NULL;"""


MODELS_STATE = (
    "eJztmm1vmzoUgP9KxKdO2qYmt3vR/UbS9DZbm0xtujttmpADhlgFmxnTNpr632ebN0OAha"
    "5pYcmnJOcFjp/4+BwbfmoesaAbvNYpQ6YLtX97PzUMPPGlqHrZ04DvZwohYGAhnTQQGUkh"
    "WASMApNxuQ3cAHKRBQOTIp8hgrkUh64rhMTkhgg7mSjE6EcIDUYcyJaQcsW371yMsAXv+M"
    "Xjn/61YSPoWrlokSXuLeUGW/lSNsHsRBqKuy0Mk7ihhzNjf8WWBKfWCDMhdSCGFDAoLs9o"
    "KMIX0cUjTUYURZqZRCEqPha0QegyZbgbMjAJFvx4NIEcoCPu8mrQP3p39P6ft0fvuYmMJJ"
    "W8u4+Gl409cpQEpnPtXuoBA5GFxJhxY4hFf24e3WgJaDm71KGAjwddxJfAquOXCDKA2aR5"
    "JIIeuDNciB22FNjevKnh9Vm/GJ3qFwfc6oUYDeETOZrh01g1iHQCqgIR3rF1hnMurWAY23"
    "cFYQ2x+fjLXATtBcEPVwV1cK5/kQy9Vaw5m03/S8wVsKOz2bDAEwWGDW4IRaxkag4JcSHA"
    "FZmd9ywAXnDXbRFuutZtjng4m53lEA8nRYZX58PxxUFf8uZGYvRK9ufA+uHCRWZzrJnfw6"
    "DG6+LfxxSEHAc1GhWgnM/v61A7VoHHKEWiftvXpZUoYrIO8YRQiBz8Ea4kywmPCWCzLL3j"
    "juUqgO1eRzNplhcU3KZdTX568AHyYcFo+o30y5F+PNYkyAUwr28BtYwcUaEhA1KQpLbrKm"
    "/gFSUAA0cSEOMQUcdoT5DraSVNopTXdog2t9i3h/v2sHU5+RTtoWBi0LAxx9jnQSgfUm9b"
    "T3IFQUmFqEzkxHyXKqyKSw2jwdwruHU0kw8PDzeZgNysegZKZUnX8jzV9zTkqrLyGylq6+"
    "8yNdnX39ZlbHX9lZ8NUjex72jOPlbNaEnCzmwbmaWnqrGmNmWJtNk3zZ1L2idumv/KTg8F"
    "xoKQaxHFGsjfHVUpjvsDwDxWn8bLzoZZndrvagvNIAaYNTvdy/k8CNwzpPR2D/ciJE93uP"
    "f0ADc928tNjjad7UmyJa1KQry6UQm5xb5N6VybIv62pvsL1WfH9xhqlXCJgxodsaQOjwNx"
    "61Nx+wh9EAS3hJbkcjVF1WfHZ2ODHa/yyC1+bSco6bFj15OPF9AFFUeB668ItY93VV3OTb"
    "54q/2HHLJNfWe6k/ttdhSfkQVJWUsRKWp7ihthsm8qOtdU7NoDw/5GTxn6NQ8Z+tEzBnU5"
    "shG/fsPOTPXpJsqttBWh7xJgQcsAJbvPY06DIQ9W9Lp51wJUK/Z9nXxpKWIKgTXD7iore5"
    "Wv8k3Ox5dz/fxT7qzpWJ+PhWYgpauC9OBt4c9IL9L7fzI/7Ymfva+z6VgSJAFzqLxjZjf/"
    "qomYQMiIgcmtASxl1UukCZi2HOzrkCJzWVbaYk1tbQOZzb62dai23UAaNHyUrrjsF+Vs38"
    "FTowHE2LybALfSIPA7Mlh2nvrhcjYth6i4FEBeYT7AbxYy2cueiwL2vZ1YayiKUeeK1tpL"
    "6MX3zQvVSFxg+NzPje9/AZZ6eOw="
)
