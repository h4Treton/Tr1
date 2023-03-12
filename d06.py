from typing import Any, Type, Sequence
from sqlalchemy import Column, INT, VARCHAR, DECIMAL, ForeignKey, BOOLEAN, create_engine, select, Row, RowMapping
from sqlalchemy.orm import DeclarativeBase, declared_attr, sessionmaker, Session
from pydantic import BaseModel, Field, validator, root_validator, EmailStr
from pydantic.types import Decimal


class Base(DeclarativeBase):
    id = Column(INT, primary_key=True)

    @declared_attr
    def __tablename__(cls):
        return ''.join(f'_{i.lower()}' if i.isupper() else i for i in cls.__name__).strip('_')


class Orders(Base):
    user_id = Column(INT, ForeignKey('users.id', ondelete='CASCADE'))
    status_id = Column(INT, ForeignKey('statuses.id', ondelete='CASCADE'))


class Statuses(Base):
    name = Column(VARCHAR(10), unique=True)


class Users(Base):
    name = Column(VARCHAR(24))
    email = Column(VARCHAR(24), unique=True)


class OrderItems(Base):
    order_id = Column(INT, ForeignKey('orders.id', ondelete='CASCADE'))
    product_id = Column(INT, ForeignKey('products.id', ondelete='CASCADE'))


class Products(Base):
    title = Column(VARCHAR(36))
    description = Column(VARCHAR(140))
    category_id = Column(INT, ForeignKey('categories.id', ondelete='CASCADE'))


class Categories(Base):
    name = Column(VARCHAR(24), unique=True)
# ----------------------------------------------------------------


class OrdersModel(BaseModel):
    id: int = Field(ge=0)
    user_id: int = Field(ge=0)
    status_id: int = Field(ge=0)


class StatusesModel(BaseModel):
    id: int = Field(ge=0)
    name: str = Field(max_length=10)


class UsersModel(BaseModel):
    id: int = Field(ge=0)
    name: str = Field(max_length=24)
    email: str = Field(max_length=24)


class OrderItemsModel(BaseModel):
    id: int = Field(ge=0)
    order_id: int = Field(ge=0)
    product_id: int = Field(ge=0)


class ProductsModel(BaseModel):
    id: int = Field(ge=0)
    title: str = Field(max_length=36)
    description: str = Field(max_length=140)
    category_id: int = Field(ge=0)


class CategoriesModel(BaseModel):
    id: int = Field(ge=0)
    name: str = Field(max_length=24)
# ----------------------------------------------------------------


from csv import reader, DictReader, writer, DictWriter


def import_statuses_from_csv():
    delimiter = ';'
    engine = create_engine('postgresql://main:main@localhost:5432/test_db')
    all_file = []
    with open('statuses.csv', 'r', encoding='utf-8') as file:
        lreader = reader(file, delimiter=delimiter)
        ldict = {}
        for line in lreader:
            ldict['id'] = line[0]
            ldict['name'] = line[1]
            v_statuses = StatusesModel(**ldict)
            all_file.append(ldict)
            ldict = {}
    with Session(autoflush=False, bind=engine) as session:
        for i in range(len(all_file)):
            print(all_file[i])
            db_statuses = Statuses(id=all_file[i]['id'], name=all_file[i]['name'])
            session.add(db_statuses)
            session.commit()
            session.refresh(db_statuses)


def import_users_from_csv():
    delimiter = ';'
    engine = create_engine('postgresql://main:main@localhost:5432/test_db')
    all_file = []
    with open('users.csv', 'r', encoding='utf-8') as file:
        lreader = reader(file, delimiter=delimiter)
        ldict = {}
        for line in lreader:
            ldict['id'] = line[0]
            ldict['name'] = line[1]
            v_statuses = StatusesModel(**ldict)
            all_file.append(ldict)
            ldict = {}
    with Session(autoflush=False, bind=engine) as session:
        for i in range(len(all_file)):
            print(all_file[i])
            db_statuses = Statuses(id=all_file[i]['id'], name=all_file[i]['name'])
            session.add(db_statuses)
            session.commit()
            session.refresh(db_statuses)


import_statuses_from_csv()
