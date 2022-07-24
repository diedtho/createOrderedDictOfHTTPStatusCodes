from dataclasses import dataclass
from dacite import from_dict

@dataclass()
class Comment:
    doc: str
    description: str

@dataclass()
class Status_Code():
    code: int
    phrase: str
    constant: str
    comment: Comment
