"""Machine learning functions"""

import logging
import random
import joblib
from typing import Dict
from fastapi import APIRouter
import pandas as pd
from pydantic import BaseModel, Field, validator, confloat

log = logging.getLogger(__name__)
router = APIRouter()

classifier = joblib.load('app/classifier.joblib')
print('Pickled model loaded')


class Penguin(BaseModel):
    """Data Model to parse and validate penguins measurements"""
    bill_length_mm: confloat(gt=32, lt=60)
    bill_depth_mm: confloat(gt=13, lt=22)

    def to_df(self):
        return pd.DataFrame([dict(self)])


@router.post('/predict')
def predict_species(penguin: Penguin):
    """Predict penguin species from bill length and depth"""
    species = classifier.predict(penguin.to_df())
    return species[0]


@router.get('/random')
def random_penguin():
    """Return a random penguin species"""
    return random.choice(['Adelie', 'Chinstrap', 'Gentoo'])
