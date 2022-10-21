# popcorn project

Singularity wrapper for https://github.com/brielin/Popcorn (the version updated May 2022 based on Python3).

Brief getting started instructions, which should execute built-in example provided together with popcorn software:

```
singularity shell --home $PWD:/home containers/popcorn.sif
cp /tools/popcorn/test/* .
./test.bash
```

# Important! - Set up Git LFS before cloning this repository

Have a look [here](https://github.com/comorment/containers/blob/main/README.md#getting-started) if you're new to git or Git LFS.

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
  | popcorn.sif  | popcorn             | https://github.com/brielin/Popcorn ef4455a

## Building/rebuilding containers

For instructions on how to build or rebuild containers using [Docker](https://www.docker.com) and [Singularity](https://docs.sylabs.io) refer to [`<popcorn>/src/README.md`](https://github.com/comorment/popcorn/blob/main/src/README.md).

## Feedback

If you face any issues, or if you need additional software, please let us know by creating a new [issue](https://github.com/comorment/popcorn/issues/new).
