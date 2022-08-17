#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 12:28:05 2022

@author: jholt
"""
import socket
isliv = 'livljobs' in socket.gethostname()
if isliv:
    coast_dir='/login/jholt/work/Git/COAsT/'
else:
    coast_dir='/home/users/jholt/work/Git/COAsT/'
import sys
sys.path.insert(0,coast_dir)
import coast
import numpy as np
from getpass import getpass
import circulation
import scipy.io
USERNAME='jholt'
PASSWORD=getpass( 'Password: ' )

database = coast.Copernicus(USERNAME, PASSWORD, "my")
globcurrent=database.get_product("dataset-uv-rep-monthly")

nemo_t = coast.Gridded(fn_data=globcurrent, config="/home/users/jholt/work/Git/COAsT/config/example_cmems_grid_uv.json")
nt=nemo_t.dataset.t_dim.size
T=np.array([])
#%%
#select months
for im in [8,9,10]:
    T=np.append(T,np.arange(im,nt,12))
T=np.sort(T).astype(int)    
#%%
A=np.load('../Data/LME_gridinfo_equ025.npz')
a=scipy.io.loadmat('../Data/equalgrid_025_LMEmask.mat')
nlme=66
J_offset=186 #account for extra rows in eORCA if data is made for normal ORCA
LME_mask=a['LME_mask'][:,:].T
lmelist=np.array([29])-1
for ilme in lmelist:    

        LMENAM=A['DOMNAM'][ilme]
        imin=(A['i_min'][ilme]+360*4)%1440
        imax=(A['i_max'][ilme]+360*4)%1440
        jmin=A['j_min'][ilme]+39
        jmax=A['j_max'][ilme]+39
        jmin0=A['j_min'][ilme]
        jmax0=A['j_max'][ilme]
#        jmin=375
#        jmax=455
#        imin=1030
#        imax=1130
        print(LMENAM)
        nemo_t1=nemo_t.subset_as_copy(x_dim=range(imin,imax),y_dim=range(jmin,jmax),z_dim=0,t_dim=T)
        mask=nemo_t1.dataset.u_velocity[0,:,:].values != np.nan
        circulation.plot_surface_circulation(nemo_t1, nemo_t1,nemo_t1, mask,'CMEMS '+LMENAM, co_located=True,Vmax=.32)