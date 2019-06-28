#This script is used to pull namv4 radial wind experiments from tape.


start=2015103000
end=2015103100
hr=03
envirs="rw_c008 rw_019 rw_021 rw_022 rw_023"
envirs="rw_030 rw_031 rw_032"

mkdir -p ./logs
mkdir -p ./jobs

for envir in $envirs; do
   ./get_namv4_fits_hpss.ksh $start $end $hr $envir

   machine="THEIA"
   if [[ $machine == "THEIA" ]]; then
      export ndate=/home/Donald.E.Lippi/bin/ndate
      submit="sbatch"
   else
      export ndate=/nwprod/util/exec/ndate
      submit="bsub <"
   fi


   valtime=`${ndate} -${hr} $start`

   while [ $valtime -lt $end ]; do
       valtime=`${ndate} +${hr} $valtime`
       echo $valtime
       $submit ./jobs/archive_namrr_${envir}_${valtime}.ksh
   done
done

