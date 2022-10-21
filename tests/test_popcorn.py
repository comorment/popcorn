# encoding: utf-8

"""
Test module for ``popcorn.sif`` build
"""

import os
import pytest
import subprocess
import tempfile


pth = os.path.join('containers', 'popcorn.sif')

def test_popcorn_compute():
    call = f'singularity run {pth} popcorn compute -h'
    out = subprocess.run(call.split(' '))
    assert out.returncode == 0

def test_popcorn_fit():
    call = f'singularity run {pth} popcorn fit -h'
    out = subprocess.run(call.split(' '))
    assert out.returncode == 0

               
