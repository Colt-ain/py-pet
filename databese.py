from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, MappedColumn

engine = create_async_engine(
	"sqlite+aiosqlite:///tasks.db",
)

new_session = AsyncSession(
	engine,
	expire_on_commit=False,
)


class Model(DeclarativeBase):
	pass


class TaskOrm(Model):
	__tablename__ = "tasks"

	id: MappedColumn[int] = MappedColumn(primary_key=True)
	name: MappedColumn[str]
	description: MappedColumn[str]


async def create_tables():
	async  with engine.begin() as conn:
		await conn.run_sync(Model.metadata.create_all)


async def delete_tables():
	async with engine.begin() as conn:
		await conn.run_sync(Model.metadata.drop_all)
