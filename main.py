from contextlib import asynccontextmanager

from fastapi import FastAPI

from databese import create_tables, delete_tables
from router import router as task_router

@asynccontextmanager
async def lifespan(app: FastAPI):
	# Load the ML model
	await delete_tables()
	print("База очищена")

	await create_tables()
	print("База готова к работе")

	yield
	# Clean up the ML models and release the resources
	print("Выключение")


app = FastAPI(lifespan=lifespan)
app.include_router(task_router)
