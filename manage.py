from src import create_app
from src.entities.Base import Base, db
from src import seed

app = create_app()

with app.app_context():
    Base.metadata.create_all(db.engine)   
    seed.run()                            

if __name__ == "__main__":
    app.run(debug=True, port=8000)
