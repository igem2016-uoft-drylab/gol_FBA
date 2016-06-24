###Name: optmodel.py
###Objective: python script to optimize a model by taking arguments: status/summary
###Date Created: May 24, 2016
###Date Last Modified: May 25, 2016
###Contributors: Fahim

import sys
import cobra.test
import os
import pandas
from os.path import join

model_name = sys.argv[1]

#print("importing the SBML file... {}".format(model_name))
model = cobra.io.sbml.create_cobra_model_from_sbml_file('{}'.format(model_name),old_sbml=False,legacy_metabolite=False,print_time=False,use_hyphens=False)

model.repair()

#model.objective = "BGalCleaveCPRG"
#print "model objective is ", model.objective

#print("model is being optimized... ")
model.optimize()
#print("model optimized... ")

if "summary" in sys.argv:
	#print("model's status is: " + model.solution.status)
	#print("model's summary: ")
	summary = model.summary(digits=6,threshold=1E-8)

if "status" in sys.argv:
	print("model's status is: " + model.solution.status)
