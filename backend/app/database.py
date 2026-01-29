from sqlmodel import create_engine

from dotenv import load_dotenv
import os
load_dotenv()

# DATABASE_URL=f"mysql+pymysql://{os.environ['MYSQL_USER']}:{os.environ['MYSQL_PASSWORD']}@{os.environ['HOST_NAME']}:3306/{os.environ['MYSQL_DATABASE']}"
DATABASE_URL=os.environ['DATABASE_URL']


# sqlite_file_name = "schoolerp.db"
# sqlite_url = f"sqlite:///./{sqlite_file_name}"

engine = create_engine(DATABASE_URL, echo=True, pool_pre_ping=True, pool_recycle=300)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)