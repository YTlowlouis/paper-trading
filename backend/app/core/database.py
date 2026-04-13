from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, session_maker


DATABASE_URL = "sqlite:///./data/database.db"


engine = create_engine(
    DATABASE_URL
)

SessionLocal = session_maker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
