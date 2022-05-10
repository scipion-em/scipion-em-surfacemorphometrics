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
# *  e-mail address 'scipion@cnb.csic.es'
# *
# **************************************************************************

import pwem
from scipion.install.funcs import VOID_TGZ

# Constants
DEFAULT_VERSION = "github"
SURFACEMORPHOMETRICS = 'surfacemorphometrics'
SURFACE_MORPH_HOME = "SURFACE_MORPH_HOME"
SURFACE_MORPH_ENV_NAME = "SURFACE_MORPH_ENV_NAME"
DEFAULT_ENV_NAME = "morphometrics"  ## This is the name defined inside the yaml use when creating the environment
INSTALLED_TXT = "installed.txt"

# end of constants. Could be moved to a constants module.


_logo = "icon.png"
_references = ['benjamin2022']


class Plugin(pwem.Plugin):
    _url = "https://github.com/scipion-em/scipion-em-surfacemorphometrics"
    _homeVar = SURFACE_MORPH_HOME

    @classmethod
    def _defineVariables(cls):
        cls._defineVar(SURFACE_MORPH_ENV_NAME, DEFAULT_ENV_NAME)
        cls._defineEmVar(SURFACE_MORPH_HOME, SURFACEMORPHOMETRICS+"-"+DEFAULT_VERSION)

    @classmethod
    def composeCommand(cls, command):
        """ Runs the command passed, having previously activated the environment"""
        cmd = cls.getCondaActivationCmd()
        cmd += "conda activate %s &&" % cls.getEnvName()
        cmd += command

        return cmd

    @classmethod
    def getEnvName(cls):
        return cls.getVar(SURFACE_MORPH_ENV_NAME)

    @classmethod
    def getScriptsPath(cls):
        return cls.getHome("surface_morphometrics")

    @classmethod
    def defineBinaries(cls, env):
        """ Defines how to install third party software"""

        # Commands to install surface morphometrics software from github
        commands = []
        commands.append(("git clone https://github.com/grotjahnlab/surface_morphometrics.git", "surface_morphometrics"))
        commands.append((cls.getCondaActivationCmd() +
                      " cd surface_morphometrics"
                      " && conda env create -f environment.yml"
                      " && conda activate " + DEFAULT_ENV_NAME +
                      " && pip install -r pip_requirements.txt"
                      " && cd .. && touch " + INSTALLED_TXT, [INSTALLED_TXT]))

        env.addPackage(SURFACEMORPHOMETRICS, version=DEFAULT_VERSION,
                       commands=commands,
                       tar=VOID_TGZ,
                       default=True)


