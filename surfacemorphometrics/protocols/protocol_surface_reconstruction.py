# -*- coding: utf-8 -*-
# **************************************************************************
# *
# * Authors:     you (you@yourinstitution.email)
# *
# * your institution
# *
# * This program is free software; you can redistribute it and/or modify
# * it under the terms of the GNU General Public License as published by
# * the Free Software Foundation; either version 2 of the License, or
# * (at your option) any later version.
# *
# * This program is distributed in the hope that it will be useful,
# * but WITHOUT ANY WARRANTY; without even the implied warranty of
# * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# * GNU General Public License for more details.
# *
# * You should have received a copy of the GNU General Public License
# * along with this program; if not, write to the Free Software
# * Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA
# * 02111-1307  USA
# *
# *  All comments concerning this program package may be sent to the
# *  e-mail address 'you@yourinstitution.email'
# *
# **************************************************************************


"""
Code for the surface reconstruction method
"""
from pwem.protocols import EMProtocol
from pyworkflow.protocol import params
from pyworkflow.utils import Message

from surfacemorphometrics import Plugin


class SurfMorphReconstruction(EMProtocol):
    """
    This protocol will print hello world in the console
    IMPORTANT: Classes names should be unique, better prefix them
    """
    _label = 'reconstruction'

    # -------------------------- DEFINE param functions ----------------------
    def _defineParams(self, form):
        """ Define the input parameters that will be used.
        Documentation here: https://scipion-em.github.io/docs/docs/developer/creating-a-protocol#creating-a-protocol
        Params:
            form: this is the form to be populated with sections and params.
        """
        # You need a params to belong to a section:
        form.addSection(label=Message.LABEL_INPUT)
        form.addParam('inputSegmentation', params.PointerParam,
                      pointerClass='SetOfTomoMasks',
                      label='Segmentation set',
                      help='Segmentation set like those generated by tomosegmemTV')

        # TODO: Add necessary parameters


    # --------------------------- STEPS functions ------------------------------
    def _insertAllSteps(self):
        # Insert processing steps
        self._insertFunctionStep(self.generateConfig)
        self._insertFunctionStep(self.reconstruct)

    def generateConfig(self):

        #TODO:  Do whatever is necessary to prepare a folder/s previous to run reconstruction method
        with open(self._getTmpPath("config.yml"),"w") as fh:
            fh.write("something here")


    def reconstruct(self):
        #TODO: Call reconstruct method: --> python segmentation_to_meshes.py config.yml
        self.runJob(Plugin.composeCommand("pip"), "list")

        print(Plugin.getScriptsPath())

        # This assumes cwd is in the git repo root path.
        self.runJob(Plugin.composeCommand("python segmentation_to_meshes.py"),  "config.yml", cwd=Plugin.getScriptsPath())


    # --------------------------- INFO functions -----------------------------------
    def _summary(self):
        """ Summarize what the protocol has done"""
        summary = []

        # Fill the summary (list of strings)
        return summary

    def _methods(self):
        methods = []

        # Fill the methods (list of strings)

        return methods
