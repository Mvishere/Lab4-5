from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# 1. Define the structure
model = BayesianNetwork([('Rain', 'Sprinkler'), 
                         ('Rain', 'WetGrass'), 
                         ('Sprinkler', 'WetGrass')])

# 2. Define CPDs
cpd_rain = TabularCPD(variable='Rain', variable_card=2, values=[[0.7], [0.3]])  # 0: No, 1: Yes
cpd_sprinkler = TabularCPD(variable='Sprinkler', variable_card=2,
                           values=[[0.6, 0.1],  # Sprinkler = 0
                                   [0.4, 0.9]], # Sprinkler = 1
                           evidence=['Rain'], evidence_card=[2])

cpd_wetgrass = TabularCPD(variable='WetGrass', variable_card=2,
                          values=[[1, 0.1, 0.1, 0.01],  # WetGrass = 0
                                  [0, 0.9, 0.9, 0.99]], # WetGrass = 1
                          evidence=['Rain', 'Sprinkler'], evidence_card=[2, 2])

# 3. Add CPDs to the model
model.add_cpds(cpd_rain, cpd_sprinkler, cpd_wetgrass)

# 4. Verify the model
print("Is model valid?", model.check_model())

# 5. Do inference
infer = VariableElimination(model)
prob = infer.query(variables=['Rain'], evidence={'WetGrass': 1})
print(prob)
