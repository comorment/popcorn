# Source files

## Singularity containers

This repository is used to develop and document [Docker](https://www.docker.com) and [Singularity](https://docs.sylabs.io) containers with various software and analytical tools.

## Software versions

  Below is the list of tools included in the different Dockerfiles and installer bash scripts for each container.
  Please keep up to date (and update the main `<popcorn>/README.md` when pushing new container builds):
  
  | container               | OS/tool             | version
  | ------------------------| ------------------- | ----------------------------------------
  | popcorn.sif  | ubuntu              | 20.04
  | popcorn.sif  | python              | 3.8.10

## Feedback

If you face any issues, or if you need additional software, please let us know by creating an [issue](https://github.com/espenhgn/popcorn/issues/new).

## Build instructions

### The easy(er) way

For convenience, a `Makefile` is provided in this directory in order to build [Singularity](https://docs.sylabs.io) containers from Dockerfiles (as `<popcorn/src/dockerfiles/popcorn/Dockerfile>`).
Using this files assumes that a working [Docker](https://www.docker.com) and [Singularity](https://docs.sylabs.io) installation, as well as the [`GNU make`](https://www.gnu.org/software/make/) utility is available on the host computer/build system.
On Debian-based Linux OS, this utility can usually be installed by issuing`apt-get install -y make`; on MacOS with [Homebrew](https://brew.sh) as`brew install make`. Prefix`sudo` if necessary.

Then, the container can be built by issuing:

```
make popcorn.sif
```

If all went well, the built file should be located as `<popcorn/containers/popcorn.sif>`.
In case super-user (`sudo`) privileges are required, issue:

```
sudo make popcorn.sif
```

### Manual builds

In order to build the container manually, this is possible via the following steps

```
docker build -t popcorn -f dockerfiles/popcorn/Dockerfile .  # build docker container
```

In case you do not want to use Singularity (e.g., for testing locally), the build can be used e.g., by issuing

```
docker run -it -p 5001:5001 popcorn python --version
```

which should return the currently installed Python version incorporated into the container. 
You may replace the port numbers (``5001``) by another (e.g., ``5000``).

To convert, and relocate the Singularity container file generated from the Docker image, issue
```
bash scripts/convert_docker_image_to_singularity.sh popcorn  # produces popcorn.sif
bash scripts/scripts/move_singularity_file.sh.sh popcorn  # put popcorn.sif file to <popcorn>/containers/ directory
```

Again, super-user (`sudo`) privileges may be required on the host computer. In that case, prefix `sudo` on the line(s) that fail. 
For further details on the commands within each bash file, open the ``.sh`` files in a code editor.

### Clean up

The above steps may leave a collection of images in the Docker registry, wasting drive space.
To list them, issue

```
docker images -a
```

Chosen images can be removed by issuing:

```
docker rmi <image-id-1> <image-id-2> ... 
```

For more info, see [`docker rm`](https://docs.docker.com/engine/reference/commandline/rm/)

## Testing container builds

Some basic checks for the functionality of the different container builds are provided in `<popcorn>/tests/`, implemented in Python.
The tests can be executed using the [Pytest](https://docs.pytest.org) testing framework.

In case `singularity` is not found in `PATH`, tests will fall back to `docker`.
In case `docker` is not found, no tests will run.

To install Pytest in the current Python environment, issue:

```
pip install pytest  # --user optional
```

New virtual environment using [conda](https://docs.conda.io/en/latest/index.html):

```
conda create -n pytest python=3 pytest -y  # creates env "pytest"
conda activate pytest  # activates env "pytest"
```

Then, all checks can be executed by issuing:

```
cd <popcorn>
py.test -v tests  # with verbose output
```

Checks for individual containers (e.g., `popcorn.sif`) can be executed by issuing:

```
py.test -v tests/test_popcorn.py
```

Note that the proper container files (*.sif files) corresponding to the different test scripts must exist in `<popcorn>/containers/`,
not only git LFS pointer files.
