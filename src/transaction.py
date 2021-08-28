from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.dialects.postgresql import UUID
import uuid
import datetime
from database import Base


class Transaction(Base):
    __tablename__ = 'some_data'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(Integer)
    amount = Column(Integer)
    created_at = Column(DateTime)

    def __init__(self,
                 id: UUID,
                 user_id: int,
                 # in cents
                 amount: int,
                 created_at: datetime):
        self.id = id
        self.user_id = user_id

        self.amount = amount
        self.created_at = created_at

    def to_dict(self):
        return {
            'id': str(self.id),
            'user_id': self.user_id,
            'amount': self.amount,
            'created_at': self.created_at.isoformat()
        }
