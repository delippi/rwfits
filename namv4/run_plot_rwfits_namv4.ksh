#!/bin/ksh
PDY='20151030'
CYC='09 12 15 18'
TMXX='00'
VAR='BIAS RMS COUNT'
#VAR='RMS COUNT'
#VAR='RMS'

montage='.true.'

#PDY='20151030'
#CYC='09'
#VAR='COUNT'

set -x

for var in $VAR; do
    for pdy in $PDY; do
        for cyc in $CYC; do
            for tmxx in $TMXX; do
                echo $pdy $cyc $tmxx $var
                python plot_rwfits.py $pdy $cyc $tmxx $var
                if [[ $cyc == '18' && $montage == '.true.' ]]; then
                   fig1=${var}_20151030.namrr.t09z.fits_conusnest.tm00.png
                   fig2=${var}_20151030.namrr.t12z.fits_conusnest.tm00.png
                   fig3=${var}_20151030.namrr.t15z.fits_conusnest.tm00.png
                   fig4=${var}_20151030.namrr.t18z.fits_conusnest.tm00.png
                   legend=legend.png
                   newfig1=${var}_20151030.namrr.t00-18z.fits_conusnest.tm00.png
                   newfig2=${var}_20151030.namrr.t00-18z.fits_conusnest_legend.tm00.png
                   montage -tile 2x2 -geometry +4+4 $fig1 $fig2 $fig3 $fig4 $newfig1
                   #identify $newfig1
                   montage -tile 1x2 -geometry +4+4 $newfig1 $legend $newfig2
                   rm -f $fig1 $fig2 $fig3 $fig4 $newfig1
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

