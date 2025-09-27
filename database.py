from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:416158@host:5432/lexora")
#DATABASE_URL = "postgresql+psycopg2://postgres:416158@localhost:5432/lexora"

#DATABASE_URL = os.getenv(
#    "DATABASE_URL",
#    "postgresql+psycopg2://postgres:416158@localhost:5432/lexora"
#)

DATABASE_URL = "postgresql://postgres:416158@localhost:5432/lexora"


engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()



