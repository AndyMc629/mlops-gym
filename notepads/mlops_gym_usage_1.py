"""
Aiming to outline some example logic I want to build. Assuming some base functionality in main classes obviously.
Began: 10/4/2022
Author: Andy McMahon
"""

import mlops_gym
import sklearn ... etc etc

from datalasses import dataclass
from typing import Dict

import pandas as pd

@dataclass
class MonitorParameters:
	"""Class for keeping track of monitor parameters"""
	metric_name: str
	metric_bounds: dict # assume 'upper' and 'lower' keys
	

if __name__ == "__main__":
	X_train, X_test, y_train, y_test = ...
	
	# Define the model
	model = sklearn.linear_model().linearRegressor().train(X)
	
	def trigger_alert_logic_batch(monitor_params: MonitorParameters, result_data_set: pd.DataFrame) -> int:
		trigger_on_number_of_breaches = 10
		if len(result_data_set[monitor_params.metric_name] > monitor_params.metric_bounds['upper']) > trigger_on_number_of_breaches:
			return 1
		elif len(result_data_set[monitor_parames.metric_name] < monitor_params.metric_bounds['lower']) > trigger_on_number_of_breaches:
			return 1
		else:
			return 0
		
	def trigger_alert_logic_api(monitor_params: MonitorParameters, result: float) -> int:
		if	result > monitor_params.metric_bounds['upper']:
			return 1
		elif result < monitor_params.metric_bounds['lower']:
			return 1
		else:
			return 0
	
	# Define the model monitor logic
	monitor_params = MonitorParameters(
		metric_name = 'recall', 
		metric_bounds = {'upper': 0.9,'lower': 0.6}, 
	)
	api_monitor = mlops_gym.monitor.RESTAPIMonitor(
		monitor_parameters = monitor_params,
		alert_logic = trigger_alert_logic_api # need to think about how this interacts with the model and simulator objects ...	
	)
	
	# Create simulator using similar syntax to open ai gym 
	# simulator = mlops_gym.make('RestAPIInference-v1') 
	# OR (my preference)
	# Create simulator using simple class object instantiation
	simulator = mlops_gym.simulator.RESTAPISimulator(
		model = model, 
		batch_size=1, 
		run_events=1000,
		inference_data_set = X_test #idea to iterate through this?
		monitor = monitor
	)
	
	# run the simulation
	simulator.run()
	
	"""
	Assumed terminal (and log) output
	
	
	$ running simulation with:
	
		model = model, #maybe provide the type?
		batch_size=1, 
		run_events=1000,
		inference_data_set = X_test #idea to iterate through this?
		monitor = monitor
	
	$ iteration 50:
		 alerts_triggered: 0
		 result_dataset: ./run_10_04_2022_{UID}_results_1.csv
		 alert_output: ./run_10_04_2022_{UID}_alerts_1.csv
		
	$ iteration 100:
		 alerts_triggered: 3
		 result_dataset: ./run_10_04_2022_{UID}_result_2.csv
		 alert_output: ./run_10_04_2022_{UID}_alerts_2.csv
		
	$ iteration 150:
		 alerts_triggered: 3
		 result_dataset: ./run_10_04_2022_{UID}_result_2.csv
		 alert_output: ./run_10_04_2022_{UID}_alerts_2.csv
		
		
	"""
	
	
	
	
	
	
	
	