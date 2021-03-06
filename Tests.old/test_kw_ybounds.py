# Adapted for numpy/ma/cdms2 by convertcdms.py
import vcs
import cdms2 as cdms
import MV2
import support
import os
bg = support.bg
f = cdms.open(os.path.join(vcs.sample_data, 'clt.nc'))
s = f('clt', slice(0, 5), latitude=(0., 0., 'cob'), squeeze=1)

nt = s.shape[0]

ax = MV2.arange(nt, typecode='d')
bounds = MV2.zeros((nt, 2), typecode='d')

for i in range(nt):
    bounds[i, 0] = ax[i]
    bounds[i, 1] = ax[i] + 1.
ax = cdms.createAxis(ax)
s.setAxis(0, ax)
x = vcs.init()
x.plot(s, bg=bg)
support.check_plot(x)
y = vcs.init()
# instead of being halfway, bounds are from node to node
y.plot(s, ybounds=bounds, bg=bg)
support.check_plot(y)
