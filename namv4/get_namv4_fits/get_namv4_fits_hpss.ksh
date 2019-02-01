#!/bin/ksh

machine="THEIA"
if [[ $machine == "THEIA" ]]; then
   export ndate=/home/Donald.E.Lippi/bin/ndate
else
   export ndate=/nwprod/util/exec/ndate
fi


start=$1
end=$2
hr=$3
envir=$4

if [[ $start == "" ]];then; start=2015103000; fi
if [[ $end   == "" ]];then;   end=2015103000; fi
if [[ $hr    == "" ]];then;    hr=06;         fi
if [[ $envir == "" ]];then; envir="rw_022";   fi


HPSS_RETENTION_PERIOD='5year'
HPSS_GROUP='emc-meso'
HPSS_USER='Donald.E.Lippi'

typeset -Z2 hr

valtime=`${ndate} -${hr} $start`

while [ $valtime -lt $end ]; do
   valtime=`${ndate} +${hr} $valtime`
   valpdy=`echo ${valtime} | cut -c 1-8`
   valcyc=`echo ${valtime} | cut -c 9-10`
   valyrmon=`echo $valtime | cut -c 1-6`
   valyr=`echo ${valtime} | cut -c 1-4`
   valmon=`echo ${valtime} | cut -c 5-6`
   hh=`echo $valtime | cut -c9-10`
   HPSSOUT="/NCEPDEV/$HPSS_GROUP/$HPSS_RETENTION_PERIOD/$HPSS_USER/rw_NAMv4/nw$envir/rh$valyr/$valyrmon/$valpdy/meso2_noscrub_Donald.E.Lippi_com_namrr_${envir}_namrr.${valtime}.bufr.tar"
   #LocalOUT="/gpfs/td3/emc/meso/noscrub/Donald.E.Lippi/com/namrr/$envir"


if [[ $machine == "THEIA" ]]; then
cat << EOF > ./jobs/archive_namrr_${envir}_${valtime}.ksh
#!/bin/ksh
#PBS -N namrr_${envir}_${valtime}
#PBS -l walltime=01:00:00
#PBS -l procs=1
#PBS -q service
#PBS -A fv3-cpu
#PBS -o ./logs/namrr_${envir}_${valtime} 
#PBS -j oe

export ndate=/nwprod/util/exec/ndate
cd /scratch4/NCEPDEV/fv3-cam/noscrub/Donald.E.Lippi/com/namrr

EOF

else
cat << EOF > ./jobs/archive_namrr_${envir}_${valtime}.ksh
#!/bin/ksh
#BSUB -P ibm                      # project code
#BSUB -J namrr_${envir}_${valtime}   # job name
#BSUB -W 03:00                    # wall-clock time (hrs:mins)
#BSUB -n 1                        # number of tasks in job
#BSUB -R "affinity[core]"         # number of cores
#BSUB -R "rusage[mem=8000]"       # number of cores
#BSUB -q transfer                 # queue
#BSUB -o ./logs/namrr_${envir}_${valtime}   # output file name in which %J is replaced by the job ID

export ndate=/nwprod/util/exec/ndate
#cd /gpfs/gd3/emc/meso/noscrub/Donald.E.Lippi/com/namrr
cd /gpfs/td3/emc/meso/noscrub/Donald.E.Lippi/com/namrr

EOF
fi

#append non machine specific part
cat << EOF >> ./jobs/archive_namrr_${envir}_${valtime}.ksh

start=${valtime}

typeset -Z2 hr
typeset -Z2 tmxx

valtime=`${ndate} +${hr} $valtime`
valpdy=`echo ${valtime} | cut -c 1-8`
valcyc=`echo ${valtime} | cut -c 9-10`
valyrmon=`echo $valtime | cut -c 1-6`
valyr=`echo ${valtime} | cut -c 1-4`
valmon=`echo ${valtime} | cut -c 5-6`
hh=`echo $valtime | cut -c9-10`

mkdir -p ./${envir}/${valpdy}
cd ${envir}/${valpdy}

htar -xvf ${HPSSOUT} ./namrr.t${valcyc}z.fits_conusnest.tm06 
htar -xvf ${HPSSOUT} ./namrr.t${valcyc}z.fits_conusnest.tm05 
htar -xvf ${HPSSOUT} ./namrr.t${valcyc}z.fits_conusnest.tm04 
htar -xvf ${HPSSOUT} ./namrr.t${valcyc}z.fits_conusnest.tm03 
htar -xvf ${HPSSOUT} ./namrr.t${valcyc}z.fits_conusnest.tm02 
htar -xvf ${HPSSOUT} ./namrr.t${valcyc}z.fits_conusnest.tm01 
htar -xvf ${HPSSOUT} ./namrr.t${valcyc}z.fits_conusnest.tm00 

htar -xvf ${HPSSOUT} ./namrr.t${valcyc}z.fits2_conusnest.tm06 
htar -xvf ${HPSSOUT} ./namrr.t${valcyc}z.fits2_conusnest.tm05 
htar -xvf ${HPSSOUT} ./namrr.t${valcyc}z.fits2_conusnest.tm04 
htar -xvf ${HPSSOUT} ./namrr.t${valcyc}z.fits2_conusnest.tm03 
htar -xvf ${HPSSOUT} ./namrr.t${valcyc}z.fits2_conusnest.tm02 
htar -xvf ${HPSSOUT} ./namrr.t${valcyc}z.fits2_conusnest.tm01 
htar -xvf ${HPSSOUT} ./namrr.t${valcyc}z.fits2_conusnest.tm00 


EOF
done

