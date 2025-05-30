from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()  # << ESTA LÍNEA es clave


class Temperatura(BaseModel):
    grados: float


@app.post("/recomendar")
def recomendar_ropa(temp: Temperatura):
    t = temp.grados
    if t <= 5:
        ropa = "Gorra y abrigo largo"
    elif t <= 10:
        ropa = "Sweater y jeans"
    elif t <= 15:
        ropa = "Suéter ligero y pantalón"
    elif t <= 20:
        ropa = "Camisa de manga larga"
    elif t <= 25:
        ropa = "Playera y jeans"
    else:
        ropa = "Playera y pantaloneta"
    return {"recomendacion": ropa}
