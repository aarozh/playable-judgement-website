"""Judgement development configuration."""

import pathlib
import os

SECRET_KEY = os.urandom(24)

JUDGEMENT_ROOT = pathlib.Path(__file__).resolve().parent.parent

DATABASE_FILENAME = JUDGEMENT_ROOT/'instance'/'judgement.sqlite'