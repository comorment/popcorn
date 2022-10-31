# popcorn project

Singularity wrapper for https://github.com/brielin/Popcorn (the version updated May 2022 based on Python3).

Brief getting started instructions, which should execute built-in example provided together with popcorn software:

```
singularity shell --home $PWD:/home containers/popcorn.sif
cp /tools/popcorn/test/* .
./test.bash
```

For EUR and EAS populations the reference files are included in ``reference`` folder.

## Important! - Set up Git LFS before cloning this repository

Have a look [here](https://github.com/comorment/containers/blob/main/README.md#getting-started) if you're new to git or Git LFS.

## Creating a reference

An easy start for making your own reference files would be to download 1kG data as processed in [MAGMA](https://ctg.cncr.nl/software/magma):

```
wget https://ctg.cncr.nl/software/MAGMA/ref_data/g1000_eas.zip --no-check-certificate
wget https://ctg.cncr.nl/software/MAGMA/ref_data/g1000_afr.zip --no-check-certificate
wget https://ctg.cncr.nl/software/MAGMA/ref_data/g1000_eur.zip --no-check-certificate
```

To select individuals from 1kG sub-populations you may use the [1000GP_Phase3.sample](https://github.com/comorment/popcorn/blob/main/reference/1000GP_Phase3.sample) file, as in the following example where we select ``ASW`` sub-population.
After that it's a good idea to exclude MHC region, and filter on MAF.

```
# ASW sub-population
cat 1000GP_Phase3.sample | grep ASW | awk '{print $1 " " $1}' > ASW.samples
plink3 --bfile g1000_afr --chr 6 --from-mb 25 --to-mb 35 --make-just-bim --out mhc_afr --threads 1
cat mhc_afr.bim | awk '{print $2}' > mhc_afr.justrs
plink --bfile g1000_afr --keep ASW.samples --exclude mhc_afr.justrs --maf 0.01 --make-bed --out g1000_asw_noMHC_maf0p01  # 61 individual

# EUR population
plink2 --bfile g1000_eur --chr 6 --from-mb 25 --to-mb 35 --make-just-bim --out mhc_eur --threads 1
cat mhc_eur.bim | awk '{print $2}' > mhc_eur.justrs
plink --bfile g1000_eur  --exclude mhc_eur.justrs --maf 0.01 --make-bed --out g1000_eur_noMHC_maf0p01  # 503 individual
```

Once this is ready, once need to compute LD scores like this:
```
export POPCORN="singularity exec --home $PWD:/home popcorn/containers/popcorn.sif popcorn"
$POPCORN compute --SNPs_to_store 50000 --bfile refs/g1000_eur_noMHC_maf0p01 refs/g1000_eur.cscore
$POPCORN compute --SNPs_to_store 50000 --bfile refs/g1000_asw_noMHC_maf0p01 refs/g1000_asw.cscore
$POPCORN compute --SNPs_to_store 50000 --bfile1 refs/g1000_eur_noMHC_maf0p01 --bfile2 refs/g1000_asw_noMHC_maf0p01 refs/g1000_eur_asw.cscore
```

We assume you already have GWAS summary statistics, formatted according to POPCORN, i.e. with columns ``rsid    a1      a2      Z       N``. Column names are case-sensitive, i.e. lowercase ``rsid``, ``a1``, ``a2``, and capital case ``Z`` and ``N``. The ``ACTG`` allele codes in ``a1`` and ``a2`` columns should be capital-case. 

Finally, perform the analysis as follows:
```
# for the univariate analysis
$POPCORN fit --sfile data/TRAIT_EUR.sumstats  --cfile refs/g1000_eur.cscore results/TRAIT_EUR.out
$POPCORN fit --sfile data/TRAIT_AAM.sumstats  --cfile refs/g1000_asw.cscore results/TRAIT_AAM.out

# for the bivariate (cross-trait)
$POPCORN fit --sfile1 data/TRAIT_EUR.sumstats --sfile2 data/TRAIT_AAM.sumstats  --cfile refs/g1000_eur_asw.cscore results/TRAIT_EUR_AAM.out
```

The resulting file will contain ``pgi`` measure, showing genetic impact correlation. See original software pages for futher details.  


## Build status

[![License](http://img.shields.io/:license-GPLv3+-green.svg)](http://www.gnu.org/licenses/gpl-3.0.html)
[![Flake8 lint](https://github.com/comorment/popcorn/actions/workflows/python.yml/badge.svg)](https://github.com/comorment/popcorn/actions/workflows/python.yml)
[![Dockerfile lint](https://github.com/comorment/popcorn/actions/workflows/docker.yml/badge.svg)](https://github.com/comorment/popcorn/actions/workflows/docker.yml)

## Description of available containers

* ``popcorn`` - Software for estimating correlation of trait effect sizes across populations

## Software versions

Below is the list of tools included in the different Dockerfile(s) and installer bash scripts for each container.
Please keep up to date (and update the main `<popcorn>/README.md` when pushing new container builds):
  
  | container               | OS/tool             | version
  | ----------------------- | ------------------- | ----------------------------------------
  | popcorn.sif  | ubuntu              | 20.04
  | popcorn.sif  | python3             | python 3.10.6
  | popcorn.sif  | popcorn             | https://github.com/ofrei/Popcorn @ fa1326c
  |              |                     | (minor fix on top of the original https://github.com/brielin/Popcorn @ ef4455a)

## Building/rebuilding containers

For instructions on how to build or rebuild containers using [Docker](https://www.docker.com) and [Singularity](https://docs.sylabs.io) refer to [`<popcorn>/src/README.md`](https://github.com/comorment/popcorn/blob/main/src/README.md).

## Feedback

If you face any issues, or if you need additional software, please let us know by creating a new [issue](https://github.com/comorment/popcorn/issues/new).
