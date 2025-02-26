from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.partner import PartnerCreate, PartnerRead
from app.services.partner_service import PartnerService
from app.database import get_db

router = APIRouter()

@router.post("/partners", response_model=PartnerRead)
def create_partner(partner: PartnerCreate, db: Session = Depends(get_db)):
    service = PartnerService(db)
    return service.create_partner(partner.dict())

@router.get("/partners/{partner_id}", response_model=PartnerRead)
def get_partner(partner_id: int, db: Session = Depends(get_db)):
    service = PartnerService(db)
    return service.get_partner_by_id(partner_id)

@router.get("/partners/search")
def search_partner(lat: float, long: float, db: Session = Depends(get_db)):
    service = PartnerService(db)
    return service.find_nearest_partner(lat, long)