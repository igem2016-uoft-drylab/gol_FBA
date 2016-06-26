file = open("../eco_cell_output",'r')
next(file)

flux_data = open("flux_data",'w')
fluxes = open('fluxes','w')

flux_name = open("flux_name",'w')

influx = []
outflux = []

for line in file:
    split_line = line.split()
    influx.append(split_line[0])
    if (len(split_line) > 2):
        outflux.append(split_line[2])

flux_data.write("NODE\t" + "CYTO" + "\n")
flux_data.write("NODE\t" + "EX" + "\n")
flux_data.write("IN\t" + "CYTO\t" + "EX\n")

for i in influx:
	fluxes.write(i+"\n")
	flux_data.write("NODE\t" + i + "\n")
	flux_data.write("NODE\t" + i[:-2] + "_c\n")
	flux_data.write("IN\t" + i[:-2] + "_c\t" + "CYTO\n")
	flux_data.write("EDGE\t" + i + "\t" + i[:-2] + "_c\n")

for o in outflux:
	fluxes.write(o + "\n")
	flux_data.write("NODE\t" + o + "\n")
	flux_data.write("IN\t" + o + "\tEX\n")
	flux_data.write("EDGE\t" + o + "\tCYTO\n")

