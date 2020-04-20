from app import create_app

app = create_app()


# to test things in flask shell
from app import create_app, db
from app.models import Posts

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Posts': Posts}



if __name__ == "__main__":
    app.run(debug=False)
