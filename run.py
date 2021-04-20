import uvicorn, cfg

if __name__ == '__main__':
    uvicorn.run(
        "application.main:app",
        host=cfg.API_HOST,
        port=cfg.API_PORT,
        workers=cfg.API_WORKERS
    )