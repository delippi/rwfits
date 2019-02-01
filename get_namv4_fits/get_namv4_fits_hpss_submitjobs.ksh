start=2015103000
end=2015103000
#end=2015103100
hr=01
envir="rw_022"

./get_namv4_fits_hpss.ksh $start $end $envir

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
    $submit archive_namrr_input_${valtime}.ksh
done


