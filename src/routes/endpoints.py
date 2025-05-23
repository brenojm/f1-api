from flask_restful import Api
from src.controllers.DriverController import DriverList, DriverItem

def initialize_endpoints(api) -> None:
    api.add_resource(DriverList, "/drivers")
    api.add_resource(DriverItem, "/drivers/<int:driver_id>")
