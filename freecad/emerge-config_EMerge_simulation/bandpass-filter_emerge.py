## EMerge simulation
#
#
# To be run with python.
# FreeCAD to OpenEMS plugin but this time it generates EMerge by Lubomir Jagos, 
# see https://github.com/LubomirJagos42/FreeCAD-OpenEMS-Export
#
# This file has been automatically generated. Manual changes may be overwritten.
#

### Import Libraries
import numpy as np
import emerge as em
import os, shutil

from basicemergesolverhelperpackage import EMergeHelperFunctions
from basicemergesolverhelperpackage.EMergeConstants import *

# Change current path to script file folder
#
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
## constants
unit    = 0.001 # Model coordinates and lengths will be specified in mm.
fc_unit = 0.001 # STL files are exported in FreeCAD standard units (mm).


currDir = os.getcwd()
print(currDir)

## prepare simulation folder, if dir exits remove and create new one to be empty
Sim_Path = os.path.join(currDir, 'simulation_output')
if os.path.exists(Sim_Path):
	shutil.rmtree(Sim_Path)   # clear previous directory
	os.mkdir(Sim_Path)    # create empty simulation folder

#######################################################################################################################################
# SIMULATION OBJECT AND HELPER FUNCTIONS OBJECT
#######################################################################################################################################
simulationObj = em.Simulation("bandpass-filter", save_file=True)
helperFunctionsObj = EMergeHelperFunctions(simulationObj)

#######################################################################################################################################
# EXCITATION basic
#######################################################################################################################################
fmin = 50.0*1000000.0
fmax = 200.0*1000000.0
resolution = 0.33
npoints = 50
simulationObj.mw.set_frequency_range(fmin, fmax, npoints)
simulationObj.mw.set_resolution(resolution)

#######################################################################################################################################
# MATERIALS AND GEOMETRY
#######################################################################################################################################
## MATERIAL - DIEL_FR4
helperFunctionsObj.addMaterial('DIEL_FR4', em.Material(name='DIEL_FR4', er=4.4, ur=1, tand=0.015))
helperFunctionsObj.setMaterialColor('DIEL_FR4', color='#476f5e', opacity=0.5)

helperFunctionsObj.importStepFile(name='bandpass-filter_PCB', filename='bandpass-filter_PCB_gen_model.step', directory=[currDir, 'stepfiles'], unit=mm, priority=9500, materialName='DIEL_FR4')

## MATERIAL - PEC
helperFunctionsObj.addMaterial('PEC', em.lib.PEC)
helperFunctionsObj.setMaterialColor('PEC', color='#ff5500', opacity=0.5)

helperFunctionsObj.importStepFile(name='bandpass-filter_top', filename='bandpass-filter_top_gen_model.step', directory=[currDir, 'stepfiles'], unit=mm, priority=9800, materialName='PEC')
helperFunctionsObj.setMaterialColor('PEC', color='#ff5500', opacity=0.5)

helperFunctionsObj.importStepFile(name='bandpass-filter_bot', filename='bandpass-filter_bot_gen_model.step', directory=[currDir, 'stepfiles'], unit=mm, priority=9700, materialName='PEC')
helperFunctionsObj.setMaterialColor('PEC', color='#ff0000', opacity=1.0)

helperFunctionsObj.importStepFile(name='bandpass-filter_via', filename='bandpass-filter_via_gen_model.step', directory=[currDir, 'stepfiles'], unit=mm, priority=9600, materialName='PEC')


# Imported objects used as boundary conditions
#

helperFunctionsObj.importStepFile(name='AirBox', filename='AirBox_gen_model.step', directory=[currDir, 'stepfiles'], unit=mm, priority=8400)


# Imported objects used as lumped elements
#

helperFunctionsObj.importStepFile(name='L4_0.4x0.4mm_c8ab52b80b38', filename='L4_0.4x0.4mm_c8ab52b80b38_gen_model.step', directory=[currDir, 'stepfiles'], unit=mm, priority=8800)
helperFunctionsObj.importStepFile(name='L2_0.4x0.4mm_7f8b2fa9aa8c', filename='L2_0.4x0.4mm_7f8b2fa9aa8c_gen_model.step', directory=[currDir, 'stepfiles'], unit=mm, priority=8900)

helperFunctionsObj.importStepFile(name='C4_0.4x0.4mm_28bab67e7a30', filename='C4_0.4x0.4mm_28bab67e7a30_gen_model.step', directory=[currDir, 'stepfiles'], unit=mm, priority=9000)
helperFunctionsObj.importStepFile(name='C2_0.4x0.4mm_7f1fb867c67d', filename='C2_0.4x0.4mm_7f1fb867c67d_gen_model.step', directory=[currDir, 'stepfiles'], unit=mm, priority=9100)

helperFunctionsObj.importStepFile(name='C3_0.4x0.4mm_09910f838df4', filename='C3_0.4x0.4mm_09910f838df4_gen_model.step', directory=[currDir, 'stepfiles'], unit=mm, priority=8700)

helperFunctionsObj.importStepFile(name='L5_0.4x0.4mm_ee1ea61ba628', filename='L5_0.4x0.4mm_ee1ea61ba628_gen_model.step', directory=[currDir, 'stepfiles'], unit=mm, priority=9200)
helperFunctionsObj.importStepFile(name='L1_0.4x0.4mm_1cc370905fb4', filename='L1_0.4x0.4mm_1cc370905fb4_gen_model.step', directory=[currDir, 'stepfiles'], unit=mm, priority=9300)

helperFunctionsObj.importStepFile(name='C5_0.4x0.4mm_d5de2ac775e6', filename='C5_0.4x0.4mm_d5de2ac775e6_gen_model.step', directory=[currDir, 'stepfiles'], unit=mm, priority=8500)
helperFunctionsObj.importStepFile(name='C1_0.4x0.4mm_8a9f25932c2f', filename='C1_0.4x0.4mm_8a9f25932c2f_gen_model.step', directory=[currDir, 'stepfiles'], unit=mm, priority=8600)

helperFunctionsObj.importStepFile(name='L3_0.4x0.4mm_bb5f473ea771', filename='L3_0.4x0.4mm_bb5f473ea771_gen_model.step', directory=[currDir, 'stepfiles'], unit=mm, priority=9400)


#######################################################################################################################################
# PORTS
#######################################################################################################################################

## PORT - in - PortIn
portStart = [ 1.23672, 3.23915, -0.035 ]
portStop  = [ 1.23672, 4.13508, 0.965 ]
portStart = [k*fc_unit for k in portStart]  #dimension scaled by freecad unit to meters
portStop = [k*fc_unit for k in portStop]  #dimension scaled by freecad unit to meters
w = abs(portStart[0] - portStop[0])
h = abs(portStart[1] - portStop[1])
th = abs(portStart[2] - portStop[2])
#portName: "PortIn" -> portNumber: 1
helperFunctionsObj.addLumpedPort(name='PortIn', portStart=portStart, width=h, height=th, R=50*1, direction=em.ZAX, power=1.0, geometryObject=em.geo.Plate(name='PortIn', origin=portStart, u=[0,h,0], v=[0,0,th]))

## PORT - out - PortOut
portStart = [ 19.7367, 3.23915, -0.035 ]
portStop  = [ 19.7367, 4.13508, 0.965 ]
portStart = [k*fc_unit for k in portStart]  #dimension scaled by freecad unit to meters
portStop = [k*fc_unit for k in portStop]  #dimension scaled by freecad unit to meters
w = abs(portStart[0] - portStop[0])
h = abs(portStart[1] - portStop[1])
th = abs(portStart[2] - portStop[2])
#portName: "PortOut" -> portNumber: 2
helperFunctionsObj.addLumpedPort(name='PortOut', portStart=portStart, width=h, height=th, R=50*1, direction=em.ZAX, power=1.0, geometryObject=em.geo.Plate(name='PortOut', origin=portStart, u=[0,h,0], v=[0,0,th]))

#######################################################################################################################################
# COMPLETE GEOMETRY
#######################################################################################################################################

simulationObj.commit_geometry()

#######################################################################################################################################
# GRID LINES
#######################################################################################################################################
helperFunctionsObj.setObjBoundarySize(name='bandpass-filter_via', size=1.0*mm)
helperFunctionsObj.setObjVolumeSize(name='AirBox', size=5.0*mm)
helperFunctionsObj.setObjFaceSize(name='C1_0.4x0.4mm_8a9f25932c2f', size=0.1*mm)
helperFunctionsObj.setObjFaceSize(name='C3_0.4x0.4mm_09910f838df4', size=0.1*mm)
helperFunctionsObj.setObjFaceSize(name='L2_0.4x0.4mm_7f8b2fa9aa8c', size=0.1*mm)
helperFunctionsObj.setObjFaceSize(name='C5_0.4x0.4mm_d5de2ac775e6', size=0.1*mm)
helperFunctionsObj.setObjFaceSize(name='L4_0.4x0.4mm_c8ab52b80b38', size=0.1*mm)
helperFunctionsObj.setObjFaceSize(name='C2_0.4x0.4mm_7f1fb867c67d', size=0.1*mm)
helperFunctionsObj.setObjFaceSize(name='C4_0.4x0.4mm_28bab67e7a30', size=0.1*mm)
helperFunctionsObj.setObjFaceSize(name='L5_0.4x0.4mm_ee1ea61ba628', size=0.1*mm)
helperFunctionsObj.setObjFaceSize(name='L3_0.4x0.4mm_bb5f473ea771', size=0.1*mm)
helperFunctionsObj.setObjFaceSize(name='L1_0.4x0.4mm_1cc370905fb4', size=0.1*mm)
helperFunctionsObj.setObjBoundarySize(name='bandpass-filter_top', size=1.0*mm)
helperFunctionsObj.setObjBoundarySize(name='bandpass-filter_bot', size=1.0*mm)

#
# First mesh must be created on existing geometry
#
simulationObj.generate_mesh()

#
# Now follows boundary condition definition
#
helperFunctionsObj.setPortAsLumpedPort('PortIn')
helperFunctionsObj.setPortAsLumpedPort('PortOut')

#######################################################################################################################################
# LUMPED PART
#######################################################################################################################################
helperFunctionsObj.setLumpedElementToObject(name='L4_0.4x0.4mm_c8ab52b80b38', impedance_function=parallel_impedance(L=12.0*nH), width=0.3999999999999986*mm, height=0.3999999999999999*mm)
helperFunctionsObj.setLumpedElementToObject(name='L2_0.4x0.4mm_7f8b2fa9aa8c', impedance_function=parallel_impedance(L=12.0*nH), width=0.40000000000000036*mm, height=0.3999999999999999*mm)
helperFunctionsObj.setLumpedElementToObject(name='C4_0.4x0.4mm_28bab67e7a30', impedance_function=parallel_impedance(C=220.0*pF), width=0.3999999999999986*mm, height=0.40000000000000036*mm)
helperFunctionsObj.setLumpedElementToObject(name='C2_0.4x0.4mm_7f1fb867c67d', impedance_function=parallel_impedance(C=220.0*pF), width=0.40000000000000036*mm, height=0.3999999999999999*mm)
helperFunctionsObj.setLumpedElementToObject(name='C3_0.4x0.4mm_09910f838df4', impedance_function=parallel_impedance(C=3.3*pF), width=0.3999999999999986*mm, height=0.3999999999999999*mm)
helperFunctionsObj.setLumpedElementToObject(name='L5_0.4x0.4mm_ee1ea61ba628', impedance_function=parallel_impedance(L=470.0*nH), width=0.3999999999999986*mm, height=0.3999999999999999*mm)
helperFunctionsObj.setLumpedElementToObject(name='L1_0.4x0.4mm_1cc370905fb4', impedance_function=parallel_impedance(L=470.0*nH), width=0.40000000000000036*mm, height=0.40000000000000036*mm)
helperFunctionsObj.setLumpedElementToObject(name='C5_0.4x0.4mm_d5de2ac775e6', impedance_function=parallel_impedance(C=5.6*pF), width=0.3999999999999986*mm, height=0.3999999999999999*mm)
helperFunctionsObj.setLumpedElementToObject(name='C1_0.4x0.4mm_8a9f25932c2f', impedance_function=parallel_impedance(C=5.6*pF), width=0.4000000000000008*mm, height=0.3999999999999999*mm)
helperFunctionsObj.setLumpedElementToObject(name='L3_0.4x0.4mm_bb5f473ea771', impedance_function=parallel_impedance(L=820.0*nH), width=0.3999999999999986*mm, height=0.3999999999999999*mm)

#######################################################################################################################################
# BOUNDARY CONDITIONS PART
#######################################################################################################################################
helperFunctionsObj.setBoundaryConditionToObject(name="AirBox", type="Absorbing")

#######################################################################################################################################
# EXPERIMENT EXPORT MESH WITH NAMED GROUP OF MESH
#######################################################################################################################################
helperFunctionsObj.createGmshNamedGroup('PortIn', 'PortIn')
helperFunctionsObj.createGmshNamedGroup('PortOut', 'PortOut')
helperFunctionsObj.createGmshNamedGroup('bandpass-filter_PCB', 'bandpass-filter_PCB')
helperFunctionsObj.createGmshNamedGroup('bandpass-filter_via', 'bandpass-filter_via')
helperFunctionsObj.createGmshNamedGroup('bandpass-filter_top', 'bandpass-filter_top')
helperFunctionsObj.createGmshNamedGroup('bandpass-filter_bot', 'bandpass-filter_bot')
helperFunctionsObj.createGmshNamedGroup('L5_0.4x0.4mm_ee1ea61ba628', 'L5_0.4x0.4mm_ee1ea61ba628_2D', useBoundary=True)
helperFunctionsObj.createGmshNamedGroup('AirBox', 'AirBox_2D', useBoundary=True)
helperFunctionsObj.createGmshNamedGroup('L2_0.4x0.4mm_7f8b2fa9aa8c', 'L2_0.4x0.4mm_7f8b2fa9aa8c_2D', useBoundary=True)
helperFunctionsObj.createGmshNamedGroup('L1_0.4x0.4mm_1cc370905fb4', 'L1_0.4x0.4mm_1cc370905fb4_2D', useBoundary=True)
helperFunctionsObj.createGmshNamedGroup('C4_0.4x0.4mm_28bab67e7a30', 'C4_0.4x0.4mm_28bab67e7a30_2D', useBoundary=True)
helperFunctionsObj.createGmshNamedGroup('C5_0.4x0.4mm_d5de2ac775e6', 'C5_0.4x0.4mm_d5de2ac775e6_2D', useBoundary=True)
helperFunctionsObj.createGmshNamedGroup('C2_0.4x0.4mm_7f1fb867c67d', 'C2_0.4x0.4mm_7f1fb867c67d_2D', useBoundary=True)
helperFunctionsObj.createGmshNamedGroup('C1_0.4x0.4mm_8a9f25932c2f', 'C1_0.4x0.4mm_8a9f25932c2f_2D', useBoundary=True)
helperFunctionsObj.createGmshNamedGroup('L3_0.4x0.4mm_bb5f473ea771', 'L3_0.4x0.4mm_bb5f473ea771_2D', useBoundary=True)
helperFunctionsObj.createGmshNamedGroup('C3_0.4x0.4mm_09910f838df4', 'C3_0.4x0.4mm_09910f838df4_2D', useBoundary=True)
helperFunctionsObj.createGmshNamedGroup('L4_0.4x0.4mm_c8ab52b80b38', 'L4_0.4x0.4mm_c8ab52b80b38_2D', useBoundary=True)

try:
	os.mkdir('mesh')
except:
	pass
simulationObj.export(os.path.join('mesh', f'bandpass-filter.msh'))

#######################################################################################################################################
# DISPLAY MODEL
#######################################################################################################################################
simulationObj.view()
simulationObj.view(plot_mesh=True, volume_mesh=False)

#######################################################################################################################################
# RUN and save results
#######################################################################################################################################
simulationResult = simulationObj.mw.run_sweep()
simulationObj.save()

