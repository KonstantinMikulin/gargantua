from typing import Optional

from sqlalchemy import select
from sqlalchemy.dialects.postgresql import insert as upsert
from sqlalchemy.ext.asyncio import AsyncSession

from bot.db.models import User, Weight, MeasureChest, MeasureWaist, MeasureHips


async def upsert_user(
    session: AsyncSession,
    telegram_id: int,
    first_name: str,
    last_name: str | None = None,
):
    """
    Добавление или обновление пользователя
    в таблице users
    :param session: сессия СУБД
    :param telegram_id: айди пользователя
    :param first_name: имя пользователя
    :param last_name: фамилия пользователя
    """

    stmt = upsert(User).values(
        {
            "telegram_id": telegram_id,
            "first_name": first_name,
            "last_name": last_name,
        }
    )

    stmt = stmt.on_conflict_do_update(
        index_elements=["telegram_id"],
        set_=dict(first_name=first_name, last_name=last_name),
    )

    await session.execute(stmt)
    await session.commit()


# request to add user weight to db
async def add_weight(session: AsyncSession, telegram_id: int, weight: float):
    """
    Добавление записи веса пользователя
    :param session: сессия СУБД
    :param telegram_id: айди пользователя
    :param weight: вес пользователя
    """

    new_weight = Weight(user_id=telegram_id, weight=weight)
    session.add(new_weight)
    await session.commit()


# TODO: refactor get_all functions
# TODO: change records limit
# get weights list
async def get_all_weights(
    session: AsyncSession, telegram_id: int
):
    stmt = (
        select(Weight)
        .where(Weight.user_id == telegram_id)
        .order_by(Weight.created_at.asc())
    )
    result = await session.execute(stmt)
    weights = result.scalars().fetchall()
    
    return weights


# TODO: make one getter if it will be usefull
# get last weight`s records
async def get_last_weight(
    session: AsyncSession, telegram_id: int
) -> Optional[Weight]:
    stmt = (
        select(Weight)
        .where(Weight.user_id == telegram_id)
        .order_by(Weight.created_at.desc())
        .limit(1)
    )
    result = await session.execute(stmt)
    weight = result.scalars().first()

    return weight


# TODO: write one function for inserting chest, waist and hips at ones
# request to add chest measurement to db
async def add_chest(session: AsyncSession, telegram_id: int, chest: float):
    """
    Добавление записи объема груди пользователя
    :param session: сессия СУБД
    :param telegram_id: айди пользователя
    :param chest: объем груди пользователя
    """

    new_chest = MeasureChest(user_id=telegram_id, measurement=chest)
    session.add(new_chest)
    await session.commit()


async def get_all_chest(
    session: AsyncSession,
    telegram_id: int
):
    stmt = (
        select(MeasureChest)
        .where(MeasureChest.user_id == telegram_id)
        .order_by(MeasureChest.created_at.asc())
    )
    result = await session.execute(stmt)
    records = result.scalars().fetchall()

    return records
    
    
# get last chest`s records
async def get_last_chest(
    session: AsyncSession, telegram_id: int
) -> Optional[MeasureChest]:
    stmt = (
        select(MeasureChest)
        .where(MeasureChest.user_id == telegram_id)
        .order_by(MeasureChest.created_at.desc())
        .limit(1)
    )
    result = await session.execute(stmt)
    chest = result.scalars().first()

    return chest


# request to add tail measurement to db
async def add_waist(session: AsyncSession, telegram_id: int, waist: float):
    """
    Добавление записи объема талии пользователя
    :param session: сессия СУБД
    :param telegram_id: айди пользователя
    :param waist: объем талии пользователя
    """

    new_waist = MeasureWaist(user_id=telegram_id, measurement=waist)
    session.add(new_waist)
    await session.commit()


async def get_all_waist(session: AsyncSession, telegram_id: int):
    stmt = (
        select(MeasureWaist)
        .where(MeasureWaist.user_id == telegram_id)
        .order_by(MeasureWaist.created_at.asc())
    )
    result = await session.execute(stmt)
    records = result.scalars().fetchall()

    return records
    

# get last waist`s records
async def get_last_waist(
    session: AsyncSession, telegram_id: int
) -> Optional[MeasureWaist]:
    stmt = (
        select(MeasureWaist)
        .where(MeasureWaist.user_id == telegram_id)
        .order_by(MeasureWaist.created_at.desc())
        .limit(1)
    )
    result = await session.execute(stmt)
    waist = result.scalars().first()

    return waist


# request to add hips measurement to db
async def add_hips(session: AsyncSession, telegram_id: int, hips: float):
    """
    Добавление записи объема пользователя
    :param session: сессия СУБД
    :param telegram_id: айди пользователя
    :param hips: объем талии пользователя
    """

    new_hips = MeasureHips(user_id=telegram_id, measurement=hips)
    session.add(new_hips)
    await session.commit()


async def get_all_hips(session: AsyncSession, telegram_id: int):
    stmt = (
        select(MeasureHips)
        .where(MeasureHips.user_id == telegram_id)
        .order_by(MeasureHips.created_at.asc())
    )
    result = await session.execute(stmt)
    records = result.scalars().fetchall()

    return records


# get last hips` records
async def get_last_hips(
    session: AsyncSession, telegram_id: int
) -> Optional[MeasureHips]:
    stmt = (
        select(MeasureHips)
        .where(MeasureHips.user_id == telegram_id)
        .order_by(MeasureHips.created_at.desc())
        .limit(1)
    )
    result = await session.execute(stmt)
    hips = result.scalars().first()

    return hips
