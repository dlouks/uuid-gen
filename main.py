from fastapi import FastAPI
import psycopg2
from pydantic import PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict

app = FastAPI()

class Settings(BaseSettings):
    dbuser: str = "uuidgen"
    dbpassword: str = ""
    host: str = "database-1-instance-1.c7mqgpfkwe5m.us-east-1.rds.amazonaws.com"
    dbname: str = "uuidgen"
    port: str = "5432"
    
@app.get("/api/generate/v1")
async def root():
    settings = Settings()
    connection = psycopg2.connect(user=settings.dbuser,
                                  password=settings.dbpassword,
                                  host=settings.host,
                                  port=settings.port,
                                  dbname=settings.dbname)
    sql = "SELECT uuid_in(overlay(overlay(md5(random()::text || ':' || random()::text) placing '4' from 13) placing to_hex(floor(random()*(11-8+1) + 8)::int)::text from 17)::cstring);"
    cursor = connection.cursor()
    cursor.execute(sql)
    record = cursor.fetchone()
    return record
