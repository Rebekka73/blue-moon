from fastapi import FastAPI
app = FastAPI(title="PocketSmart AI")

@app.get("/")
def home():
    return {"message": "PocketSmart AI - Smart Budget & Recommendation Assistant is Running"}

@app.post("/add-expense")
def add_expense(amount: float, category: str):
    # AI logic here
    return {"status": "saved", "recommendation": f"You spent {amount} on {category}. Try saving 10% next time!"}
