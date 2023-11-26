import uvicorn

from plantapop import CONFIGMAP, create_app, init_models
import asyncio

app = create_app()


def main():
    uvicorn.run(
        "plantapop.__main__:app",
        host=CONFIGMAP.HOST,
        port=CONFIGMAP.PORT,
        reload=CONFIGMAP.RELOAD,
        workers=CONFIGMAP.WORKERS,
    )


if __name__ == "__main__":
    asyncio.run(init_models())
    main()
