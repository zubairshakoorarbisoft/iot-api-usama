import io
import sys
from sqlalchemy import create_engine, MetaData
from sqlacodegen.codegen import CodeGenerator


def generate_model(outfile=None):
    # engine = create_engine(
    #     f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}')
    engine = create_engine('mssql+pyodbc://DESKTOP-DTMKRB0\\SQLEXPRESS/SensyrtechStage2?trusted_connection=yes&driver=ODBC+Driver+13+for+SQL+Server')
    metadata = MetaData(bind=engine)
    metadata.reflect()
    outfile = io.open(
        outfile,
        'w',
        encoding='utf-8') if outfile else sys.stdout
    generator = CodeGenerator(metadata)
    generator.render(outfile)


if __name__ == '__main__':
 

    generate_model(
        'sql_db_models.py')
