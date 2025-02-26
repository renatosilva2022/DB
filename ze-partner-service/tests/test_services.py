from app.services.partner_service import PartnerService
from app.models.partner import Partner
from app.database import SessionLocal

def test_create_partner():
    db = SessionLocal()
    service = PartnerService(db)
    partner_data = {
        "tradingName": "Test",
        "ownerName": "Owner",
        "document": "123",
        "coverageArea": "MULTIPOLYGON(((0 0, 1 1, 1 0, 0 0)))",
        "address": "POINT(0 0)"
    }
    partner = service.create_partner(partner_data)
    assert partner.id is not None