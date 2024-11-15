from uuid import UUID

from sqlalchemy import BigInteger, ForeignKey, Uuid, text, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship

from bot.db import Base
from bot.db.models.mixins import TimestampMixin


class Weight(TimestampMixin, Base):
    __tablename__ = 'weights'
    
    id: Mapped[UUID] = mapped_column(
        Uuid, primary_key=True, server_default=text("gen_random_uuid()")
    )
    user_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey('users.telegram_id', ondelete='CASCADE')
    )
    weight: Mapped[float] = mapped_column(Float, nullable=False)
    
    user: Mapped['User'] = relationship(back_populates='weights') # type:ignore  # noqa: F821
