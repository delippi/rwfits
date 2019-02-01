#!/bin/ksh
#PBS -N namrr_2015103000
#PBS -l walltime=01:00:00
#PBS -l procs=1
#PBS -q service
#PBS -A fv3-cpu
#PBS -o ./logs/namrr_2015103000 
#PBS -j oe

export ndate=/nwprod/util/exec/ndate
cd /scratch4/NCEPDEV/fv3-cam/noscrub/Donald.E.Lippi/com/namrr


start=2015103000

typeset -Z2 hr
typeset -Z2 tmxx

valtime=2015103006
valpdy=20151030
valcyc=00
valyrmon=201510
valyr=2015
valmon=10
hh=00

mkdir -p ./rw_021/20151030
cd rw_021/20151030

htar -xvf /NCEPDEV/emc-meso/5year/Donald.E.Lippi/rw_NAMv4/nwrw_021/rh2015/201510/20151030/meso2_noscrub_Donald.E.Lippi_com_namrr_rw_021_namrr.2015103000.bufr.tar ./namrr.t00z.fits_conusnest.tm06 
htar -xvf /NCEPDEV/emc-meso/5year/Donald.E.Lippi/rw_NAMv4/nwrw_021/rh2015/201510/20151030/meso2_noscrub_Donald.E.Lippi_com_namrr_rw_021_namrr.2015103000.bufr.tar ./namrr.t00z.fits_conusnest.tm05 
htar -xvf /NCEPDEV/emc-meso/5year/Donald.E.Lippi/rw_NAMv4/nwrw_021/rh2015/201510/20151030/meso2_noscrub_Donald.E.Lippi_com_namrr_rw_021_namrr.2015103000.bufr.tar ./namrr.t00z.fits_conusnest.tm04 
htar -xvf /NCEPDEV/emc-meso/5year/Donald.E.Lippi/rw_NAMv4/nwrw_021/rh2015/201510/20151030/meso2_noscrub_Donald.E.Lippi_com_namrr_rw_021_namrr.2015103000.bufr.tar ./namrr.t00z.fits_conusnest.tm03 
htar -xvf /NCEPDEV/emc-meso/5year/Donald.E.Lippi/rw_NAMv4/nwrw_021/rh2015/201510/20151030/meso2_noscrub_Donald.E.Lippi_com_namrr_rw_021_namrr.2015103000.bufr.tar ./namrr.t00z.fits_conusnest.tm02 
htar -xvf /NCEPDEV/emc-meso/5year/Donald.E.Lippi/rw_NAMv4/nwrw_021/rh2015/201510/20151030/meso2_noscrub_Donald.E.Lippi_com_namrr_rw_021_namrr.2015103000.bufr.tar ./namrr.t00z.fits_conusnest.tm01 
htar -xvf /NCEPDEV/emc-meso/5year/Donald.E.Lippi/rw_NAMv4/nwrw_021/rh2015/201510/20151030/meso2_noscrub_Donald.E.Lippi_com_namrr_rw_021_namrr.2015103000.bufr.tar ./namrr.t00z.fits_conusnest.tm00 

htar -xvf /NCEPDEV/emc-meso/5year/Donald.E.Lippi/rw_NAMv4/nwrw_021/rh2015/201510/20151030/meso2_noscrub_Donald.E.Lippi_com_namrr_rw_021_namrr.2015103000.bufr.tar ./namrr.t00z.fits2_conusnest.tm06 
htar -xvf /NCEPDEV/emc-meso/5year/Donald.E.Lippi/rw_NAMv4/nwrw_021/rh2015/201510/20151030/meso2_noscrub_Donald.E.Lippi_com_namrr_rw_021_namrr.2015103000.bufr.tar ./namrr.t00z.fits2_conusnest.tm05 
htar -xvf /NCEPDEV/emc-meso/5year/Donald.E.Lippi/rw_NAMv4/nwrw_021/rh2015/201510/20151030/meso2_noscrub_Donald.E.Lippi_com_namrr_rw_021_namrr.2015103000.bufr.tar ./namrr.t00z.fits2_conusnest.tm04 
htar -xvf /NCEPDEV/emc-meso/5year/Donald.E.Lippi/rw_NAMv4/nwrw_021/rh2015/201510/20151030/meso2_noscrub_Donald.E.Lippi_com_namrr_rw_021_namrr.2015103000.bufr.tar ./namrr.t00z.fits2_conusnest.tm03 
htar -xvf /NCEPDEV/emc-meso/5year/Donald.E.Lippi/rw_NAMv4/nwrw_021/rh2015/201510/20151030/meso2_noscrub_Donald.E.Lippi_com_namrr_rw_021_namrr.2015103000.bufr.tar ./namrr.t00z.fits2_conusnest.tm02 
htar -xvf /NCEPDEV/emc-meso/5year/Donald.E.Lippi/rw_NAMv4/nwrw_021/rh2015/201510/20151030/meso2_noscrub_Donald.E.Lippi_com_namrr_rw_021_namrr.2015103000.bufr.tar ./namrr.t00z.fits2_conusnest.tm01 
htar -xvf /NCEPDEV/emc-meso/5year/Donald.E.Lippi/rw_NAMv4/nwrw_021/rh2015/201510/20151030/meso2_noscrub_Donald.E.Lippi_com_namrr_rw_021_namrr.2015103000.bufr.tar ./namrr.t00z.fits2_conusnest.tm00 


