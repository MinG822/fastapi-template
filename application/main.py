from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from application.controllers.sample import sample_handler
from application.controllers.exception import exception_handler


app = FastAPI(title="FastAPITemplate", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# FastAPI 인스턴스를 매개변수로 넘겨주면 자동으로 swagger 페이지(host:port/docs)가 생김
app = sample_handler(app=app)
app = exception_handler(app=app)

