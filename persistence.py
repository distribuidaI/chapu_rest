from models import Match, MatchSchema


class MatchDataAccess:

    @staticmethod
    def get_all():
        raw_data = Match.query.all()
        match_schema = MatchSchema(many=True)
        data = match_schema.dump(raw_data).data
        return data