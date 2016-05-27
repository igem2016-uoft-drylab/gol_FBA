###Name: eco_living.py
###Objective: Recreate a ecoli model with the beta-gal-cleave-rxn
###Date Created: May 27, 2016
###Date Last Modified: May 27, 2016
###Contributors: Fahim, Zakary, Heba, Mike, Zian

# import these things
from cobra import Model, Reaction, Metabolite, Gene
import cobra.test
import os
import copy
from os.path import join

# create new model from sbml file
print("importing the existing the ecoli model...")
eco = cobra.io.sbml.create_cobra_model_from_sbml_file("/home/zion/Documents/gitStuff/igem/gol_FBA/msb201165-s3.xml",old_sbml=False,legacy_metabolite=False,print_time=False,use_hyphens=False)

'''          ignoring the following block of code
print("Creating new_model...")
new_model = Model('new_model')



print("Adding compartment 'a' for 'all'...")
new_model.compartments['a'] = 'all'

#Adding all metabolites from existing model removing duplications
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

#Adding all reactions excluding transport, exchange, flippase, sink
print("Adding all reactions excluding transport, exchange, flippase, sink...")
for react in eco.reactions:
	if (react.name.find('transport') == -1 and react.subsystem.find('Transport') == -1 and react.name.find('exchange') == -1 and react.name.find('flippase') == -1  and react.name.find('Sink') == -1):
		for x in react.reactants:
			x.id = x.id[:-2]+'_a'
		for x in react.products:
			x.id = x.id[:-2]+'_a'
		new_model.add_reaction(react)
print("Number of reactions in new_model",len(new_model.reactions))

#removing all reactions that are dupliates
print("Removing all duplicate reactions...")
for react in new_model.reactions:
    for y in new_model.reactions:
        if react.reaction == y.reaction and react.name != y.name:
            y.delete()
print("Number of reactions after deleting duplicates: ",len(new_model.reactions))
#'''


# adding necessary metabolites and reactions for biosensor project
print("Adding necessary metabolites and reactions for biosensor project...")

Au_plus = Metabolite('Au_plus', formula='Au', name='Gold(1)',compartment='c')
Au_3plus = Metabolite('Au_3plus', formula='Au', name='Gold(3)',compartment='c')
BGal = Metabolite('BGal', formula='', name='Beta Galactosidase',compartment='c')
CPRG = Metabolite('CPRG', formula='C25H22Cl2O10S', name='chlorophenol-red-B-D-galactopyranoside',compartment='c')
CPR = Metabolite('CPR', formula='C19H12Cl2O5S', name='Chlorophenol Red',compartment='c')
BDGal = Metabolite('BDGal', formula='C6H12O6', name='Beta-D-Galactose',compartment='c')
H2O = eco.metabolites.get_by_id('h2o_c')

reaction = Reaction('BGalCleaveCPRG')
reaction.name = 'B-Gal Cleavage Of CPRG'
reaction.subsystem = ''
reaction.lower_bound = 0.  # default
reaction.upper_bound = 1000.  # default
reaction.objective_coefficient = 0. # default
reaction.add_metabolites({CPRG: -1, H2O: -1, BDGal: 1, CPR: 1})

eco.add_reaction(reaction)

print("Writing to SBML file 'eco_living.xml'...")
cobra.io.write_sbml_model(eco, "eco_living.xml",sbml_level=2,sbml_version=1,print_time=False,use_fbc_package=False)
