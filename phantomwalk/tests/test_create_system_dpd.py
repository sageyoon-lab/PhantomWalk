import pytest
import datetime
import os

import sys
import os
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir, 'src')))
import create_system_dpd as dpd

def test_creation():
    s = dpd.create_polymer_system_dpd(num_pol=5, num_mon=10, density=0.5)
    assert s > 0

def test_custom_log_files():
    time_string = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    gsd_file_name = f"{time_string}.gsd"
    log_file_name = f"{time_string}.txt"
    s = dpd.create_polymer_system_dpd(
        num_pol=5,
        num_mon=10,
        density=0.5,
        gsd_file_name=gsd_file_name,
        log_file_name=log_file_name
    )
    assert os.path.isfile(gsd_file_name) and os.path.isfile(log_file_name)
