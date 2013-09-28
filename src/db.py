import os
import sqlalchemy as sqla
import sqlalchemy.orm as orm
import sqlalchemy.ext.declarative as decl

db_str = os.getenv('DATABASE')
print db_str

engine = sqla.create_engine(db_str)
Session = orm.sessionmaker(bind=engine)
session = Session()
Base = decl.declarative_base()
