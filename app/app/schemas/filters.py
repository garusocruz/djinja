from ninja import Schema, Path

class Filters(Schema):
    limit: int = 0
    offset: int = 0
    query: str = None