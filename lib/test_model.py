from sqlalchemy.orm import declarative_base, Mapped, mapped_column
from sqlalchemy import Integer, String, create_engine

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String)
    age: Mapped[int] = mapped_column(Integer)

engine = create_engine('sqlite:///:memory:', echo=True)
Base.metadata.create_all(engine)

print("Table created successfully!")
