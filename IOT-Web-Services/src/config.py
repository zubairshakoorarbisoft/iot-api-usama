from pydantic import BaseSettings


class Settings(BaseSettings):
    pgsql_host: str
    pgsql_dns: str
    pgsql_port: int
    pgsql_user: str
    pgsql_password: str
    pgsql_db_name: str

    class Config:
        env_prefix = ''
        env_file = '../.env' 


settings = Settings()
