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


# +
class StatusesModel(BaseModel):
    id: int = Field(ge=0)
    name: str = Field(max_length=10)


# +
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
            ldict['email'] = line[2]
            v_statuses = UsersModel(**ldict)
            all_file.append(ldict)
            ldict = {}
    with Session(autoflush=False, bind=engine) as session:
        for i in range(len(all_file)):
            print(all_file[i])
            db_users = Users(id=all_file[i]['id'], name=all_file[i]['name'], email=all_file[i]['email'])
            session.add(db_users)
            session.commit()
            session.refresh(db_users)


def import_orders_from_csv():
    delimiter = ';'
    engine = create_engine('postgresql://main:main@localhost:5432/test_db')
    all_file = []
    with open('orders.csv', 'r', encoding='utf-8') as file:
        lreader = reader(file, delimiter=delimiter)
        ldict = {}
        for line in lreader:
            ldict['id'] = line[0]
            ldict['user_id'] = line[1]
            ldict['status_id'] = line[2]
            v_statuses = OrdersModel(**ldict)
            all_file.append(ldict)
            ldict = {}
    with Session(autoflush=False, bind=engine) as session:
        for i in range(len(all_file)):
            print(all_file[i])
            db_orders = Orders(id=all_file[i]['id'], user_id=all_file[i]['user_id'], status_id=all_file[i]['status_id'])
            session.add(db_orders)
            session.commit()
            session.refresh(db_orders)
# -----------------------------------------


def export_statuses_to_csv():
    delimiter = ';'
    engine = create_engine('postgresql://main:main@localhost:5432/test_db')
    all_file = []
    with Session(autoflush=False, bind=engine) as session:
        db_statuses = session.query(Statuses)
        for db_status in db_statuses:
            ldict = {}
            ldict['id'] = db_status.id
            ldict['name'] = db_status.name
            all_file.append(ldict)
    with open('statuses_ex.csv', 'w', encoding='utf-8') as file:
        lwriter = writer(file, delimiter=';')
        for i in range(len(all_file)):
            lwriter.writerow([all_file[i]['id'], all_file[i]['name']])


def export_users_to_csv():
    delimiter = ';'
    engine = create_engine('postgresql://main:main@localhost:5432/test_db')
    all_file = []
    with Session(autoflush=False, bind=engine) as session:
        db_users = session.query(Users)
        for db_user in db_users:
            ldict = {}
            ldict['id'] = db_user.id
            ldict['name'] = db_user.name
            ldict['email'] = db_user.email
            all_file.append(ldict)
    with open('users_ex.csv', 'w', encoding='utf-8') as file:
        lwriter = writer(file, delimiter=';')
        for i in range(len(all_file)):
            lwriter.writerow([all_file[i]['id'], all_file[i]['name'], all_file[i]['email']])


def export_orders_to_csv():
    delimiter = ';'
    engine = create_engine('postgresql://main:main@localhost:5432/test_db')
    all_file = []
    with Session(autoflush=False, bind=engine) as session:
        db_orders = session.query(Orders)
        for db_order in db_orders:
            ldict = {}
            ldict['id'] = db_order.id
            ldict['user_id'] = db_order.user_id
            ldict['status_id'] = db_order.status_id
            all_file.append(ldict)
    with open('orders_ex.csv', 'w', encoding='utf-8') as file:
        lwriter = writer(file, delimiter=';')
        for i in range(len(all_file)):
            lwriter.writerow([all_file[i]['id'], all_file[i]['user_id'], all_file[i]['status_id']])


export_orders_to_csv()
