#!/usr/bin/env python3
from flask import Flask, make_response, jsonify
import config
import init_setup
import controllers


def create_app(env="dev"):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = config.configs[env].DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['TESTING'] = config.configs[env].TESTING
    init_setup.db_global.ma.init_app(app)
    init_setup.db_global.db.init_app(app)
    controllers.init_controllers(app)
    return app


def wrap_app_with_handlers(app):
    @app.errorhandler(404)
    def not_found():
        return make_response(jsonify({'error': 'Not found'}), 404)

    @app.errorhandler(500)
    def server_error():
        return make_response(jsonify({'error': 'Server error'}), 500)

    @app.route("/init")
    def init_database():
        db = init_setup.db_global.db
        db.create_all()
        matches = []
        from models import Match
        match1 = Match("Brasil", "9", "https://www.transfermarkt.es/spielbericht/index/spielbericht/2265626")
        matches.append(match1)
        match2 = Match("Platense", "7", "https://www.youtube.com/watch?v=YVBVc8MjRYA")
        matches.append(match2)
        match3 = Match("Tigre", "10", "https://www.ole.com.ar/futbol-primera/ganamos-actitud_0_Sks1MSJj2l.html")
        matches.append(match3)

        for match in matches:
            db.session.add(match)
        db.session.commit()
        return make_response("OK", 200)


APP_INSTANCE = create_app()
wrap_app_with_handlers(APP_INSTANCE)


if __name__ == '__main__':

    APP_INSTANCE.run(
        host=APP_INSTANCE.config.get('HOST', '0.0.0.0'),
        port=APP_INSTANCE.config.get('PORT', 5000),
        debug=True
    )



