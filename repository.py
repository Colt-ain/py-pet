from databese import new_session, TaskOrm
from schemas import STaskAdd, STask


class TaskRepository:
	@classmethod
	async def add_one(cls, task: STaskAdd) -> int:
		async with new_session() as session:
			task.dict = task.model_dump()

			task = TaskOrm(**task.dict)
			session.add(task)

			await session.flush()
			await session.commit()

			return task.id

	@classmethod
	async def find_all(cls) -> list[STask]:
		async with new_session() as session:
			query = session.query(TaskOrm)
			result = await session.execute(query)
			tasks = result.scalars().all()

			task_schemas = [STask.model_validate(task_model) for task_model in tasks]

			return task_schemas
