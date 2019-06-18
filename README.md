My pipelines for commonly processed NGS data, some were mixed with plot functions, designed with Python and parallel computating. Maybe not stable and may need adjustment for specific jobs.
Major design idea: one folder one file type, 1.fastq -> 2.bam -> 3.bedpe -> 4.bw, for example bam2bedpe.py can work for 2.bam->3.bedpe.

---
## Common
Non-specific scripts for propressing NGS data. 
Mapping DNA sequenes to genome: [dnaMapping](https://github.com/YaqiangCao/ngsPipes/blob/master/common/dnaMapping.py)

---
## MNase
Specific scripts for analysis of MNase-seq data.

---
## Plot

---
## Updates
