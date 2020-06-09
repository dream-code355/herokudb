from db_app.app import db, Class

db.session.add(Class(name = "Toshinori Yagi", hobby = "saving the world with a smile", age = 49))
db.session.commit()
