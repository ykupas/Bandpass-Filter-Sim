## EMerge simulation - S11
#
#
import emerge as em
import numpy as np
from emerge.plot import smith, plot_sp

from basicemergesolverhelperpackage import EMergeHelperFunctions
from basicemergesolverhelperpackage.EMergeConstants import *

simulationObj = em.Simulation("bandpass-filter", load_file=True)
simulationResult = simulationObj.data.mw
helperFunctionsObj = EMergeHelperFunctions(simulationObj)

###############################################################################
# PORT NAME AND THEIR NUMBERS LIST
###############################################################################
portNamesAndNumbersList = {}
portNamesAndNumbersList["PortIn"] = 1
portNamesAndNumbersList["PortOut"] = 2

###############################################################################
# PLOT S DATA
###############################################################################
sourcePortName = 'PortIn'
sourcePortNumber = portNamesAndNumbersList[sourcePortName]

# Generate touchstone file available since EMerge 2.5.5
simulationResult.scalar.grid.export_touchstone("bandpass-filter.s1p", Z0ref=50, format="RI", funit="GHz")

helperFunctionsObj.exportCSV_SParam("bandpass-filter_s11.csv", sourcePortNumber, sourcePortNumber)
helperFunctionsObj.plotSParamUsingPortNumbers(sourcePortNumber, sourcePortNumber)

