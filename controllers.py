from flask import jsonify
import persistence


def init_controllers(app):

    @app.route("/match", methods=['GET'])
    def get_matches():
        get_all = persistence.MatchDataAccess.get_all()
        return jsonify(get_all)

    @app.route("/match", methods=['POST'])
    def add_match(request):
        print(request.is_json)
        content = request.get_json()
        print(content)
        return 'JSON posted'




