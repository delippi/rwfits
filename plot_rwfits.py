import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys
try:
   pdy=str(sys.argv[1])
   cyc=str(sys.argv[2])
   tmxx=str(sys.argv[3])
   var=str(sys.argv[4])
except:
   pdy='20151030'
   cyc='12'
   tmxx='00'
   var='BIAS'
   var='RMS'
   var='COUNT'
# KEY:
# ptop 1000  900 800 600 400 300 250 200 150 100  50    0
# pbot 1200 1000 900 800 600 400 300 250 200 150 100 2000    <-----    use this line for df['1200.0'], for example
# count line 1
# bias  line 2
# rms   line 3

# stats is defined as stats( exp, lev, stat ), where stat(count, rms, bias)
stats=np.zeros([5,11,3])
stats2=np.zeros([5,1,3])

if(var == 'RMS'):   experiments=['c008', '019']
if(var == 'BIAS'):  experiments=['c008', '019', '021', '022', '023']
if(var == 'COUNT'): experiments=['c008', '019', '021', '022', '023']
if(var == 'RMS'):   experiments=['c008', '019', '021', '022', '023']

levels    =['1200.0','1000.0','900.0', '800.0', '600.0', '400.0', '300.0', '250.0', '200.0', '150.0', '100.0']
levels2   =['2000.0']
levels_int=np.arange(0,11,1)
levels2_int=np.arange(0,1,1)



for expi in range(len(experiments)):
    exp=experiments[expi]
    print exp
    it=3
    iti=0
    try:
        filename='/gpfs/gd3/emc/meso/noscrub/Donald.E.Lippi/com/namrr/rw_'+exp+'/'+pdy+'/namrr.t'+cyc+'z.fits_conusnest.tm'+tmxx
        with open(filename,'r') as searchfile:
             skiprows=1
             for line in searchfile:
                 skiprows=skiprows+1
                 if "current vfit of radar wind data" in line:
                     iti=iti+1
                     if(it==iti):
                        break
        df=pd.read_csv(filename,skiprows=skiprows,delimiter=r"\s+",nrows=4)
    except:
        filename='/gpfs/gd3/emc/meso/noscrub/Donald.E.Lippi/com/namrr/rw_'+exp+'/namrr.'+pdy+'/namrr.t'+cyc+'z.fits_conusnest.tm'+tmxx
        with open(filename,'r') as searchfile:
             skiprows=1
             for line in searchfile:
                 skiprows=skiprows+1
                 if "current vfit of radar wind data" in line:
                     iti=iti+1
                     if(it==iti):
                        break
        df=pd.read_csv(filename,skiprows=skiprows,delimiter=r"\s+",nrows=4)



    for levi in range(len(levels)):
        level=levels[levi] # string name for df[level]
        print(level)
        for stati in range(3):
            stats[expi,levi,stati]=float(df[level][stati+1])
    for levi2 in range(len(levels2)):
        level2=levels2[levi2] # string name for df[level]
        print(level2)
        for stati2 in range(3):
            stats2[expi,levi2,stati2]=float(df[level2][stati2+1])



###########################
plt.figure(figsize=(10,6))#
fig_title_fontsize=18     #
xy_label_fontsize=14      #
tick_label_fontsize=12    #
legend_fontsize=10        #
dot_size=15
linewidth=2
###########################



##Plot 1 - BIAS
#ax1=plt.subplot(1,2,1)
#ax1.plot(stats[1,:,1]-stats[0,:,1],levels_int,color='black',label='w_only - control: bias')
##ax1.plot(stats[1,:,1],levels_int,color='black',label='w_only: bias',linewidth=2)
##ax1.plot(stats[0,:,1],levels_int,color='#ff0044',label='control: bias',linewidth=2)
#ax1.axvline(x=0,color='lightgray')
#ax1.set_yticks(levels_int)
#ax1.set_yticklabels(levels)
#ax1.axvline(x=0)
#plt.xlabel('BIAS (m/s)',fontsize=xy_label_fontsize)
#plt.ylabel('vertical layer (hPa)',fontsize=xy_label_fontsize)
#plt.setp(ax1.get_xticklabels(),visible=True,fontsize=tick_label_fontsize)
#plt.setp(ax1.get_yticklabels(),visible=True,fontsize=tick_label_fontsize)
#ax1.legend(fontsize=legend_fontsize)

#Plot 2 - RMS
if(var=='COUNT'): vari=0
if(var=='BIAS'): vari=1
if(var=='RMS'): vari=2

plot_all_exps=True

ax2=plt.subplot(1,1,1)
ylow=0; yhigh=12; ax2.set_ylim(ylow,yhigh)

if(var=='COUNT'):
   xlow=0; xhigh=250000; ax2.set_xlim(xlow,xhigh)
   plt.xlabel(var,fontsize=xy_label_fontsize)

if(var == 'BIAS'):
   xlow=-1.0; xhigh=1.; ax2.set_xlim(xlow,xhigh)
   plt.xlabel(var+' (m/s)',fontsize=xy_label_fontsize)

if(var=='RMS'):
   xlow=-3; xhigh=3; ax2.set_xlim(xlow,xhigh)
   plt.xlabel(var+' (m/s)',fontsize=xy_label_fontsize)

if(True):
   # XP
   ax2.plot(stats[0,:,vari],levels_int,color='black',label='control',linewidth=linewidth)
   ax2.plot(stats[1,:,vari],levels_int,color='#ff0044',label='w_only',linewidth=linewidth)
   ax2.plot(stats[2,:,vari],levels_int,color='#55ff00',label='w_so_elev5',linewidth=linewidth)
   ax2.plot(stats[3,:,vari],levels_int,color='#00aaff',label='w_so_elev10',linewidth=linewidth)
   ax2.plot(stats[4,:,vari],levels_int,color='#8800ff',label='so_elev10',linewidth=linewidth)

   # control - XP
   ax2.plot(stats[1,:,vari]-stats[0,:,vari],levels_int,color='#ff0044',label='w_only - control',linestyle='--',linewidth=linewidth)
   ax2.plot(stats[2,:,vari]-stats[0,:,vari],levels_int,color='#55ff00',label='w_so_elev5 - control',linestyle='--',linewidth=linewidth)
   ax2.plot(stats[3,:,vari]-stats[0,:,vari],levels_int,color='#00aaff',label='w_so_elev10 - control',linestyle='--',linewidth=linewidth)
   ax2.plot(stats[4,:,vari]-stats[0,:,vari],levels_int,color='#8800ff',label='so_elev10 - control',linestyle='--',linewidth=linewidth)

   #0-2000 hpa level
   y_of_dot=stats2[0,:,vari]*0+0.125
   ax2.scatter(stats2[1,:,vari]-stats2[0,:,vari], y_of_dot , marker='o',s=dot_size,color="#ff0044",label='column aggregate (w_only-control)')
   ax2.scatter(stats2[2,:,vari]-stats2[0,:,vari], y_of_dot , marker='o',s=dot_size,color="#55ff00",label='column aggregate (w_so_elev5-control)')
   ax2.scatter(stats2[3,:,vari]-stats2[0,:,vari], y_of_dot , marker='o',s=dot_size,color="#00aaff",label='column aggregate (w_so_elev10-control)')
   ax2.scatter(stats2[4,:,vari]-stats2[0,:,vari], y_of_dot , marker='o',s=dot_size,color="#8800ff",label='column aggregate (so_elev10-control)')


#if(var=='COUNT'):
#   xlow=0; xhigh=350000; ax2.set_xlim(xlow,xhigh)
#   ax2.plot(stats[0,:,vari],levels_int,color='black',label='control')
#   ax2.plot(stats[1,:,vari],levels_int,color='#ff0044',label='w_only')
#   ax2.plot(stats[2,:,vari],levels_int,color='#55ff00',label='w_so_elev5')
#   ax2.plot(stats[3,:,vari],levels_int,color='#00aaff',label='w_so_elev10')
#   ax2.plot(stats[4,:,vari],levels_int,color='#8800ff',label='so_elev10')
#   plt.xlabel(var,fontsize=xy_label_fontsize)
#
#if(var == 'BIAS'):
#   xlow=-1.0; xhigh=1.; ax2.set_xlim(xlow,xhigh)
#   ax2.plot(stats[1,:,vari]-stats[0,:,vari],levels_int,color='#ff0044',label='w_only - control',linestyle='--')
#   ax2.plot(stats[0,:,vari],levels_int,color='black',label='control')
#   ax2.plot(stats[1,:,vari],levels_int,color='#ff0044',label='w_only')
#   #ax2.plot(stats[2,:,vari],levels_int,color='#55ff00',label='w_so_elev5')
#   #ax2.plot(stats[3,:,vari],levels_int,color='#00aaff',label='w_so_elev10')
#   #ax2.plot(stats[4,:,vari],levels_int,color='#8800ff',label='so_elev10')
#   plt.xlabel(var,fontsize=xy_label_fontsize)

ax2.set_yticks(levels_int)
ax2.set_yticklabels(levels)
ax2.axvline(x=0,color='lightgray')
plt.ylabel('vertical layer (hPa)',fontsize=xy_label_fontsize)
plt.setp(ax2.get_xticklabels(),visible=True,fontsize=tick_label_fontsize)
plt.setp(ax2.get_yticklabels(),visible=True,fontsize=tick_label_fontsize)
leg=ax2.legend(fontsize=legend_fontsize,ncol=3,scatterpoints =1)
leg.get_frame().set_alpha(0.9)


plt.suptitle('Radar winds O-F statistics: %s \n %s t%sz tm%s' % (var,pdy,cyc,tmxx),fontsize=fig_title_fontsize,x=0.5,y=1.00)
plt.savefig('./'+var+'_'+pdy+'.namrr.t'+cyc+'z.fits_conusnest.tm'+tmxx+'.png',bbox_inches='tight')


