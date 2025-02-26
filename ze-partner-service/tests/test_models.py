import pytest
from app.models.partner import Partner
from app.database import Base, engine

@pytest.fixture
def db_session():
    Base.metadata.create_all(bind=engine)
    from sqlalchemy.orm import sessionmaker
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()

def test_create_partner(db_session):
    partner = Partner(tradingName="Test", ownerName="Owner", document="123", coverageArea="MULTIPOLYGON(((0 0, 1 1, 1 0, 0 0)))", address="POINT(0 0)")
    db_session.add(partner)
    db_session.commit()
    assert partner.id is not None