from src.repositories import GiftRepository, M
from src.schemas import GiftOut 
from src.exception import GiftAlreadyOpened, GiftNotFound



class GiftService:
    repo = GiftRepository()

    async def get_all(self) -> list[GiftOut]:
        gifts = await self.repo.get_all()
        return [GiftOut.model_validate(gift).model_dump() for gift in gifts]

    async def open_gift(self, id: int) -> GiftOut:
        gift = await self.repo.get_object(id=id)

        if not gift:
            raise GiftNotFound()

        if gift.is_opened:
            raise GiftAlreadyOpened()
        
        open_gift = await self.repo.update(gift, is_opened=True)
        return GiftOut.model_validate(open_gift).model_dump()
    
    async def restore_gifts(self):
        all_gifts = await self.repo.get_all()

        for gift in all_gifts:
            gift.is_opened = False

        await self.repo.bulk_update(all_gifts, fields=["is_opened"])
    




