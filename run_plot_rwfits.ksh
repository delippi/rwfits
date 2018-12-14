#!/bin/ksh
PDY='20180911'
CYC='06'
TMXX='00'
VAR='BIAS RMS COUNT'
#VAR='RMS COUNT'
#VAR='RMS'

montage='.false.'

#PDY='20151030'
#CYC='00'
#VAR='RMS'

set -x

for var in $VAR; do
    for pdy in $PDY; do
        for cyc in $CYC; do
            for tmxx in $TMXX; do
                echo $pdy $cyc $tmxx $var
                python plot_rwfits.py $pdy $cyc $tmxx $var
                if [[ $cyc == '06' && $montage == '.true.' ]]; then
                   fig1=${var}_${pdy}.fv3gfs.t${cyc}z.rwfits.tm${tmxx}.png
                   #fig1=${var}_20151030.namrr.t06z.fits_conusnest.tm00.png
                   #fig3=${var}_20151030.namrr.t12z.fits_conusnest.tm00.png
                   #fig4=${var}_20151030.namrr.t18z.fits_conusnest.tm00.png
                   legend=legend.png
                   #montage -tile 2x2 -geometry +4+4 $fig1 $fig2 $fig3 $fig4 ${var}_20151030.namrr.t00-18z.fits_conusnest.tm00.png
                   montage -tile 1x2 -geometry +4+4 $fig1 $legend ${var}_${pdy}.fv3gfs.t${cyc}z.rwfits.tm${tmxx}_leg.png
                   rm -f $fig1 
                fi
            done
        done
    done
done
set +x
#echo "tar this up on HPSS? (y/n)"
#read ans
#if [[ $ans == 'y' ]]; then 
#   cp *.png rwfits_figs/.
#   htar -cvf /NCEPDEV/emc-meso/5year/Donald.E.Lippi/rwfits_figs.tar ./rwfits_figs/
#fi
#echo "run the following on theia:"
#echo "cd ~"
#echo "htar -xvf /NCEPDEV/emc-meso/5year/Donald.E.Lippi/rwfits_figs.tar"

