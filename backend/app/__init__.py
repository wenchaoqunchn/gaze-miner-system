from flask import Flask
from flask_cors import CORS
from flasgger import Swagger
from .config import Config
from .routes import init_routes


def create_app() -> Flask:
    """
    创建并配置 Flask 应用程序实例。

    该函数负责初始化 Flask 应用程序，加载配置，设置跨域请求支持，并注册路由。

    Returns:
        Flask: 配置好的 Flask 应用程序实例。
    """
    app = Flask(__name__)
    swagger = Swagger(app)
    app.config.from_object(Config)
    CORS(app)  # 允许跨域请求
    init_routes(app)  # 初始化路由
    return app
