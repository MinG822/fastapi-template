from fastapi import FastAPI, Request
from application.validators import sample as sample_validator

samples = {"a":"apple", "b":"banana", "c":"camera"}

def sample_handler(app:FastAPI):
    @app.get(path="/api/v1/samples")
    async def get_samples():
        return samples


    @app.put(path="/api/v1/samples")
    async def add_samples(request:Request):
        # request.json
        # 장점 : params 로 받는 것보다 조금 더 빠르다
        # 단점 : 자동으로 제공해주는 swagger 에서 테스트하기 어렵다
        req = await request.json()
        sample_validator.is_valid_put_req(req)
        for k in req:
            samples[k] = req[k]
        return samples

    return app
