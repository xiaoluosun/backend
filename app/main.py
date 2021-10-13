# coding: utf-8

"""
  __author__ = allen

"""
from datetime import timedelta
from flask_principal import identity_loaded, UserNeed, RoleNeed
from flask import Flask, make_response, jsonify
from flask_cors import CORS
from flask_login import current_user
from .init_app import InitApp
app = Flask(__name__, instance_relative_config=True)

with app.app_context():
    make = InitApp(app)
    make.init_all()

from flask_login import LoginManager
from .lib.connectdb import db
from .scheduler.config import SchedulerConfig
from . lib.logger import logger
from .example import exampleviews
# logger.setup_logger('INFO')


# 解决跨域请求问题
CORS(app, supports_credentials=True)

# session.permanent = True
# app.permanent_session_lifetime = timedelta(minutes=31536000)
app.secret_key = '7890'
# 权限控制
login_manager = LoginManager()
login_manager.login_view = "user_info.login"
login_manager.init_app(app)
login_manager.remember_cookie_duration = timedelta(days=365)

# 注册蓝图
app.register_blueprint(exampleviews.example)

# 非测试环境，启动定时任务
if not app.debug:
    # 初始化定时任务
    app.config.from_object(SchedulerConfig())
    # scheduler = APScheduler()
    scheduler.init_app(app)
    scheduler.start()


@app.errorhandler(404)
def page_not_found(e):
    return make_response(jsonify(msg=str(e), code=404), 404)


@app.errorhandler(401)
def unauthorized_visit(e):
    return make_response(jsonify(msg=str(e), code=401), 401)


@app.errorhandler(500)
def unauthorized_visit(e):
    return make_response(jsonify(msg=str(e), code=500), 500)


@identity_loaded.connect_via(app)
def on_identity_loaded(sender, identity):
    identity.user = current_user

    if hasattr(current_user, 'id'):
        identity.provides.add(UserNeed(current_user.id))

    if hasattr(current_user, 'roles'):
        for role in current_user.roles:
            identity.provides.add(RoleNeed(role.role_name))






