import os
import psycopg2
from typing import List, Optional
from datetime import date, datetime
from fastapi import FastAPI, Form, HTTPException
from pydantic import BaseModel, EmailStr

app = FastAPI(title="CSGO Tournament API")

# --- Modèles Pydantic ---

class EquipeBase(BaseModel):
    nom_equipe: str

class Equipe(EquipeBase):
    id_equipe: int

class ParticipantBase(BaseModel):
    pseudo: str
    date_naissance: date
    email: Optional[EmailStr] = None
    pays: Optional[str] = None

class Participant(ParticipantBase):
    id_participant: int

class Match(BaseModel):
    numero_match: int
    date_heure: datetime
    etat: str
    id_saison: Optional[int] = None
    scores: Optional[List[dict]] = []

# --- Connexion BDD ---

def get_conn():
    return psycopg2.connect(
        host="pg-sandbox",
        port=5432,
        dbname="appdb",
        user="appuser",
        password="apppass"
    )

# --- Endpoints ---

@app.get("/ping")
def ping():
    return {"ok": True}

@app.get("/equipes", response_model=List[Equipe])
def get_equipes():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT id_equipe, nom_equipe FROM equipe ORDER BY nom_equipe")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return [{"id_equipe": r[0], "nom_equipe": r[1]} for r in rows]

@app.get("/participants", response_model=List[Participant])
def get_participants():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT id_participant, pseudo, date_naissance, email, pays FROM participant")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return [
        {
            "id_participant": r[0], 
            "pseudo": r[1], 
            "date_naissance": r[2], 
            "email": r[3], 
            "pays": r[4]
        } for r in rows
    ]

@app.get("/matchs")
def get_matchs():
    conn = get_conn()
    cur = conn.cursor()
    # On récupère les matchs et les noms des équipes liées
    query = """
        SELECT m.numero_match, m.date_heure, m.etat, e.nom_equipe, me.score
        FROM matchs m
        JOIN match_equipe me ON m.numero_match = me.numero_match
        JOIN equipe e ON me.id_equipe = e.id_equipe
        ORDER BY m.date_heure
    """
    cur.execute(query)
    rows = cur.fetchall()
    cur.close()
    conn.close()
    
    # Transformation pour grouper par match
    matchs_dict = {}
    for r in rows:
        num = r[0]
        if num not in matchs_dict:
            matchs_dict[num] = {
                "numero_match": num,
                "date_heure": r[1],
                "etat": r[2],
                "equipes": []
            }
        matchs_dict[num]["equipes"].append({"nom": r[3], "score": r[4]})
    
    return list(matchs_dict.values())

# --- Endpoint pédagogique (Formulaire) ---

# @app.post("/login")
# def login(
#     username: str = Form(...),
#     password: str = Form(...)
# ):
#     """
#     Exemple pédagogique de réception de données via un formulaire HTML classique.
#     Utilise 'python-multipart' (doit être installé via pip).
#     """
#     # Ici on simule une vérification
#     if username == "admin" and password == "p@ssword":
#         return {"message": "Connexion réussie", "user": username}
#     raise HTTPException(status_code=401, detail="Identifiants invalides")
