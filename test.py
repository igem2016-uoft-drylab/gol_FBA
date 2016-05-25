# import these things
from cobra import Model, Reaction, Metabolite, Gene
import cobra.test
import os
import copy
from os.path import join

# create new model from sbml file
eco = cobra.io.sbml.create_cobra_model_from_sbml_file('/home/protoxpire0/Documents/gol_FBA/msb201165-s3.xml',old_sbml=False,legacy_metabolite=False,print_time=False,use_hyphens=False)

print("Creating new_model...")
new_model = Model('new_model')

print("Adding compartment 'a' for 'all'...")
new_model.compartments['a'] = 'all'

print("Adding all metabolites from existing model removing duplications...")
for x in eco.metabolites:
	dup = False
	for y in new_model.metabolites:
		if x.id[:-2] == y.id:
			dup = True
			break
	if dup == False:
		met = copy.deepcopy(x)
		met.id = met.id[:-2]+'_a'
		met.compartment = 'a'
		new_model.add_metabolites({met})

for react in eco.reactions:
	if (react.name.find('transport') == -1 and react.subsystem.find('Transport') == -1 and react.name.find('exchange') == -1 and react.name.find('flippase') == -1  and react.name.find('Sink') == -1):
		for x in react.reactants:
			x.id = x.id[:-2]+'_a'
		for x in react.products:
			x.id = x.id[:-2]+'_a'
		new_model.add_reaction(react)

print len(new_model.reactions)

for react in new_model.reactions:
    for y in new_model.reactions:
        if react.reaction == y.reaction and react.name != y.name:
            y.delete()

print len(new_model.reactions)

#print("Writing to SBML file 'eco_new_model.xml'...")
#cobra.io.write_sbml_model(new_model, "eco_new_model.xml",sbml_level=2,sbml_version=1,print_time=False,use_fbc_package=False)
