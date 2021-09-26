import io
import sys
from sqlalchemy import create_engine, MetaData
from sqlacodegen.codegen import CodeGenerator
from src.config import settings


def generate_model(host, port, user, password, database, outfile=None):
    sql_conn = f"postgresql://{user}:{password}@{host}:{port}/{database}"
    engine = create_engine(sql_conn)
    metadata = MetaData(bind=engine)
    metadata.reflect()
    outfile = io.open(
        outfile,
        'w',
        encoding='utf-8') if outfile else sys.stdout
    generator = CodeGenerator(metadata)
    generator.render(outfile)


if __name__ == '__main__':
    host = settings.pgsql_host
    port = settings.pgsql_port
    user = settings.pgsql_user
    password = settings.pgsql_password
    database = settings.pgsql_db_name

    generate_model(
        host,
        port,
        user,
        password,
        database,
        'models/pgsql_db_models.py')
