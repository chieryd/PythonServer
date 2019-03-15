from app import app, api, request
from API.NodeAPI import NodeAPI

api.add_resource(NodeAPI, '/node')

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

# @app.route('/')
# @app.route('/index')
# def index():
#     return "Hello, World!"