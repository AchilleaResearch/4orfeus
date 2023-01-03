# JZB20220102 Experimenting with PSS/E's python API
import psse35
psse35.set_minor(5)
exam_path = psse35.EXAM_PATH 

# The following are compiled python files (.pyc) so pylance cannot resolve the imports
import psspy
import excelpy
psspy.psseinit()

# Read RAW file and solve
fname = 'Texas7k_20220923.RAW'
psspy.read(0, 'TAMU/'+fname)
psspy.fnsl([1,1,1,1,1,0,0,0])

# Get bus numbers and names for the entire system
ierr, bus_names = psspy.abuschar(-1, 2, 'NAME')
ierr, bus_nums = psspy.abusint(-1, 2, 'NUMBER')
print('Total number of buses in the file: %d' %len(bus_nums[0]))

# Get area numbers and names
ierr, area_nums = psspy.aareaint(-1, 2, 'NUMBER')
ierr, area_names = psspy.aareachar(-1, 2, 'AREANAME')

# iterate over areas: define bussysbstems for each and count the number of buses
buscnt=0
for sid, (anum,aname) in enumerate(zip(area_nums[0], area_names[0])):
    ierr = psspy.bsys(sid=sid, numarea=1, areas=[anum])
    ierr, bus_names_1 = psspy.abuschar(sid, 2, 'NAME')
    ierr, bus_nums_1 = psspy.abusint(sid, 2, 'NUMBER')
    print('Total number of buses in area %s: %d' %(aname, len(bus_nums_1[0])))
    buscnt += len(bus_nums_1[0])

print("Total number of buses from areas: %d" %buscnt)

fexcel = excelpy.workbook(xlsfile='output/' + fname.rsplit('.',1)[0], 
                        sheet='Buses',
                        overwritesheet=True,
                        mode='w')

fexcel.set_cell('A1', 'Number')
fexcel.set_cell('B1', 'Name')
fexcel.set_range(topRow=2, leftCol=1, 
                 data=[bus_nums[0], bus_names[0]],
                 transpose=True
                 )
fexcel.worksheet_add_end('Areas', overwritesheet=True)
fexcel.set_active_sheet('Areas')
fexcel.set_cell('A1', 'Number')
fexcel.set_cell('B1', 'Name')
fexcel.set_range(topRow=2, leftCol=1, 
                 data=[area_nums[0], area_names[0]],
                 transpose=True
                 )
fexcel.save()
fexcel.close()

print('exiting')
