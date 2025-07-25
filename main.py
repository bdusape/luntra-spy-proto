from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

# 1. Initialize the FastAPI app
app = FastAPI()

# 2. Mount the static directory. This is the critical line.
app.mount("/static", StaticFiles(directory="static"), name="static")

# 3. Initialize the templates.
templates = Jinja2Templates(directory="templates")


# --- API Endpoint ---
@app.get("/api/trading-signal/spy")
async def get_spy_trading_signal():
    return {
        "ticker": "SPY",
        "signal": "BUY",
        "confidence": 0.85,
        "strategy": "Momentum Crossover"
    }


# --- Page Routes ---
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request):
    data = {"username": "Brian", "task_count": 5, "agent_status": "Active"}
    return templates.TemplateResponse("dashboard.html", {"request": request, "data": data})


@app.get("/spy-signal", response_class=HTMLResponse)
async def spy_signal_page(request: Request):
    return templates.TemplateResponse("spy_signal.html", {"request": request})

