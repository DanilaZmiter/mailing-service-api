from typing import Optional
from uuid import UUID

from pydantic import EmailStr
from sqlalchemy import func  # , ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from src.models import BaseORM


class UserORM(BaseORM):
    __tablename__ = "users"
    uuid: Mapped[UUID] = mapped_column(
        primary_key=True, server_default=func.gen_random_uuid(), unique=True, index=True
    )
    # campaign_id: Mapped[UUID] = mapped_column(ForeignKey("campaign.id", ondelete="CASCADE"), index=True) # cascsde for deleting user when deleting company
    username: Mapped[str] = mapped_column(nullable=False, unique=True)
    first_name: Mapped[str] = mapped_column(nullable=False)
    last_name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[Optional[str]] = mapped_column(nullable=True)
    email: Mapped[EmailStr] = mapped_column(nullable=False)
    is_superuser: Mapped[bool] = mapped_column(default=False)
    password_hash: Mapped[str] = mapped_column(nullable=False)
