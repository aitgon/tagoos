Download
===========================

Gzipped BED (bed.gz) and TABIX (bed.gz.tbi) files can be downloaded here:
TAGOOS files

.. list-table:: TAGOOS BED and TBI files
   :widths: 15 10 30
   :header-rows: 1

   * - Size
     - Last modified
     - File name
   * - 1.2G
     - May -26-2018
     - `tagoos_intergenic_hg19.bed.gz <http://pedagogix-tagc.univ-mrs.fr/~gonzalez/tagoos/release/180328/tagoos_intergenic_hg19.bed.gz>`_
   * - 685K
     - May -26-2018
     - `tagoos_intergenic_hg19.bed.gz.tbi <http://pedagogix-tagc.univ-mrs.fr/~gonzalez/tagoos/release/180328/tagoos_intergenic_hg19.bed.gz.tbi>`_
   * - 1.2G
     - May -26-2018
     - `tagoos_intergenic_hg38.bed.gz <http://pedagogix-tagc.univ-mrs.fr/~gonzalez/tagoos/release/180328/tagoos_intergenic_hg38.bed.gz>`_
   * - 684K
     - May -26-2018
     - `tagoos_intergenic_hg38.bed.gz.tbi <http://pedagogix-tagc.univ-mrs.fr/~gonzalez/tagoos/release/180328/tagoos_intergenic_hg38.bed.gz.tbi>`_
   * - 2.0G
     - May -26-2018
     - `tagoos_intronic_hg19.bed.gz <http://pedagogix-tagc.univ-mrs.fr/~gonzalez/tagoos/release/180328/tagoos_intronic_hg19.bed.gz>`_
   * - 754K
     - May -26-2018
     - `tagoos_intronic_hg19.bed.gz.tbi <http://pedagogix-tagc.univ-mrs.fr/~gonzalez/tagoos/release/180328/tagoos_intronic_hg19.bed.gz.tbi>`_
   * - 2.0G
     - May -26-2018
     - `tagoos_intronic_hg38.bed.gz <http://pedagogix-tagc.univ-mrs.fr/~gonzalez/tagoos/release/180328/tagoos_intronic_hg38.bed.gz>`_
   * - 754K
     - May -26-2018
     - `tagoos_intronic_hg38.bed.gz.tbi <http://pedagogix-tagc.univ-mrs.fr/~gonzalez/tagoos/release/180328/tagoos_intronic_hg38.bed.gz.tbi>`_


Column descriptions of bed files

1. Chromosome number with "chr" suffix. It goes from 1 to 22, i.e. no X o Y chromosomes
2. Starting position (zero-based)
3. End position (one-based)
4. Score
5. p-value
6. Negative log with base 10 of the p-value
7. Comma-separated list of annotation variables

Example line for the rs227727 SNP (chr17:54776954-54776955 in hg19 genome) retrieved with `tabix <../content/scores.html>`_

.. code-block:: bash

    chr17	54776954	54776955	0.26526207	0.00279416049738879	2.55374865150445	ahr.mcf7.GSE41820ReMap,atf3.NS.ENCODEReMap,atf7.mcf7.encode2,dnase.bodyofpancreasmaleadult_54years_.encode2,dnase.brainmalefetal_72days_andmalefetal_76days_.encode2,dnase.bronchialepithelialcell.encode2,dnase.daoy.encode2,dnase.esdr_h1_bmp4_meso.roadmap,dnase.fibroblastofupperlegskinmalefetal_12weeks_.encode2,dnase.gastrocnemiusmedialismaleadult_54years_.encode2,dnase.heartfetal_96days_.encode2,dnase.ipsdf19.11malenewborn.encode2,dnase.largeintestinemalefetal_108days_.encode2,dnase.leftkidneyfemalefetal_87days_.encode2,dnase.mg63.encode2,dnase.mus_trnk_fet.roadmap,dnase.skinfibroblastmalefetal_97days_.encode2,dnase.smallintestinemalefetal_108days_.encode2,dnase.stomachmalechild_3years_.encode2,dnase.testismalefetal.encode2,dnase.thyroidglandmaleadult_37years_.encode2,dnase.trophoblastcellfetal_21week_.encode2,dnase.trophoblastcellfetal_23weeks_.encode2,dnase.urinarybladdermalefetal_76days_.encode2,e2f1.NS.ENCODEReMap,egfpzxdb.hek293originatedfromhek293stablyexpressingfusionprotein.encode2,ep300.breastepitheliummaleadult_37years_.encode2,ep300.esophagusmuscularismucosamaleadult_37years_.encode2,ep300.sigmoidcolonmaleadult_37years_.encode2,ep300.suprapubicskinfemaleadult_53years_.encode2,ep300.suprapubicskinmaleadult_54years_.encode2,eqtl.Esophagus_Muscularis.gtex,faireseq.a549.encode2,faireseq.h54.encode2,faireseq.helas3.encode2,faireseq.rcc7860.encode2,h2afz.hct116.encode2,h2afz.imr90femalefetal_16weeks_.encode2,h2afz.inducedpluripotentstemcellmaleadult_53years_originatedfromfibroblastofarm.encode2,h2afz.mcf7.encode2,h2az.brst_hmec.roadmap,h3k27ac.Skeletal_Muscle_Myoblast.youngh3k27ac,h3k27ac.esdr_cd184_endo.roadmap,h3k27ac.esdr_cd56_meso.roadmap,h3k27ac.esdr_h1_msc.roadmap,h3k27ac.foreskinkeratinocytemalenewborn.encode2,h3k27ac.panc1.encode2,h3k27ac.sigmoidcolonfemaleadult_53years_.encode2,h3k27ac.stomachfemaleadult_53years_.encode2,h3k27me3.adrl_glnd_fet.roadmap,h3k27me3.foreskinmelanocytemalenewborn.encode2,h3k27me3.hepg2.encode2,h3k27me3.sknshtreatedwithalltransretinoicacid.encode2,h3k4me1.fat_adip_dr_msc.roadmap,h3k4me1.fat_adip_nuc.roadmap,h3k4me1.gastrocnemiusmedialismaleadult_37years_.encode2,h3k4me1.helas3.encode2,h3k4me1.hues64derivedcd184+.encode2,h3k4me1.mus_sat.roadmap,h3k4me1.muscleoflegfemalefetal_110days_.encode2,h3k4me1.osteoblast.encode2,h3k4me1.stomachfemalefetal_96days_.encode2,h3k4me1.strm_chon_mrw_dr_msc.roadmap,h3k4me1.thoracicaortamaleadult_37years_.encode2,h3k4me2.fibroblastofarmmaleadult_53years_.encode2,h3k4me2.lng_a549_etoh002_cncr.roadmap,h3k4me2.mammaryepithelialcellfemaleadult_50years_.encode2,h3k4me2.vas_huvec.roadmap,h3k4me3.fibroblastofarmmaleadult_53years_.encode2,h3k4me3.mus_hsmmt.roadmap,jun.mcf7.encode2,jund.h1hesc.encode2,max.hela.GSE43227ReMap,polr2a.adrenalglandfemaleadult_51year_.encode2,polr2a.breastepitheliumfemaleadult_51year_.encode2,polr2a.endothelialcellofumbilicalveinnewborn.encode2,polr2aphosphos5.transversecolonfemaleadult_53years_.encode2,zbtb33.NS.ENCODEReMap




