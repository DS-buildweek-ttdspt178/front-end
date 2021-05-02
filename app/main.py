from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pathlib import Path
import uvicorn

# from .app import db, ml, viz


BASE_DIR = Path(__file__).parent  # this meant the app directory
# description = """
# Edit your app's title and description. See [https://fastapi.tiangolo.com/tutorial/metadata/](https://fastapi.tiangolo.com/tutorial/metadata/)
#
# To use these interactive docs:
# - Click on an endpoint below
# - Click the **Try it out** button
# - Edit the Request body or any parameters
# - Click the **Execute** button
# - Scroll down to see the Server response Code & Details
#
# We'll use the [Palmer Penguins](https://github.com/allisonhorst/palmerpenguins) dataset. It's an alternative to [Iris](https://en.wikipedia.org/wiki/Iris_flower_data_set). Instead of using Iris flower measurements to predict one of three species, we'll use penguin measurements to predict one of three species.
#
# <img src="https://raw.githubusercontent.com/allisonhorst/palmerpenguins/master/man/figures/lter_penguins.png" width="50%" />
#
# Artwork by [@allison_horst](https://twitter.com/allison_horst)
#
#
# """

# app = FastAPI(
#     title='🏠 AirBnB Rent Prediction API',
#     # description=description,
#     docs_url='/',
#     version='1.0.0',
# )

app = FastAPI()
#
# app.include_router(db.router, tags=['Database'])
# app.include_router(ml.router, tags=['Machine Learning'])
# app.include_router(viz.router, tags=['Visualization'])

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=['*'],
#     allow_credentials=True,
#     allow_methods=['*'],
#     allow_headers=['*'],
# )
app.mount(
    "/static",
    StaticFiles(directory=BASE_DIR / "static"),
    name="static",
)

templates = Jinja2Templates(directory=BASE_DIR / "templates")


@app.get("/")
def home_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/landing.html")
def home_page(request: Request):
    return templates.TemplateResponse("landing.html", {"request": request})


if __name__ == '__main__':
    uvicorn.run(app)
