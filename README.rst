TAGOOS : associated tag SNP boosting 
---------------------------------------------

.. image:: https://readthedocs.org/projects/tagoos/badge/?version=latest
    :target: http://tagoos.readthedocs.io/en/latest/?badge=latest

We provide two set of intronic and intergenic TAGOOS scores. The TAGOOS underlying model has been trained with the XGBOOST algorithm using intronic and intergenic associated SNPs (GWAS P-value < 10e-8) from the GRASP database. The predictive variables have been selected by the learning algorithm among 4684 gene regulation related annotations such as histone modifications, eQTLs or transcription factors in different tissues from the Expressed enhancers, ENCODE, GTEx, ReMap, RoadMap and H3K27ac data sets.


Documentation
--------------

The `TAGOOS score documentation <http://tagoos.readthedocs.org/>`_ with user guide and
API reference is hosted at Read The Docs.

To build the documentation, it is better to create a conda environment:

.. code-block:: bash

    conda create --name tagoos python=3.5
    pip install sphinx sphinx_rtd_theme recommonmark


Then run *make html* in the *docs* folder

Developer Documentation
----------------------------

Run this command and open *docs_developer/manual.html* in a browser

.. code-block:: bash

    pandoc -s -S --toc -c buttondown.css $PWD/docs/*.md >$PWD/docs/manual.html

