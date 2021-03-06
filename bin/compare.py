#!/usr/bin/env python3

import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'lib'))

from workload import Workload
import constant
import matplotlib.pyplot as pp
import numpy as np

def main(names, component_id=1):
    count = len(names)
    pp.figure(figsize=(14, 2 * count), facecolor='w', edgecolor='k')
    for i in range(count):
        data = Workload.aggregate(Workload.locate(names[i]), 'dynamic_power')
        step_count = data.shape[1]
        time = constant.TIME_STEP * np.arange(step_count)
        pp.subplot(count, 1, i + 1)
        pp.plot(time, data[component_id, :])
        pp.xlim([time[0], time[-1]])
        pp.xlabel('Time (s)')
        pp.ylabel('Power (W)')
    pp.show()

main(sys.argv[1:])
