# Import all the models, so that Base has them before being
# imported by Alembic
from src.db.base_class import Base  # fmt: off
from src.models.users import Users  # fmt: off