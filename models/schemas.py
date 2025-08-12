from pydantic import BaseModel


class PowInput(BaseModel):
    a: int
    b: int


class SingleInput(BaseModel):
    a: int


class ResultOutput(BaseModel):
    result: int


class OperationRecord(BaseModel):
    id: int
    type: str
    a: int
    b: int | None
    result: str
    timestamp: str
