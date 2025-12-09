from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "films" ALTER COLUMN "title_ru" SET NOT NULL;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "films" ALTER COLUMN "title_ru" DROP NOT NULL;"""


MODELS_STATE = (
    "eJztmm1vmzoUgP9KxKdeaZuarHvR/UbSdM3WJlOb7k6bJuSASawamxnTNpr6369t3gmw0D"
    "UtLHxKcl7AfuLjc3zgl+ZQC2Lvlc44MjHU/u390ghw5Je86kVPA66bKKSAg4Vy0kBgpIRg"
    "4XEGTC7kNsAeFCILeiZDLkeUCCnxMZZCagpDRJaJyCfopw8NTpeQryATiu8/hBgRC96Ji4"
    "c/3WvDRhBbmdEiS95byQ2+dpVsQviJMpR3Wxgmxb5DEmN3zVeUxNaIcCldQgIZ4FBenjNf"
    "Dl+OLpxpNKNgpIlJMMSUjwVt4GOemu6WDExKJD8xGk9NcCnv8nLQP3p39P7126P3wkSNJJ"
    "a8uw+ml8w9cFQEpnPtXukBB4GFwphw44gHf24W3WgFWDG72CGHTww6jy+CVcUvEiQAk0Xz"
    "SAQdcGdgSJZ8JbG9eVPB64t+MTrVLw6E1T9yNlQs5GCFT0PVINBJqCmI8I5vMpwLaQnD0L"
    "4tCCuIzcdf53LQjuf9xGlQB+f6V8XQWYeas9n0Q2SeAjs6mw1zPJFn2OCGMsQLluaQUgwB"
    "KYnsrGcO8EK47opw3b1ue8TD2ewsg3g4yTO8Oh+OLw76ircwkrNPRX8GrOsvMDLrY038Hg"
    "Y13Bf/PqbAFziYUSsBZXx+n4easQs8RiqS+du+LsxEAZNNiCeUQbQkn+BasZyIMQFiFoV3"
    "WLFcebDZ+2giTeKCgdu4qskuDzFBMS0YLL+RfjnSj8eaArkA5vUtYJaRISo1dEBzkth2U+"
    "UMnLwEELBUBOQ85KhDtCcIO1pBkajklRWiLSy68rArDxsXk09RHkomBvNrcwx9OpQxyjUE"
    "BSmiNJIj831KsWlc6WHUWHw5t5auv8PDw20WoDArX4FKWVC2PE/6PfWFqij/BorKBLyKTb"
    "oE3LiILU/A6rNG6Eb2LY3Zx8oZDQnYmW0js7CtGmoqQ5Yqm65qbl3QPnHV/JDWSiOjNteq"
    "WlB6LUexAfJ3vaqUY9cBzGJ1WbjtbBnVsf2+ltAcEkB4vfZexudB4J4hpHfb3QuQPF137+"
    "kBbtvcyyyOJjX3FNmCUiUiXl6o+MKiK1NaV6bIv63u+SLts+dnjHSWwHSJarVYYofHgbjz"
    "pbh7hC7wvFvKCmK5nGLaZ89XY40Tb+qZW/jejldQY4euJ58uIAYlrcDNd4Sax7ssL2cWX3"
    "jU/kMOyaG+NdXJ/S4rii/IgrSopAgUlTXFjTTpiorWFRX79sSwv9VThn7FQ4Z+8IwhvR3Z"
    "SFy/ZmWW9mknyp2UFb6LKbCgZYCC0+exoMGRA0tq3axrDqoV+r6KvjQUMYPAmhG8TtJe6b"
    "t8k/Px5Vw//5zpNR3r87HUDJR0nZMevM39GfFFev9N5qc9+bP3bTYdK4LU40um7pjYzb9p"
    "ckzA59Qg9NYAVmrXi6QRmKY09nXIkLkqSm2hpjK3gcSmy20tym03kHk1H6WnXLpNOTl3iN"
    "CoATE0byfAnRQI4o4cFvVTP17OpsUQUy45kFdETPC7hUz+ooeRx380E2sFRTnrTNLaeAs9"
    "/8J5LhvJCwyf+7nx/f8QpHk3"
)
