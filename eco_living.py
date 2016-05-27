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
eco = cobra.io.sbml.create_cobra_model_from_sbml_file("/home/xuleon1/Desktop/iGEM/gol_FBA-1/msb201165-s3.xml",old_sbml=False,legacy_metabolite=False,print_time=False,use_hyphens=False)

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

# change lower bounds for exchange reactions specified in KU Leuven 2013
rxn_to_lb = {}

with open("exchange_rxn_names.txt") as exchange_rxns:
    for line in exchange_rxns:
        line = line.rstrip("\n").split(",")

        rxn_to_lb[line[0] + " exchange"] = float(line[1])

raw_input("Press enter to continue...")

for rxn in eco.reactions:
    if rxn.name in rxn_to_lb:
	print(rxn.name)
        rxn.lower_bound = rxn_to_lb[rxn.name]

print("Writing to SBML file 'eco_living2.xml'...")
cobra.io.write_sbml_model(eco, "eco_living2.xml",sbml_level=2,sbml_version=1,print_time=False,use_fbc_package=False)
