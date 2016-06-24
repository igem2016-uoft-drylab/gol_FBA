file = open("../eco_cell_output",'r')
next(file)

influx_id = open("influx_id",'w')
outflux_id = open('outflux_id','w')

influx_name = open("influx_name",'w')
outflux_name = open('outflux_name','w')

influx = []
outflux = []

for line in file:
    split_line = line.split()
    influx.append(split_line[0])
    if (len(split_line) > 2):
        outflux.append(split_line[2])

for i in influx:
    influx_id.write("NODE\t" + i + "_in\n")
    influx_id.write("NODE\t" + i + "_out\n")

for i in outflux:
    outflux_id.write("NODE\t" + i + "_in\n")
    outflux_id.write("NODE\t" + i + "_out\n")
