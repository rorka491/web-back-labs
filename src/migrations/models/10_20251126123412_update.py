from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "offices" ADD "tenant_id" INT;
        ALTER TABLE "offices" ADD CONSTRAINT "fk_offices_users_1e919b5c" FOREIGN KEY ("tenant_id") REFERENCES "users" ("id") ON DELETE CASCADE;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "offices" DROP CONSTRAINT IF EXISTS "fk_offices_users_1e919b5c";
        ALTER TABLE "offices" DROP COLUMN "tenant_id";"""


MODELS_STATE = (
    "eJztmm1P2zoUx79KlVdM2qbRsQfdd2kpoxu0V1B2p01T5CZuauHYmeMA1cR3v7bjPDhNsu"
    "ZeCo3oK8p5SOxfbZ//SfrbCqgHcfTaZhy5GFp/9X5bBATyQ9n1smeBMMwd0sDBXCVZIAlS"
    "RjCPOAMuF/YFwBEUJg9GLkMhR5QIK4kxlkbqikBE/NwUE/Qrhg6nPuRLyITjx09hRsSDd+"
    "Li+t/w2lkgiD1jtMiT91Z2h69CZRsTfqIC5d3mjktxHJA8OFzxJSVZNCJcWn1IIAMcystz"
    "Fsvhy9HpmaYzSkaahyRDLOR4cAFizAvT3ZCBS4nkJ0YTqQn68i6v+odHH44+vn1/9FGEqJ"
    "Fklg/3yfTyuSeJisBkZt0rP+AgiVAYc24c8eTLNdENl4BVs8sSSvjEoMv4UlhN/FJDDjBf"
    "NA9EMAB3DobE50uJ7d27Bl5f7YvhqX1xIKJeyNlQsZCTFT7Rrn7ik1ALEOEdX2c4E9Yahj"
    "q+KwgbiM1G32Zy0EEU/cJFUAfn9jfFMFhpz9l08ikNL4Adnk0HJZ4ochbghjLEK5bmgFIM"
    "AanZ2WZmCfBcpG6LcNuzbnPEg+n0zEA8GJcZXp0PRhcHh4q3CJKzL+x+A2wYzzFy22PN8/"
    "ZQTaggFjyY06oCGTl/LkS7cQw8RC2SBXxxXVmKEibrEE8og8gnX+BKsRyLMQHiVu1vLVmu"
    "IrjbB2luzQUDA7eZrDGXh5igmBZMlt/QvhzaxyNLgZwD9/oWMM8xiEoP7dOSJYtddwX9oG"
    "wBBPiKgJyHHLVGexoLl1UhExNHo0hcZiF7hbhju7JJIaq/LQRiGt8VcbMlfbh20D3Nhp0u"
    "FsitbOy0p3HLUhWzb+s6t2kfua3TdLq/a0tiWWjbazmK1mq5kLiXyybWkOljZ8NdncU/J5"
    "lsPl0ggPB2/YWR85/APcGW3m57kSB5vPbi8QFu2l0Yi2OXugtFtkKqpMTrhUosIvYypXMy"
    "RX5tbfuLYs4z7zGKVQJTH5E2HLOEh4G49aW4fYQhiKJbyir2cj3FYs4zX40tOt7CQz/95j"
    "Cq0Ng69eTLBcRATbK2JhfeUu4e77q6bCw+3Wr/Tw55U98ZdXK/TUXxFXmQVkmKxNGoKW5k"
    "yF5UdE5UPLdX2odv3mxwgIuo2gNc+cxauEDi+i2VWTGnmyi3IiviEFPgQc8BFd3nsaDBUQ"
    "BrtK6ZWoLq6dzX6YcdRcwg8KYEr/KyV/trgvH56HJmn/9tPGs6tmcj6ekbPydIrQfvS19G"
    "dpHeP+PZaU/+2/s+nYwUQRpxn6k75nGz75YcE4g5dQi9dYBXOPVSawpmVx7s25Ahd1lV2r"
    "SnsbaBPGZf2zpU224gi7QA3PRULqTsD+W87xBbowVEHd5NgFsRCOKOHFY9T/18OZ1UQyyk"
    "lEBeETHBHx5y+cseRhH/uZtYGyjKWRtFa+13cOWfvJWqkbzA4KnfG9//C2BmGIo="
)
