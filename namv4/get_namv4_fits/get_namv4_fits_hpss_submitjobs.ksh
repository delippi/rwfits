start=2015103000
#end=2015103000
end=2015103100
hr=06
envirs="rw_c008 rw_019 rw_020 rw_021 rw_022"

mkdir -p ./logs
mkdir -p ./jobs

for envir in $envirs; do
   ./get_namv4_fits_hpss.ksh $start $end $hr $envir

   machine="THEIA"
   if [[ $machine == "THEIA" ]]; then
      export ndate=/home/Donald.E.Lippi/bin/ndate
      submit="qsub"
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

