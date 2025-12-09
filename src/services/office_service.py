from typing import TypeVar
from quart import Request
from src.repositories import OfficeRepository, UserRepository
from src.models import Office, User
from enum import Enum
from src.schemas import OfficeOut, OfficeList, Method
from pydantic import BaseModel
from src.schemas import JsonRpcBookingResponse, JsonRpcCancelationResponse, JsonRpcInfoResponse, JsonRpcRequest
from src.exception import BusinessError, OfficeAlreadyBookedError, OfficeNotRentedByUserError, OfficeNotFound, UserUnauthorized

T = TypeVar('T', bound='OfficeService')

class OfficeService:

    def __init__(self, user: str):
        self.user = user
        self.repo = OfficeRepository()
        self.user_repo = UserRepository()
    
    async def handle_request(self, request: Request) -> dict:
        json_rpc_body = await request.get_json()
        data = JsonRpcRequest(**json_rpc_body)
        match data.method: 
            case Method.INFO: response = await self.info()
            case Method.BOOKING: response = await self.booking(office_id=data.office_id)
            case Method.CANCELATION: response = await self.cancelation(office_id=data.office_id)
        return response.model_dump()

    async def info(self) -> JsonRpcInfoResponse:
        office_list = await self.repo.get_all('tenant')
        result = OfficeList(office_list=office_list)
        return JsonRpcInfoResponse(result=result)

    async def booking(self, office_id: int) -> JsonRpcBookingResponse:
        office = await self.get_office(office_id)
        await self.booking_office(office)
        return JsonRpcBookingResponse(result=office)

    async def cancelation(self, office_id: int) -> JsonRpcCancelationResponse:
        office = await self.get_office(office_id)
        await self.cancel_booking(office)
        return JsonRpcCancelationResponse(result=office)

    async def get_office(self, office_id: int) -> Office:
        office = await self.repo.get_object('tenant', id=office_id)
        if not office:
            raise OfficeNotFound()
        return office

    async def booking_office(self, office: Office) -> Office:
        if office.is_booking:
            raise OfficeAlreadyBookedError()
        
        updated_office = await self.repo.update(
            office, 
            is_booking=True, 
            tenant=self.user
        )
        return updated_office
    
    async def cancel_booking(self, office: Office) -> Office:
        if office.tenant != self.user:
            raise OfficeNotRentedByUserError()
        
        updated_office = await self.repo.update(
            office, 
            is_booking=False, 
            tenant=None
        )
        return updated_office


