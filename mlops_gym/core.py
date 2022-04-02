from abc import ABC, abstractmethod
from typing import Generic, Optional, SupportsFloat, Tuple, TypeVar, Union #will work on type hinting later

import mlops_gym
#from mlops_gym import models

class Simulator(ABC):
    """Main mlops-gym class. Similarly to in OpenAI gym this will act as a representation of a system with
    arbitrarily complex dynamics in the background. In this case, we refer to the detailed implementation of the ML
    model being run in a production setting. Here we just simulate the process of a prediction running from the
    model and then later of getting true labels for predicted data (or similar).

    API methods of importance will be:

    - model_predict
    ...

    Will need the following attributes:

    - model
    ...
    """

    def __init__(self, model):
        self.model = model

    @abstractmethod
    def model_predict(self):
        pass
        #return self.model.predict() # assume the model has a 'predict' method ... or enforce through a base class?
