from flask import Flask

def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)

    from app import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    return app


app = create_app("config")

if __name__ == "__main__":
    app.run(port=5000, debug=True)