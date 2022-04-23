from abc import ABC, abstractmethod
#from typing import Generic, Optional, SupportsFloat, Tuple, TypeVar, Union #will work on type hinting later
from typing import Dict
import mlops_gym
#from mlops_gym import models
import pandas as pd

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
    # TODO: Add type hinting for this constructor, maybe using
    #  https://stackoverflow.com/questions/44330538/type-annotation-with-multiple-types-in-kwargs
    def __init__(self, **kwargs) -> None:
        #TODO: think of a cleaner way to do this ...
        if 'model' in kwargs.keys():
            self.model = kwargs['model']
        else:
            print('You have not specified a model for this simulator object, specify one to run simulations.')
        # Batch size definitions
        if 'pred_batch_size' in kwargs.keys():
            self.pred_batch_size = kwargs['pred_batch_size']
        else:
            self.pred_batch_size = 1
            print('You have not specified a pred_batch_size, will default this to 1 and assume a call->response scenario.')
        # Number of batches definitions
        if 'num_batches' in kwargs.keys():
            self.num_batches = kwargs['num_batches']
        else:
            self.num_batches = 7 # why not?
            print('You have not specified a num_batches, will default this to 7.')


        # Variables created via methods
        self.simulated_data_frame = self.create_sim_batch_dataframe()

    @abstractmethod
    def model_predict(self):
        pass
        #return self.model.predict() # assume the model has a 'predict' method ... or enforce through a base class?

    # Not abstract as this will always be the same and shouldn't be overwritten
    def create_sim_batch_dataframe(self):
        df = pd.DataFrame(
            data={
                'batch_id': list(range(self.num_batches))*self.pred_batch_size,
                'prediction': None # TODO: check if there's a better default to use?
            }
        ).sort_values('batch_id').reset_index(drop=True)
        return df


    # @abstractmethod
    # def simulate(self):
    #     pass


    # @abstractmethod
    # def tolerance_alert(self) -> Dict:
    #     '''
    #
    #     :return: dict or json objective
    #     '''
    #     pass #does this fail type check?