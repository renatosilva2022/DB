from pydantic import BaseModel

class PartnerCreate(BaseModel):
    tradingName: str
    ownerName: str
    document: str
    coverageArea: dict
    address: dict

class PartnerRead(BaseModel):
    id: int
    tradingName: str
    ownerName: str
    document: str
    coverageArea: dict
    address: dict