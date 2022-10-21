all: popcorn.sif  # additional .sif files may be listed here for corresponding dockerfiles

%.sif: dockerfiles/%/Dockerfile
	docker build -t $* -f dockerfiles/$*/Dockerfile . && \
	scripts/convert_docker_image_to_singularity.sh $* && \
	scripts/move_singularity_file.sh $*

# Example commands executed by this make file
# 
# Run "make popcorn.sif" will trigger this:
# docker build -t popcorn -f dockerfiles/popcorn/Dockerfile . && \  # build docker container
#     scripts/convert_docker_image_to_singularity.sh popcorn && \         # produces popcorn.sif
#     scripts/scripts/move_singularity_file.sh.sh popcorn        # moves popcorn.sif to ../singularity/.
#  
# Run "make all" will build all singularity containers in this project
