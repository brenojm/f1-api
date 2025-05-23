"""
Seed inicial – temporada 2024 + GP do Bahrain
Roda somente se o banco ainda não contém dados.
"""

from datetime import date

# ——— repositórios ———
from src.repositories.TeamRepository import add as add_team, list_all as list_teams
from src.repositories.DriverRepository import add as add_driver, list_all as list_drivers
from src.repositories.SeasonRepository import add as add_season
from src.repositories.CircuitRepository import add as add_circuit
from src.repositories.RaceRepository import add as add_race
from src.repositories.DriverContractRepository import add as add_contract
from src.repositories.ResultRepository import add as add_result


def run():
    """Executa o seed, se banco vazio."""
    if list_teams() or list_drivers():
        print("[seed] Dados já existem – seed ignorado.")
        return

    # 1) Teams
    redbull = add_team(
        name="Red Bull Racing",
        logo_url="https://upload.wikimedia.org/wikipedia/en/f/f1/Red_Bull_Racing.svg",
        base_country="AUT",
        principal="Christian Horner",
        founded_year=2005,
    )
    ferrari = add_team(
        name="Scuderia Ferrari",
        logo_url="https://upload.wikimedia.org/wikipedia/en/9/93/Scuderia_Ferrari_Logo.svg",
        base_country="ITA",
        principal="Frédéric Vasseur",
        founded_year=1950,  # ano de estreia na F-1
    )

    # 2) Drivers
    verstappen = add_driver(
        full_name="Max Verstappen",
        nationality="NLD",
        date_of_birth=date(1997, 9, 30),
        image_url="https://upload.wikimedia.org/wikipedia/commons/9/99/Max_Verstappen_2017_Malaysia_3.jpg",
    )
    leclerc = add_driver(
        full_name="Charles Leclerc",
        nationality="MCO",
        date_of_birth=date(1997, 10, 16),
        image_url="https://upload.wikimedia.org/wikipedia/commons/5/5d/Charles_Leclerc_2019.jpg",
    )

    # 3) Season
    season2024 = add_season(
        year=2024,
        start_date=date(2024, 3, 2),
        description="74ª temporada do Campeonato Mundial de Fórmula 1",
    )

    # 4) Circuit
    bahrain = add_circuit(
        name="Bahrain International Circuit",
        country="BHR",
        image_url="https://upload.wikimedia.org/wikipedia/commons/9/95/Bahrain_International_Circuit--Grand_Prix_Layout.svg",
        length_km=5.412,
        map_url="https://www.formula1.com/en/racing/2024/Bahrain.html",
    )

    # 5) Race
    race_bahrain = add_race(
        name="Bahrain Grand Prix",
        race_date=date(2024, 3, 2),
        season_id=season2024.id,
        circuit_id=bahrain.id,
        laps=57,
        weather="Dry",
    )

    # 6) Contracts
    add_contract(
        season_id=season2024.id,
        team_id=redbull.id,
        driver_id=verstappen.id,
        number=1,
        salary_musd=55.0,
    )
    add_contract(
        season_id=season2024.id,
        team_id=ferrari.id,
        driver_id=leclerc.id,
        number=16,
        salary_musd=24.0,
    )

    # 7) Results
    add_result(
        race_id=race_bahrain.id,
        team_id=redbull.id,
        driver_id=verstappen.id,
        position=1,
        points=25,
        fastest_lap=False,
    )
    add_result(
        race_id=race_bahrain.id,
        team_id=ferrari.id,
        driver_id=leclerc.id,
        position=2,
        points=18,
        fastest_lap=True,
    )

    print("[seed] Temporada 2024 e GP do Bahrain inseridos com sucesso.")
