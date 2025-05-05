from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database import Base
import datetime

class Currency(Base):
    __tablename__ = "currency"

    id = Column(Integer, primary_key=True)
    symbol = Column(String, nullable=False)
    name = Column(String, nullable=False)
    market_cap = Column(Float)

    prices = relationship("Price", back_populates="currency", cascade="all, delete-orphan")
    recommendations = relationship("Recommendation", back_populates="currency", cascade="all, delete-orphan")


class Price(Base):
    __tablename__ = "price"

    id = Column(Integer, primary_key=True)
    currency_id = Column(Integer, ForeignKey("currency.id", ondelete="CASCADE"))
    price_usd = Column(Float)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)

    currency = relationship("Currency", back_populates="prices")


class Recommendation(Base):
    __tablename__ = "recommendation"

    id = Column(Integer, primary_key=True)
    currency_id = Column(Integer, ForeignKey("currency.id", ondelete="CASCADE"))
    recommendation = Column(String)
    confidence = Column(Float)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)

    currency = relationship("Currency", back_populates="recommendations")
