from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Base
    debug: bool
    project_name: str
    api_v1_prefix: str

    # Database
    db_name: str
    db_passwd: str
    db_user: str
    db_host: str
    db_port: int
    db_dialect: str
    db_connector: str
