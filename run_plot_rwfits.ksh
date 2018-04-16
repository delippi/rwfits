#!/bin/ksh

PDY='20151030 20151031'
CYC='00 06 12 18'
TMXX='00'
VAR='BIAS RMS COUNT'
#VAR='RMS'
#VAR='COUNT'

#PDY='20151030'
#CYC='00'
#VAR='BIAS'

for var in $VAR; do
    for pdy in $PDY; do
        for cyc in $CYC; do
            for tmxx in $TMXX; do
                echo $pdy $cyc $tmxx $var
                if [[ $pdy == '20151031' && $cyc != '00' ]]; then
                   exit
                else
                   python plot_rwfits.py $pdy $cyc $tmxx $var
                fi
            done
        done
    done
done
exit
