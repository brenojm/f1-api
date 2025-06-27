from datetime import date

# --- repositórios ---
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
    print("[seed] Inserindo equipes...")
    redbull = add_team(
        name="Red Bull Racing",
        logo_url="https://media.formula1.com/image/upload/f_auto,c_limit,w_1920,q_auto/f_auto,q_auto/common/f1/teams/2024/redbull.png",
        base_country="AUT",
        principal="Christian Horner",
        founded_year=2005,
    )
    mercedes = add_team(
        name="Mercedes-AMG Petronas F1 Team",
        logo_url="https://media.formula1.com/image/upload/f_auto,c_limit,w_1920,q_auto/f_auto,q_auto/common/f1/teams/2024/mercedes.png",
        base_country="DEU",
        principal="Toto Wolff",
        founded_year=2010,
    )
    ferrari = add_team(
        name="Scuderia Ferrari",
        logo_url="https://media.formula1.com/image/upload/f_auto,c_limit,w_1920,q_auto/f_auto,q_auto/common/f1/teams/2024/ferrari.png",
        base_country="ITA",
        principal="Frédéric Vasseur",
        founded_year=1950,
    )
    mclaren = add_team(
        name="McLaren Formula 1 Team",
        logo_url="https://media.formula1.com/image/upload/f_auto,c_limit,w_1920,q_auto/f_auto,q_auto/common/f1/teams/2024/mclaren.png",
        base_country="GBR",
        principal="Andrea Stella",
        founded_year=1963,
    )
    aston_martin = add_team(
        name="Aston Martin Aramco F1 Team",
        logo_url="https://media.formula1.com/image/upload/f_auto,c_limit,w_1920,q_auto/f_auto,q_auto/common/f1/teams/2024/astonmartin.png",
        base_country="GBR",
        principal="Mike Krack",
        founded_year=2021,
    )
    alpine = add_team(
        name="BWT Alpine F1 Team",
        logo_url="https://media.formula1.com/image/upload/f_auto,c_limit,w_1920,q_auto/f_auto,q_auto/common/f1/teams/2024/alpine.png",
        base_country="FRA",
        principal="Bruno Famin",
        founded_year=2021,
    )
    williams = add_team(
        name="Williams Racing",
        logo_url="https://media.formula1.com/image/upload/f_auto,c_limit,w_1920,q_auto/f_auto,q_auto/common/f1/teams/2024/williams.png",
        base_country="GBR",
        principal="James Vowles",
        founded_year=1977,
    )
    rb = add_team(
        name="Visa Cash App RB F1 Team",
        logo_url="https://media.formula1.com/image/upload/f_auto,c_limit,w_1920,q_auto/f_auto,q_auto/common/f1/teams/2024/rb.png",
        base_country="ITA",
        principal="Laurent Mekies",
        founded_year=2006,
    )
    sauber = add_team(
        name="Stake F1 Team Kick Sauber",
        logo_url="https://media.formula1.com/image/upload/f_auto,c_limit,w_1920,q_auto/f_auto,q_auto/common/f1/teams/2024/sauber.png",
        base_country="CHE",
        principal="Alessandro Alunni Bravi",
        founded_year=1993,
    )
    haas = add_team(
        name="MoneyGram Haas F1 Team",
        logo_url="https://media.formula1.com/image/upload/f_auto,c_limit,w_1920,q_auto/f_auto,q_auto/common/f1/teams/2024/haas.png",
        base_country="USA",
        principal="Ayao Komatsu",
        founded_year=2016,
    )
    print("[seed] Equipes inseridas.")

    # 2) Drivers
    print("[seed] Inserindo pilotos...")
    verstappen = add_driver(
        full_name="Max Verstappen",
        nationality="NLD",
        date_of_birth=date(1997, 9, 30),
        image_url="https://media.formula1.com/image/upload/f_auto,c_limit,w_1920,q_auto/f_auto,q_auto/common/f1/drivers/MAXVER01.png",
    )
    perez = add_driver(
        full_name="Sergio Pérez",
        nationality="MEX",
        date_of_birth=date(1990, 1, 26),
        image_url="https://media.formula1.com/image/upload/f_auto,c_limit,w_1920,q_auto/f_auto,q_auto/common/f1/drivers/SERPER01.png",
    )
    hamilton = add_driver(
        full_name="Lewis Hamilton",
        nationality="GBR",
        date_of_birth=date(1985, 1, 7),
        image_url="https://media.formula1.com/image/upload/f_auto,c_limit,w_1920,q_auto/f_auto,q_auto/common/f1/drivers/LEWHAM01.png",
    )
    russell = add_driver(
        full_name="George Russell",
        nationality="GBR",
        date_of_birth=date(1998, 2, 15),
        image_url="https://media.formula1.com/image/upload/f_auto,c_limit,w_1920,q_auto/f_auto,q_auto/common/f1/drivers/GEORUS01.png",
    )
    leclerc = add_driver(
        full_name="Charles Leclerc",
        nationality="MCO",
        date_of_birth=date(1997, 10, 16),
        image_url="https://media.formula1.com/image/upload/f_auto,c_limit,w_1920,q_auto/f_auto,q_auto/common/f1/drivers/CHALEC01.png",
    )
    sainz = add_driver(
        full_name="Carlos Sainz Jr.",
        nationality="ESP",
        date_of_birth=date(1994, 9, 1),
        image_url="https://media.formula1.com/image/upload/f_auto,c_limit,w_1920,q_auto/f_auto,q_auto/common/f1/drivers/CARSAI01.png",
    )
    norris = add_driver(
        full_name="Lando Norris",
        nationality="GBR",
        date_of_birth=date(1999, 11, 13),
        image_url="https://media.formula1.com/image/upload/f_auto,c_limit,w_1920,q_auto/f_auto,q_auto/common/f1/drivers/LANNOR01.png",
    )
    piastri = add_driver(
        full_name="Oscar Piastri",
        nationality="AUS",
        date_of_birth=date(2001, 4, 6),
        image_url="https://media.formula1.com/image/upload/f_auto,c_limit,w_1920,q_auto/f_auto,q_auto/common/f1/drivers/OSCPIA01.png",
    )
    alonso = add_driver(
        full_name="Fernando Alonso",
        nationality="ESP",
        date_of_birth=date(1981, 7, 29),
        image_url="https://media.formula1.com/image/upload/f_auto,c_limit,w_1920,q_auto/f_auto,q_auto/common/f1/drivers/FERALO01.png",
    )
    stroll = add_driver(
        full_name="Lance Stroll",
        nationality="CAN",
        date_of_birth=date(1998, 10, 29),
        image_url="https://media.formula1.com/image/upload/f_auto,c_limit,w_1920,q_auto/f_auto,q_auto/common/f1/drivers/LANSTR01.png",
    )
    ocon = add_driver(
        full_name="Esteban Ocon",
        nationality="FRA",
        date_of_birth=date(1996, 9, 17),
        image_url="https://media.formula1.com/image/upload/f_auto,c_limit,w_1920,q_auto/f_auto,q_auto/common/f1/drivers/ESTOCO01.png",
    )
    gasly = add_driver(
        full_name="Pierre Gasly",
        nationality="FRA",
        date_of_birth=date(1996, 2, 7),
        image_url="https://media.formula1.com/image/upload/f_auto,c_limit,w_1920,q_auto/f_auto,q_auto/common/f1/drivers/PIEGAS01.png",
    )
    albon = add_driver(
        full_name="Alexander Albon",
        nationality="THA",
        date_of_birth=date(1996, 3, 23),
        image_url="https://media.formula1.com/image/upload/f_auto,c_limit,w_1920,q_auto/f_auto,q_auto/common/f1/drivers/ALEALB01.png",
    )
    sargeant = add_driver(
        full_name="Logan Sargeant",
        nationality="USA",
        date_of_birth=date(2000, 12, 31),
        image_url="https://media.formula1.com/image/upload/f_auto,c_limit,w_1920,q_auto/f_auto,q_auto/common/f1/drivers/LOGSAR01.png",
    )
    ricciardo = add_driver(
        full_name="Daniel Ricciardo",
        nationality="AUS",
        date_of_birth=date(1989, 7, 1),
        image_url="https://media.formula1.com/image/upload/f_auto,c_limit,w_1920,q_auto/f_auto,q_auto/common/f1/drivers/DANRIC01.png",
    )
    tsunoda = add_driver(
        full_name="Yuki Tsunoda",
        nationality="JPN",
        date_of_birth=date(2000, 5, 11),
        image_url="https://media.formula1.com/image/upload/f_auto,c_limit,w_1920,q_auto/f_auto,q_auto/common/f1/drivers/YUKTSU01.png",
    )
    bottas = add_driver(
        full_name="Valtteri Bottas",
        nationality="FIN",
        date_of_birth=date(1989, 8, 28),
        image_url="https://media.formula1.com/image/upload/f_auto,c_limit,w_1920,q_auto/f_auto,q_auto/common/f1/drivers/VALBOT01.png",
    )
    zhou = add_driver(
        full_name="Zhou Guanyu",
        nationality="CHN",
        date_of_birth=date(1999, 5, 30),
        image_url="https://media.formula1.com/image/upload/f_auto,c_limit,w_1920,q_auto/f_auto,q_auto/common/f1/drivers/GUAZHO01.png",
    )
    magnussen = add_driver(
        full_name="Kevin Magnussen",
        nationality="DNK",
        date_of_birth=date(1992, 10, 5),
        image_url="https://media.formula1.com/image/upload/f_auto,c_limit,w_1920,q_auto/f_auto,q_auto/common/f1/drivers/KEVMAG01.png",
    )
    hulkenberg = add_driver(
        full_name="Nico Hülkenberg",
        nationality="DEU",
        date_of_birth=date(1987, 8, 19),
        image_url="https://media.formula1.com/image/upload/f_auto,c_limit,w_1920,q_auto/f_auto,q_auto/common/f1/drivers/NICHUL01.png",
    )
    print("[seed] Pilotos inseridos.")

    # 3) Season
    print("[seed] Inserindo temporada 2024...")
    season2024 = add_season(
        year=2024,
        start_date=date(2024, 3, 2),
        description="75ª temporada do Campeonato Mundial de Fórmula 1",
    )
    print("[seed] Temporada 2024 inserida.")

    # 4) Circuits
    print("[seed] Inserindo circuitos...")
    bahrain = add_circuit(
        name="Bahrain International Circuit",
        country="BHR",
        length_km=5.412,
    )
    jeddah = add_circuit(
        name="Jeddah Corniche Circuit",
        country="SAU",
        length_km=6.174,
    )
    melbourne = add_circuit(
        name="Albert Park Circuit",
        country="AUS",
        length_km=5.303,
    )
    suzuka = add_circuit(
        name="Suzuka International Racing Course",
        country="JPN",
        length_km=5.807,
    )
    shanghai = add_circuit(
        name="Shanghai International Circuit",
        country="CHN",
        length_km=5.451,
    )
    miami = add_circuit(
        name="Miami International Autodrome",
        country="USA",
        length_km=5.410,
    )
    imola = add_circuit(
        name="Autodromo Internazionale Enzo e Dino Ferrari",
        country="ITA",
        length_km=4.909,
    )
    monaco = add_circuit(
        name="Circuit de Monaco",
        country="MCO",
        length_km=3.337,
    )
    montreal = add_circuit(
        name="Circuit Gilles Villeneuve",
        country="CAN",
        length_km=4.361,
    )
    barcelona = add_circuit(
        name="Circuit de Barcelona-Catalunya",
        country="ESP",
        length_km=4.655,
    )
    spielberg = add_circuit(
        name="Red Bull Ring",
        country="AUT",
        length_km=4.318,
    )
    silverstone = add_circuit(
        name="Silverstone Circuit",
        country="GBR",
        length_km=5.891,
    )
    hungaroring = add_circuit(
        name="Hungaroring",
        country="HUN",
        length_km=4.381,
    )
    spa = add_circuit(
        name="Circuit de Spa-Francorchamps",
        country="BEL",
        length_km=7.004,
    )
    zandvoort = add_circuit(
        name="Circuit Zandvoort",
        country="NLD",
        length_km=4.259,
    )
    monza = add_circuit(
        name="Autodromo Nazionale Monza",
        country="ITA",
        length_km=5.793,
    )
    baku = add_circuit(
        name="Baku City Circuit",
        country="AZE",
        length_km=6.003,
    )
    singapore = add_circuit(
        name="Marina Bay Street Circuit",
        country="SGP",
        length_km=5.063,
    )
    cota = add_circuit(
        name="Circuit of the Americas",
        country="USA",
        length_km=5.513,
    )
    mexico_city = add_circuit(
        name="Autódromo Hermanos Rodríguez",
        country="MEX",
        length_km=4.304,
    )
    sao_paulo = add_circuit(
        name="Autódromo José Carlos Pace",
        country="BRA",
        length_km=4.309,
    )
    las_vegas = add_circuit(
        name="Las Vegas Strip Circuit",
        country="USA",
        length_km=6.201,
    )
    lusail = add_circuit(
        name="Lusail International Circuit",
        country="QAT",
        length_km=5.380,
    )
    abu_dhabi = add_circuit(
        name="Yas Marina Circuit",
        country="ARE",
        length_km=5.281,
    )
    print("[seed] Circuitos inseridos.")

    # 5) Races
    print("[seed] Inserindo corridas...")
    race_bahrain = add_race(
        name="Bahrain Grand Prix",
        race_date=date(2024, 3, 2),
        season_id=season2024.id,
        circuit_id=bahrain.id,
        laps=57,
        weather="Dry",
    )
    add_race(
        name="Saudi Arabian Grand Prix",
        race_date=date(2024, 3, 9),
        season_id=season2024.id,
        circuit_id=jeddah.id,
        laps=50,
        weather="Dry",
    )
    add_race(
        name="Australian Grand Prix",
        race_date=date(2024, 3, 24),
        season_id=season2024.id,
        circuit_id=melbourne.id,
        laps=58,
        weather="Dry",
    )
    add_race(
        name="Japanese Grand Prix",
        race_date=date(2024, 4, 7),
        season_id=season2024.id,
        circuit_id=suzuka.id,
        laps=53,
        weather="Dry",
    )
    add_race(
        name="Chinese Grand Prix",
        race_date=date(2024, 4, 21),
        season_id=season2024.id,
        circuit_id=shanghai.id,
        laps=56,
        weather="Dry",
    )
    add_race(
        name="Miami Grand Prix",
        race_date=date(2024, 5, 5),
        season_id=season2024.id,
        circuit_id=miami.id,
        laps=57,
        weather="Dry",
    )
    add_race(
        name="Emilia Romagna Grand Prix",
        race_date=date(2024, 5, 19),
        season_id=season2024.id,
        circuit_id=imola.id,
        laps=63,
        weather="Dry",
    )
    add_race(
        name="Monaco Grand Prix",
        race_date=date(2024, 5, 26),
        season_id=season2024.id,
        circuit_id=monaco.id,
        laps=78,
        weather="Dry",
    )
    add_race(
        name="Canadian Grand Prix",
        race_date=date(2024, 6, 9),
        season_id=season2024.id,
        circuit_id=montreal.id,
        laps=70,
        weather="Wet", # Based on real-world conditions
    )
    add_race(
        name="Spanish Grand Prix",
        race_date=date(2024, 6, 23),
        season_id=season2024.id,
        circuit_id=barcelona.id,
        laps=66,
        weather="Dry",
    )
    add_race(
        name="Austrian Grand Prix",
        race_date=date(2024, 6, 30),
        season_id=season2024.id,
        circuit_id=spielberg.id,
        laps=71,
        weather="Dry",
    )
    add_race(
        name="British Grand Prix",
        race_date=date(2024, 7, 7),
        season_id=season2024.id,
        circuit_id=silverstone.id,
        laps=52,
        weather="Dry",
    )
    add_race(
        name="Hungarian Grand Prix",
        race_date=date(2024, 7, 21),
        season_id=season2024.id,
        circuit_id=hungaroring.id,
        laps=70,
        weather="Dry",
    )
    add_race(
        name="Belgian Grand Prix",
        race_date=date(2024, 7, 28),
        season_id=season2024.id,
        circuit_id=spa.id,
        laps=44,
        weather="Dry",
    )
    add_race(
        name="Dutch Grand Prix",
        race_date=date(2024, 8, 25),
        season_id=season2024.id,
        circuit_id=zandvoort.id,
        laps=72,
        weather="Dry",
    )
    add_race(
        name="Italian Grand Prix",
        race_date=date(2024, 9, 1),
        season_id=season2024.id,
        circuit_id=monza.id,
        laps=53,
        weather="Dry",
    )
    add_race(
        name="Azerbaijan Grand Prix",
        race_date=date(2024, 9, 15),
        season_id=season2024.id,
        circuit_id=baku.id,
        laps=51,
        weather="Dry",
    )
    add_race(
        name="Singapore Grand Prix",
        race_date=date(2024, 9, 22),
        season_id=season2024.id,
        circuit_id=singapore.id,
        laps=62,
        weather="Dry",
    )
    add_race(
        name="United States Grand Prix",
        race_date=date(2024, 10, 20),
        season_id=season2024.id,
        circuit_id=cota.id,
        laps=56,
        weather="Dry",
    )
    add_race(
        name="Mexico City Grand Prix",
        race_date=date(2024, 10, 27),
        season_id=season2024.id,
        circuit_id=mexico_city.id,
        laps=71,
        weather="Dry",
    )
    add_race(
        name="São Paulo Grand Prix",
        race_date=date(2024, 11, 3),
        season_id=season2024.id,
        circuit_id=sao_paulo.id,
        laps=71,
        weather="Dry",
    )
    add_race(
        name="Las Vegas Grand Prix",
        race_date=date(2024, 11, 23),
        season_id=season2024.id,
        circuit_id=las_vegas.id,
        laps=50,
        weather="Dry",
    )
    add_race(
        name="Qatar Grand Prix",
        race_date=date(2024, 12, 1),
        season_id=season2024.id,
        circuit_id=lusail.id,
        laps=57,
        weather="Dry",
    )
    add_race(
        name="Abu Dhabi Grand Prix",
        race_date=date(2024, 12, 8),
        season_id=season2024.id,
        circuit_id=abu_dhabi.id,
        laps=58,
        weather="Dry",
    )
    print("[seed] Corridas inseridas.")

    # 6) Contracts
    print("[seed] Inserindo contratos de pilotos...")
    # Red Bull
    add_contract(season_id=season2024.id, team_id=redbull.id, driver_id=verstappen.id, number=1, salary_musd=55.0)
    add_contract(season_id=season2024.id, team_id=redbull.id, driver_id=perez.id, number=11, salary_musd=10.0)
    # Mercedes
    add_contract(season_id=season2024.id, team_id=mercedes.id, driver_id=hamilton.id, number=44, salary_musd=35.0)
    add_contract(season_id=season2024.id, team_id=mercedes.id, driver_id=russell.id, number=63, salary_musd=18.0)
    # Ferrari
    add_contract(season_id=season2024.id, team_id=ferrari.id, driver_id=leclerc.id, number=16, salary_musd=24.0)
    add_contract(season_id=season2024.id, team_id=ferrari.id, driver_id=sainz.id, number=55, salary_musd=12.0)
    # McLaren
    add_contract(season_id=season2024.id, team_id=mclaren.id, driver_id=norris.id, number=4, salary_musd=20.0)
    add_contract(season_id=season2024.id, team_id=mclaren.id, driver_id=piastri.id, number=81, salary_musd=3.0)
    # Aston Martin
    add_contract(season_id=season2024.id, team_id=aston_martin.id, driver_id=alonso.id, number=14, salary_musd=18.0)
    add_contract(season_id=season2024.id, team_id=aston_martin.id, driver_id=stroll.id, number=18, salary_musd=10.0)
    # Alpine
    add_contract(season_id=season2024.id, team_id=alpine.id, driver_id=ocon.id, number=31, salary_musd=5.0)
    add_contract(season_id=season2024.id, team_id=alpine.id, driver_id=gasly.id, number=10, salary_musd=5.0)
    # Williams
    add_contract(season_id=season2024.id, team_id=williams.id, driver_id=albon.id, number=23, salary_musd=3.0)
    add_contract(season_id=season2024.id, team_id=williams.id, driver_id=sargeant.id, number=2, salary_musd=1.0)
    # RB
    add_contract(season_id=season2024.id, team_id=rb.id, driver_id=ricciardo.id, number=3, salary_musd=2.0)
    add_contract(season_id=season2024.id, team_id=rb.id, driver_id=tsunoda.id, number=22, salary_musd=1.0)
    # Sauber
    add_contract(season_id=season2024.id, team_id=sauber.id, driver_id=bottas.id, number=77, salary_musd=10.0)
    add_contract(season_id=season2024.id, team_id=sauber.id, driver_id=zhou.id, number=24, salary_musd=2.0)
    # Haas
    add_contract(season_id=season2024.id, team_id=haas.id, driver_id=magnussen.id, number=20, salary_musd=5.0)
    add_contract(season_id=season2024.id, team_id=haas.id, driver_id=hulkenberg.id, number=27, salary_musd=3.0)
    print("[seed] Contratos de pilotos inseridos.")

    # 7) Results (Bahrain Grand Prix 2024 - based on actual results)
    print("[seed] Inserindo resultados do GP do Bahrain 2024...")
    # FIX: Points are for position only, fastest_lap handles the bonus point.
    add_result(race_id=race_bahrain.id, team_id=redbull.id, driver_id=verstappen.id, position=1, points=25, fastest_lap=True)
    add_result(race_id=race_bahrain.id, team_id=redbull.id, driver_id=perez.id, position=2, points=18, fastest_lap=False)
    add_result(race_id=race_bahrain.id, team_id=ferrari.id, driver_id=sainz.id, position=3, points=15, fastest_lap=False)
    add_result(race_id=race_bahrain.id, team_id=ferrari.id, driver_id=leclerc.id, position=4, points=12, fastest_lap=False)
    add_result(race_id=race_bahrain.id, team_id=mercedes.id, driver_id=russell.id, position=5, points=10, fastest_lap=False)
    add_result(race_id=race_bahrain.id, team_id=mercedes.id, driver_id=hamilton.id, position=7, points=6, fastest_lap=False)
    add_result(race_id=race_bahrain.id, team_id=mclaren.id, driver_id=norris.id, position=8, points=4, fastest_lap=False)
    add_result(race_id=race_bahrain.id, team_id=aston_martin.id, driver_id=alonso.id, position=9, points=2, fastest_lap=False)
    add_result(race_id=race_bahrain.id, team_id=mclaren.id, driver_id=piastri.id, position=10, points=1, fastest_lap=False)
    add_result(race_id=race_bahrain.id, team_id=rb.id, driver_id=tsunoda.id, position=14, points=0, fastest_lap=False)
    add_result(race_id=race_bahrain.id, team_id=rb.id, driver_id=ricciardo.id, position=13, points=0, fastest_lap=False)
    add_result(race_id=race_bahrain.id, team_id=haas.id, driver_id=hulkenberg.id, position=16, points=0, fastest_lap=False)
    add_result(race_id=race_bahrain.id, team_id=haas.id, driver_id=magnussen.id, position=12, points=0, fastest_lap=False)
    add_result(race_id=race_bahrain.id, team_id=williams.id, driver_id=albon.id, position=15, points=0, fastest_lap=False)
    add_result(race_id=race_bahrain.id, team_id=williams.id, driver_id=sargeant.id, position=20, points=0, fastest_lap=False)
    add_result(race_id=race_bahrain.id, team_id=alpine.id, driver_id=ocon.id, position=17, points=0, fastest_lap=False)
    add_result(race_id=race_bahrain.id, team_id=alpine.id, driver_id=gasly.id, position=18, points=0, fastest_lap=False)
    add_result(race_id=race_bahrain.id, team_id=sauber.id, driver_id=bottas.id, position=19, points=0, fastest_lap=False)
    add_result(race_id=race_bahrain.id, team_id=sauber.id, driver_id=zhou.id, position=11, points=0, fastest_lap=False)
    add_result(race_id=race_bahrain.id, team_id=aston_martin.id, driver_id=stroll.id, position=6, points=8, fastest_lap=False) # Corrected Stroll's actual position and points in Bahrain

    print("[seed] Resultados do GP do Bahrain 2024 inseridos.")
    print("[seed] Temporada 2024 completa e GP do Bahrain inseridos com sucesso.")