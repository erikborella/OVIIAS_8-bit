from Control import app
import Models

if __name__ == "__main__":
    Users = Models.User.query.all()
    app.run()
