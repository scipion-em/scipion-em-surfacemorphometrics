====================================
Scipion surface morphometrics plugin
====================================

Integrates `surface morphometrics software <https://github.com/GrotjahnLab/surface_morphometrics>`_ into **scipion**

=================================
Steps to install it in devel mode
=================================


**Clone it:**

.. code-block::

    git clone https://github.com/scipion-em/scipion-em-surfacemophometrics.git

**Install it in editable/devel mode**

.. code-block::

    scipion3 installp -p /home/me/scipion-em-surfacemophometrics --devel

TIP: If installation fails, you can access pip options like:

.. code-block::

    scipion3 python -m pip ... (list, install, uninstall)

**Run tests**

.. code-block::

    scipion3 tests --grep surfacemorphometrics --run

    scipion3 last  # will show the last project, typically the one created by the test

