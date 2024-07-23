from typing import Annotated, Optional

from fastapi import APIRouter, Depends
from pydantic import BaseModel

from repository import TaskRepository
from schemas import STaskAdd, STask, StaskId

router = APIRouter(
	prefix="/tasks",
)


@router.get("/home")
def get_home():
	return {
		"data": "Hello World!"
	}


tasks = []


@router.post("/")
async def add_task(
		task: Annotated[STaskAdd, Depends()],
) -> StaskId:
	task_id = await TaskRepository.add_one(task)
	return {"ok": True, "task_id": task_id}


@router.get("/")
async def get_tasks() -> list[STask]:
	res = await TaskRepository.find_all()

	return res
