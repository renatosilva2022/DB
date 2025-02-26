from sqlalchemy.orm import Session
from app.models.partner import Partner

class PartnerService:
    def __init__(self, db: Session):
        self.db = db

    def create_partner(self, partner_data):
        partner = Partner(**partner_data)
        self.db.add(partner)
        self.db.commit()
        self.db.refresh(partner)
        return partner

    def get_partner_by_id(self, partner_id):
        return self.db.query(Partner).filter(Partner.id == partner_id).first()

    def find_nearest_partner(self, lat: float, long: float):
        point = f"SRID=4326;POINT({long} {lat})"
        return self.db.query(Partner).filter(Partner.coverageArea.ST_Contains(point)).first()