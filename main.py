from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def home():
	return {"Estamos en el inicio de la pagina"}

@app.get("/Facturación")
async def Facturación():
	return {"Estamos en el area de Facturación"}
