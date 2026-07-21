import uvicorn
from fastapi import FastAPI


async def lifespan() -> None:  # function for start and end of app
    pass


app: FastAPI = FastAPI(lifespan=lifespan)  # type: ignore /now for minimal root of project

if __name__ == "__main__":
    """
    uvicorn run to start app with one click
    reload argument for reloading server on save event
    """
    uvicorn.run("main:app", reload=True)
