from typing import List, Optional
from pydantic import BaseModel


class SensorModel(BaseModel):
    sensorId: str
    voltage: int
    battery: int
    signal: int

