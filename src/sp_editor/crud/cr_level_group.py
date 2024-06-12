import sys
import pandas as pd
from openpyxl.pivot.cache import LevelGroup
from pandas import DataFrame

from sqlmodel import Session, select
from sp_editor.database.models import Grouplevel, Pierlabel, Level

from sqlalchemy.engine.base import Engine


def get_level_db(engine: Engine, df: DataFrame):
    df.to_sql("level", con=engine, if_exists='replace')


def get_pier_label_db(engine: Engine, df: DataFrame):
    df.to_sql("pierlabel", con=engine, if_exists='replace')


def get_pierlabel_with_level(engine: Engine, stories: list[str]):
    with Session(engine) as session:
        statement = select(Pierlabel.piername).where(Pierlabel.story.in_(stories))
        result = session.exec(statement)
        piernames = result.all()
        return piernames


def create_level_group(engine: Engine, stories: list[str]):
    with Session(engine) as session:
        for story in stories:
            group = Grouplevel(story=story, tier='1')
            session.add(group)
        session.commit()


def update_group_level(engine: Engine, stories: list[str], tier_name: str):
    with Session(engine) as session:
        statement = select(Grouplevel).where(Grouplevel.story.in_(stories))
        results = session.exec(statement)
        groups = results.all()
        for group in groups:
            print(group)
            # group.tier = tier_name
            # session.add(group)
            # session.commit()
            # session.refresh(group)
        return groups


def get_level(engine: Engine):
    with Session(engine) as session:
        statement = select(Level)
        results = session.exec(statement)
        level_detail = results.all()
        return level_detail

# def update_tier(engine: Engine, list[Level]):
#     with Session(engine) as session:
#         statement = select(Grouplevel).where(Grouplevel.story==)
