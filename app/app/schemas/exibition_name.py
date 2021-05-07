from ninja import Schema, Path

class PathExibitionName(Schema):
    name: str
    nickname: str
    age: int

    def value(self):
        return {
            "name": self.name,
            "nickname": self.nickname,
            "age": self.age
        }
