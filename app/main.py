from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from app import db, ml, viz

description = """
Edit your app's title and description. See [https://fastapi.tiangolo.com/tutorial/metadata/](https://fastapi.tiangolo.com/tutorial/metadata/)

To use these interactive docs:
- Click on an endpoint below
- Click the **Try it out** button
- Edit the Request body or any parameters
- Click the **Execute** button
- Scroll down to see the Server response Code & Details

We'll use the [Palmer Penguins](https://github.com/allisonhorst/palmerpenguins) dataset. It's an alternative to [Iris](https://en.wikipedia.org/wiki/Iris_flower_data_set). Instead of using Iris flower measurements to predict one of three species, we'll use penguin measurements to predict one of three species.

<img src="https://raw.githubusercontent.com/allisonhorst/palmerpenguins/master/man/figures/lter_penguins.png" width="50%" />

Artwork by [@allison_horst](https://twitter.com/allison_horst)


"""

app = FastAPI(
    title='🐧 Penguin Predictor API',
    description=description,
    docs_url='/',
    version='1.0.0',
)

app.include_router(db.router, tags=['Database'])
app.include_router(ml.router, tags=['Machine Learning'])
app.include_router(viz.router, tags=['Visualization'])

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

if __name__ == '__main__':
    uvicorn.run(app)
