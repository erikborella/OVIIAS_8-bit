from Control import app

def migrate_db():
    db.drop_all()
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
