"""Machine learning functions"""

import logging
import random
import joblib
from typing import Dict
from fastapi import APIRouter
import pandas as pd
from pydantic import BaseModel, Field, validator, confloat, constr, conint

log = logging.getLogger(__name__)
router = APIRouter()

# classifier = joblib.load('app/classifier.joblib')
# print('Pickled model loaded')


# class Penguin(BaseModel):
#     """Data Model to parse and validate penguins measurements"""
#     bill_length_mm: confloat(gt=32, lt=60)
#     bill_depth_mm: confloat(gt=13, lt=22)
#
#     def to_df(self):
#         return pd.DataFrame([dict(self)])
#
# @router.post('/predict')
# def predict_species(penguin: Penguin):
#     """Predict penguin species from bill length and depth"""
#     species = classifier.predict(penguin.to_df())
#     return species[0]


pipeline = joblib.load('app/pipeline.joblib')
print('Pickled model loaded')


class Airbnb(BaseModel):
    neighbourhood_group: constr()
    latitude: confloat(gt=18, le=48)
    longitude: confloat(gt=-119, le=-72)
    room_type: constr()
    minimum_nights: conint(ge=1, le=1250)
    number_of_reviews: conint(ge=1, le=840)
    reviews_per_month: confloat(ge=0.01, le=34)
    calculated_host_listings_count: conint(ge=1, le=284)
    availability_365: conint(ge=0, le=365)
    city: constr()

    def to_df(self):
        return pd.DataFrame([dict(self)])


@router.post('/predict')
def predict_rent(rent: Airbnb):
    """Predict the optimal rent for an AirBnb Landlord renting"""
    predict = pipeline.predict(rent.to_df())
    return predict[0]


@router.get('/random')
def random_penguin():
    """Return a random penguin species"""
    return random.choice(['Adelie', 'Chinstrap', 'Gentoo'])
