
from typing import Union

from flask import Flask

from app.extensions import db, cors, scheduler
from app.blueprints.sakura_vod_info import vod_bp
from app.blueprints.comment import comment_bp
from app.blueprints.auth import auth_bp
from app.blueprints.video_collection import vd_col_bp
from setting import config


def create_app(env: Union[str, None] = None) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config)
    # if not os.path.exists(app.config['LOGGING_PATH']):
    #     # 日志文件目录
    #     os.mkdir(app.config['LOGGING_PATH'])
    # logging.config.dictConfig(get_logging_config())  # 载入日志配置
    db.init_app(app)
    # csrf.init_app(app)
    cors.init_app(app)
    app.register_blueprint(vod_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(comment_bp)
    app.register_blueprint(vd_col_bp)
    register_process_request(app)
    return app


def register_process_request(app):
    @app.after_request
    def handler_after_request(response):
        # response.headers['Access-Control-Allow-Origin'] = "*"  # 设置允许跨域
        response.headers['Access-Control-Allow-Credentials'] = 'true'
        # response.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'
        return response


if __name__ == '__main__':
    app = create_app(env='PRODUCTION')
    app.run(host='0.0.0.0', debug=False)
