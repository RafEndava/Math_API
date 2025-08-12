from typing import List
from fastapi import APIRouter

from models.schemas import PowInput, SingleInput, ResultOutput, OperationRecord
from core.calculator import calculate_pow, calculate_fibonacci, calculate_factorial
from services.recorder import save_operation, get_all_operations
from services.logger import logger

router = APIRouter()


@router.post("/pow", response_model=ResultOutput)
def pow_route(data: PowInput):
    result = calculate_pow(data.a, data.b)
    logger.info(f"[API] pow({data.a}, {data.b}) = {result}")
    save_operation("pow", data.a, data.b, result)
    return {"result": result}


@router.post("/fibonacci", response_model=ResultOutput)
def fibonacci_route(data: SingleInput):
    result = calculate_fibonacci(data.a)
    logger.info(f"[API] fibonacci({data.a}) = {result}")
    save_operation("fibonacci", data.a, None, result)
    return {"result": result}


@router.post("/factorial", response_model=ResultOutput)
def factorial_route(data: SingleInput):
    result = calculate_factorial(data.a)
    logger.info(f"[API] factorial({data.a}) = {result}")
    save_operation("factorial", data.a, None, result)
    return {"result": result}


@router.get("/history", response_model=List[OperationRecord])
def get_history():
    logger.info("[API] fetched history")
    return get_all_operations()
