from quart import Blueprint, render_template, url_for, redirect, request, session, g, jsonify, send_file, Request
from src.services.office_service import OfficeService
from src.schemas import JsonRpcRequest

lab6 = Blueprint("lab6", __name__, url_prefix="/lab6")


@lab6.route('/')
async def main(): 
    return await render_template('lab6/lab6.html')


@lab6.route('/api', methods=['POST'])
async def api():
    service = OfficeService(user=g.get('user'))
    return await service.handle_request(request)

