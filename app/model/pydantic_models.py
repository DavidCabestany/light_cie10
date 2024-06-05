import json
from pydantic import BaseModel, Field

from typing import Optional, List

class PersonalInfo(BaseModel):
    apellidos: Optional[str] 
    nombre: Optional[str] 
    genero: Optional[str] 
    fecha_de_nacimiento: Optional[str] 
    club: Optional[str] 
    licencia: Optional[str] 
    marked_fields: Optional[List[str]] 
    cie10_codes: Optional[List[str]] 
