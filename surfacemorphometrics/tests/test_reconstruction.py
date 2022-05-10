from imod.protocols import ProtImodTomoNormalization
from pyworkflow.tests import BaseTest, setupTestProject, DataSet
from pyworkflow.utils import magentaStr
from tomo.protocols import ProtImportTomograms, ProtImportTomomasks

# Trigger tomo dataset definition
from tomo.tests import *

from surfacemorphometrics.protocols import SurfMorphReconstruction


class TestMembraneReconstruction(BaseTest):

    outputPath = None
    ds = None
    boxSize = 44
    samplingRate = 13.68
    nVesicles = 3
    vesiclesPackagesSize = 3
    inTomoSet = None
    inTomoSetBinned = None
    inTomomaskSetBinned = None

    @classmethod
    def setUpClass(cls):
        setupTestProject(cls)
        ds = DataSet.getDataSet('emd_10439')
        cls.ds = ds
        cls.inTomoSet = cls._importTomograms()
        cls.inTomoSetBinned = cls._normalizeTomo()
        cls.inTomomaskSetBinned = cls._ImportTomoMasks()

    @classmethod
    def _importTomograms(cls):
        print(magentaStr("\n==> Importing data - tomograms:"))
        protImportTomogram = cls.newProtocol(ProtImportTomograms,
                                             filesPath=cls.ds.getFile('tomoEmd10439'),
                                             samplingRate=cls.samplingRate)

        cls.launchProtocol(protImportTomogram)
        outputTomos = getattr(protImportTomogram, 'outputTomograms', None)
        cls.assertIsNotNone(outputTomos, 'No tomograms were genetated.')

        return outputTomos

    @classmethod
    def _normalizeTomo(cls):
        print(magentaStr("\n==> Tomogram normalization:"))
        protTomoNormalization = cls.newProtocol(ProtImodTomoNormalization,
                                                inputSetOfTomograms=cls.inTomoSet,
                                                binning=2)

        cls.launchProtocol(protTomoNormalization)
        outputTomos = getattr(protTomoNormalization, 'outputSetOfTomograms', None)
        cls.assertIsNotNone(outputTomos, 'No tomograms were generated in tomo normalization.')

        return outputTomos

    @classmethod
    def _ImportTomoMasks(cls):
        print(magentaStr("\n==> Importing data - tomoMasks"
                         ":"))
        protImportTomomasks = cls.newProtocol(ProtImportTomomasks,
                                              filesPath=cls.ds.getFile('tomomaskAnnotated'),
                                              inputTomos=cls.inTomoSetBinned)

        cls.launchProtocol(protImportTomomasks)
        tomoMaskSet = getattr(protImportTomomasks, 'outputTomoMasks', None)
        cls.assertIsNotNone(tomoMaskSet, 'No tomograms were generated.')

        return tomoMaskSet


    def test_membrane_reconstruction(self):

        reconstruction = self.newProtocol(SurfMorphReconstruction,
                         inputSegmentation = self.inTomomaskSetBinned)

        self.launchProtocol(reconstruction)

        # TODO: do the assertions
        #self.assertSetSize(reconstruction.outputMeshes, 3)
        # ...
