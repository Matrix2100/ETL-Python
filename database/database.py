from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.connections import padrao, operacional, dimensional
from classes.classes_operacional import base_operacional
# from classes.classes_dimensional import base_dimensional


def connect():
    session = get_session_operacional()
    return session


def connection_string(username, password):
    return padrao['dialect'] + '+' + padrao['sql_driver'] + '://' + username + ':' + password + '@' + padrao[
        'host'] + ':' + str(padrao['port']) + '/?service_name=' + padrao['service']


def get_engine(username, password):
    url = connection_string(username, password)
    return create_engine(url, pool_size=50, echo=False)


def get_session_operacional():
    session = sessionmaker(bind=get_engine(operacional['username'], operacional['password']))()
    return session


# def get_session_dimensional():
#     session = sessionmaker(bind=get_engine(dimensional['username'], dimensional['password']))()
#     print('Session do dimensional')
#     return session


# def create_all_operacional():
#     return base_operacional.metadata.create_all(get_session_operacional())


# def create_all_dimensional():
#     return base_dimensional.metadata.create_all(get_session_dimensional())