.. TAGOOS documentation master file, created by
   sphinx-quickstart on Wed Mar 21 08:04:45 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

TAGOOS : associated tag SNP boosting 
======================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   content/ucsc
   content/scores
   content/download

TAGOOS is a nucleotide scoring tool for non-coding (Intronic and intergenic) regions. There are two underlying models trained with the `XGBOOST <https://xgboost.readthedocs.io/en/latest/>`_ algorithm using intronic and intergenic associated SNPs (GWAS P-value < :math:`5\cdot10^{-8}`) from the `GRASP <https://grasp.nhlbi.nih.gov/Overview.aspx>`_ database. The predictive variables have been selected by the learning algorithm among 4684 gene regulation related annotations such as histone modifications, eQTLs or transcription factors in different tissues from these databases:

- `Expressed enhancers <http://enhancer.binf.ku.dk/presets/>`_
- `ENCODE <https://www.encodeproject.org/>`_
- `GTEx <https://www.gtexportal.org/home/>`_
- `ReMap <http://tagc.univ-mrs.fr/remap/>`_
- `RoadMap <href="http://www.roadmapepigenomics.org/>`_
- `H3K27ac from the Young lab <href="http://www.cell.com/abstract/S0092-8674(13)01227-0>`_

The scores can be `downloaded <content/download.html>`_ or accessed remotely using:

- `UCSC (Remote) <content/ucsc.html>`_
- `Tabix (Remote and local) <content/scores.html>`_

Indices and tables
====================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
