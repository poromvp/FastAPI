from fastapi import FastAPI, Depends
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship, Session
from pydantic import BaseModel

# a) database.py
engine = create_engine(
    "sqlite:///./rag_history.db", connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# b) models.py
class ChatSession(Base):
    __tablename__ = "chat_sessions"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    messages = relationship("Message", back_populates="session")


class Message(Base):
    __tablename__ = "messages"
    id = Column(Integer, primary_key=True, index=True)
    content = Column(String)
    session_id = Column(Integer, ForeignKey("chat_sessions.id"))
    session = relationship("ChatSession", back_populates="messages")


# c) schemas.py
class MessageCreate(BaseModel):
    content: str


class MessageOut(BaseModel):
    id: int
    content: str

    class Config:
        orm_mode = True  # Quan trọng để đọc ORM model


# d) crud.py
def create_message(db: Session, session_id: int, msg: MessageCreate):
    db_msg = Message(content=msg.content, session_id=session_id)
    db.add(db_msg)
    db.commit()
    db.refresh(db_msg)
    return db_msg


# e) main.py
Base.metadata.create_all(bind=engine)
app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/sessions/{session_id}/messages", response_model=MessageOut)
def add_message(session_id: int, message: MessageCreate, db: Session = Depends(get_db)):
    return create_message(db=db, session_id=session_id, msg=message)


# ==========================================
# 1. DATABASE SETUP (database.py)
# ==========================================
SQLALCHEMY_DATABASE_URL = "sqlite:///./bay_van_menu.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# ==========================================
# 2. SQLALCHEMY MODELS (models.py)
# ==========================================
class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    dishes = relationship("Dish", back_populates="category")


class Dish(Base):
    __tablename__ = "dishes"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Float)
    category_id = Column(Integer, ForeignKey("categories.id"))

    category = relationship("Category", back_populates="dishes")


# ==========================================
# 3. PYDANTIC SCHEMAS (schemas.py)
# ==========================================
class DishCreate(BaseModel):
    name: str
    price: float
    category_id: int


class DishOut(BaseModel):
    id: int
    name: str
    price: float
    category_id: int

    class Config:
        orm_mode = True  # Cực kỳ quan trọng để Pydantic đọc được dữ liệu từ SQLAlchemy


# ==========================================
# 4. CRUD OPERATIONS (crud.py)
# ==========================================
def create_dish(db: Session, dish: DishCreate):
    db_dish = Dish(name=dish.name, price=dish.price, category_id=dish.category_id)
    db.add(db_dish)
    db.commit()
    db.refresh(db_dish)
    return db_dish
