from flask_restful import Api
from src.controllers.DriverController import DriverList, DriverItem
from src.controllers.TeamController import TeamList, TeamItem
from src.controllers.SeasonController import SeasonList, SeasonItem, SeasonDriverStandings, SeasonTeamStandings
from src.controllers.CircuitController import CircuitList, CircuitItem
from src.controllers.RaceController import RaceList, RaceItem
from src.controllers.DriverContractController import ContractList, ContractItem
from src.controllers.ResultController import ResultList, ResultItem

def initialize_endpoints(api) -> None:
    api.add_resource(DriverList, "/drivers")
    api.add_resource(DriverItem, "/drivers/<int:driver_id>")

    api.add_resource(TeamList, "/teams")
    api.add_resource(TeamItem, "/teams/<int:team_id>")

    api.add_resource(SeasonList, "/seasons")
    api.add_resource(SeasonItem, "/seasons/<int:season_id>")

    api.add_resource(CircuitList, "/circuits")
    api.add_resource(CircuitItem, "/circuits/<int:circuit_id>")

    api.add_resource(RaceList, "/races")
    api.add_resource(RaceItem, "/races/<int:race_id>")

    api.add_resource(ContractList, "/contracts")
    api.add_resource(ContractItem, "/contracts/<int:contract_id>")

    api.add_resource(ResultList, "/results")
    api.add_resource(ResultItem, "/results/<int:result_id>")

    api.add_resource(SeasonDriverStandings,
                 "/seasons/<int:season_id>/standings/drivers")
    api.add_resource(SeasonTeamStandings,
                 "/seasons/<int:season_id>/standings/teams")

