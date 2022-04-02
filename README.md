# mlops-gym
A gym type toolkit for developing MLOps solutions. Development began 02/04/2022.

## The Idea
The basic concept of this toolkit will be to emulate the ease o use and extensibility of something like 
[Gym from OpenAI](https://gym.openai.com/). The aim here however will not be to help developers
and data scientists learn reinforcement learning but to help ML and MLOps engineers
build out and test their MLOps pipelines and logic.

This will require the following pieces (in the simplest version, this will be improved upon
at a later date):

- Simulation: We will need to simulation out of sample inferencing as would happen for a model post-deployment.
- Performance Calculation: We need to provide a simple interface to allow users to calculate the performance of their 
models in the simulated scenarios.

Potential other components to explore would be 'Trainers', for testing different retraining schedules and logic 
and 'Alerting' to allow for simulation of alerting to MLOps teams in different scenarios.


## v1.0
The first version of this toolkit will be very basic. This will include some initial notebooks
to show where the concepts come from and how they can be used and focus on simulating extremely
simple models and MLOps pipelines. The first few examples will therefore rely heavily on sklearn.

## Code Design
Work in progress ...

## References/Further Reading
#### MLOps Tools
1. [Seldon](https://www.seldon.io/)
2. [Seldon - Alibi Detect](https://github.com/SeldonIO/alibi-detect)
3. [Monitoring and explainability of models in production, ICML 2020](https://arxiv.org/abs/2007.06299)

#### MLOps Theory

#### ML Engineering
1. [Machine Learning Engineering with Python](https://www.packtpub.com/product/machine-learning-engineering-with-python/9781801079259),
Disclaimer - my book.

## Author
Andy McMahon, author of [Machine Learning Engineering with Python](https://www.packtpub.com/product/machine-learning-engineering-with-python/9781801079259), Packt.
