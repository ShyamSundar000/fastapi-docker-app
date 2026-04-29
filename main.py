import json
import os
import uuid
from fastapi import FastAPI, Depends
from pydantic import BaseModel
from database import engine, SessionLocal
from models import Base, ContactDB
from sqlalchemy.orm import Session

#Base.metadata.create_all(bind=engine)
print("App started")

app = FastAPI()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()


class Contact(BaseModel):
    name:str
    phone:str
    email:str

@app.get("/test-db")
def test_db(db:Session=Depends(get_db)):
    return {"message":"DB connected"}

@app.post("/contacts")
def add_contact(contact:Contact, db:Session=Depends(get_db)):
    new_contact=ContactDB(
        name=contact.name,
        phone=contact.phone,
        email=contact.email
    )

    db.add(new_contact)
    db.commit()
    db.refresh(new_contact)

    return new_contact

@app.get("/contacts")
def get_contacts(db:Session=Depends(get_db)):
    contacts = db.query(ContactDB).all()
    return contacts


@app.get("/contacts/{contact_id}")
def get_contact(contact_id:int,db:Session=Depends(get_db)):
    contact=db.query(ContactDB).filter(ContactDB.id==contact_id).first()
    if not contact:
        return {"error":"Contact not found"}
    return contact

@app.put("/contacts/{contact_id}")
def update_contact(contact_id:int,updated:Contact,db:Session=Depends(get_db)):
    contact=db.query(ContactDB).filter(ContactDB.id==contact_id).first()
    if not contact:
        return {"error":"Contact not found"}
    contact.name =  updated.name
    contact.phone = updated.phone
    contact.email = updated.email

    db.commit()
    db.refresh(contact)
    return contact

@app.delete("/contacts/{contact_id}")
def delete_contact(contact_id:int,db:Session=Depends(get_db)):
    contact = db.query(ContactDB).filter(ContactDB.id==contact_id).first()
    if not contact:
        return {"error":"Contact not found"}
    db.delete(contact)
    db.commit()
    return {"message":"Contact deleted successfully!"}