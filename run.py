from flask import Flask, request

def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)

    from app import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    return app


app = create_app("config")
@app.before_request
def handle_before_request():
    print("请求地址：" + str(request.path))
    print("请求方法：" + str(request.method))
    print("---请求headers--start--")
    print(str(request.headers).rstrip())
    print("---请求headers--end----")
    print("GET参数：" + str(request.args))
    print("POST参数：" + str(request.form))

@app.after_request
def handle_after_request(response):
    print(response, response.json)
    return response


if __name__ == "__main__":
    app.run(port=5000, debug=True)