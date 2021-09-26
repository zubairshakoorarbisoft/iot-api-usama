# coding: utf-8
# flake8: noqa
from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class MigrationVersion(Base):
    __tablename__ = 'migration_versions'

    version = Column(String(14), primary_key=True)
    executed_at = Column(
        TIMESTAMP(
            precision=0),
        nullable=False,
        comment='(DC2Type:datetime_immutable)')


class UsersSecurity(Base):
    __tablename__ = 'users_security'
    
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    country_id = Column(Integer, nullable=False)
    company_id = Column(Integer, nullable=False)
    security_key = Column(String(255), nullable=False)
