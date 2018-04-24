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
stats_omf=np.zeros([5,11,3])
stats_oma=np.zeros([5,11,3])
stats2_omf=np.zeros([5,1,3])
stats2_oma=np.zeros([5,1,3])

if(var == 'RMS'):   experiments=['c008', '019']
if(var == 'BIAS'):  experiments=['c008', '019', '021', '022', '023']
if(var == 'COUNT'): experiments=['c008', '019', '021', '022', '023']
if(var == 'RMS'):   experiments=['c008', '019', '021', '022', '023']

levels    =['1200.0','1000.0','900.0', '800.0', '600.0', '400.0', '300.0', '250.0', '200.0', '150.0', '100.0']
levels2   =['2000.0']
levels_int=np.arange(0,11,1)
levels2_int=np.arange(0,1,1)

common_dir='/gpfs/gd3/emc/meso/noscrub/Donald.E.Lippi/com/namrr/'

for expi in range(len(experiments)):
    exp=experiments[expi]
    print exp
    omf_it=1
    oma_it=3
    iti=0
    #filename=common_dir+'rw_'+exp+'/'+pdy+'/namrr.t'+cyc+'z.fits_conusnest.tm'+tmxx
    filename=common_dir+'rw_'+exp+'/namrr.'+pdy+'/namrr.t'+cyc+'z.fits_conusnest.tm'+tmxx
    
# GET STATS FROM FILE
    with open(filename,'r') as searchfile:
         skiprows=1
         for line in searchfile:
             skiprows=skiprows+1
             if "current vfit of radar wind data" in line:
                 iti=iti+1
                 if(omf_it==iti):
                    skiprows_omf=skiprows
                 if(oma_it==iti):
                    skiprows_oma=skiprows
                    break
    df_omf=pd.read_csv(filename,skiprows=skiprows_omf,delimiter=r"\s+",nrows=4)
    df_oma=pd.read_csv(filename,skiprows=skiprows_oma,delimiter=r"\s+",nrows=4)



    for levi in range(len(levels)):
        level=levels[levi] # string name for df[level]
        print(level)
        for stati in range(3):
            stats_omf[expi,levi,stati]=float(df_omf[level][stati+1])
            stats_oma[expi,levi,stati]=float(df_oma[level][stati+1])

    for levi2 in range(len(levels2)):
        level2=levels2[levi2] # string name for df[level]
        print(level2)
        for stati2 in range(3):
            stats2_omf[expi,levi2,stati2]=float(df_omf[level2][stati2+1])
            stats2_oma[expi,levi2,stati2]=float(df_oma[level2][stati2+1])



###########################
plt.figure(figsize=(10,6))#
fig_title_fontsize=18     #
xy_label_fontsize=14      #
tick_label_fontsize=12    #
legend_fontsize=8.8       #<=9
dot_size=40
l_dot_size=5
linewidth=2
###########################




#Plot 2
if(var=='COUNT'): vari=0
if(var=='BIAS'): vari=1
if(var=='RMS'): vari=2

plot_all_exps=True

ax2=plt.subplot(1,1,1)
ylow=0; yhigh=12; ax2.set_ylim(ylow,yhigh)

if(var=='COUNT'):
   xlow=0; xhigh=350000; ax2.set_xlim(xlow,xhigh)
   plt.xlabel(var,fontsize=xy_label_fontsize)

if(var == 'BIAS'):
   xlow=-1.0; xhigh=1.; ax2.set_xlim(xlow,xhigh)
   plt.xlabel(var+' (m/s)',fontsize=xy_label_fontsize)

if(var=='RMS'):
   xlow=0; xhigh=3; ax2.set_xlim(xlow,xhigh)
   plt.xlabel(var+' (m/s)',fontsize=xy_label_fontsize)

if(True):
   # XP
   #omf
   ax2.plot(stats_omf[0,:,vari],levels_int,color='#000000',marker='o',markersize=l_dot_size,label='control omf',    linewidth=linewidth,linestyle='-')
   ax2.plot(stats_omf[1,:,vari],levels_int,color='#ff0044',marker='o',markersize=l_dot_size,label='w_only omf',     linewidth=linewidth,linestyle='-')
   ax2.plot(stats_omf[2,:,vari],levels_int,color='#55ff00',marker='o',markersize=l_dot_size,label='w_so_elev5 omf', linewidth=linewidth,linestyle='-')
   ax2.plot(stats_omf[3,:,vari],levels_int,color='#00aaff',marker='o',markersize=l_dot_size,label='w_so_elev10 omf',linewidth=linewidth,linestyle='-')
   ax2.plot(stats_omf[4,:,vari],levels_int,color='#8800ff',marker='o',markersize=l_dot_size,label='so_elev10 omf',  linewidth=linewidth,linestyle='-')
   #oma
   ax2.plot(stats_oma[0,:,vari],levels_int,color='#000000',marker='^',markersize=l_dot_size,label='control oma',    linewidth=linewidth,linestyle='--')
   ax2.plot(stats_oma[1,:,vari],levels_int,color='#ff0044',marker='^',markersize=l_dot_size,label='w_only oma',     linewidth=linewidth,linestyle='--')
   ax2.plot(stats_oma[2,:,vari],levels_int,color='#55ff00',marker='^',markersize=l_dot_size,label='w_so_elev5 oma', linewidth=linewidth,linestyle='--')
   ax2.plot(stats_oma[3,:,vari],levels_int,color='#00aaff',marker='^',markersize=l_dot_size,label='w_so_elev10 oma',linewidth=linewidth,linestyle='--')
   ax2.plot(stats_oma[4,:,vari],levels_int,color='#8800ff',marker='^',markersize=l_dot_size,label='so_elev10 oma',  linewidth=linewidth,linestyle='--')

   #0-2000 hpa level
   y_of_dot_omf=stats2_omf[0,:,vari]*0+0.5
   y_of_dot_oma=stats2_omf[0,:,vari]*0+0.25

   #omf
   ax2.scatter(stats2_omf[0,:,vari],y_of_dot_omf, marker='o',s=dot_size,color="#000000",label='control omf (t. atm.)')
   ax2.scatter(stats2_omf[1,:,vari],y_of_dot_omf, marker='o',s=dot_size,color="#ff0044",label='w_only omf (t. atm.)')
   ax2.scatter(stats2_omf[2,:,vari],y_of_dot_omf, marker='o',s=dot_size,color="#55ff00",label='w_so_elev5 omf (t. atm.)')
   ax2.scatter(stats2_omf[3,:,vari],y_of_dot_omf, marker='o',s=dot_size,color="#00aaff",label='w_so_elev10 omf (t. atm.)')
   ax2.scatter(stats2_omf[4,:,vari],y_of_dot_omf, marker='o',s=dot_size,color="#8800ff",label='so_elev10 omf (t. atm.)')
   #oma
   ax2.scatter(stats2_oma[0,:,vari],y_of_dot_oma, marker='^',s=dot_size,color="#000000",label='control oma (t. atm.)')
   ax2.scatter(stats2_oma[1,:,vari],y_of_dot_oma, marker='^',s=dot_size,color="#ff0044",label='w_only oma (t. atm.)')
   ax2.scatter(stats2_oma[2,:,vari],y_of_dot_oma, marker='^',s=dot_size,color="#55ff00",label='w_so_elev5 oma (t. atm.)')
   ax2.scatter(stats2_oma[3,:,vari],y_of_dot_oma, marker='^',s=dot_size,color="#00aaff",label='w_so_elev10 oma (t. atm.)')
   ax2.scatter(stats2_oma[4,:,vari],y_of_dot_oma, marker='^',s=dot_size,color="#8800ff",label='so_elev10 oma (t. atm.)')


ax2.set_yticks(levels_int)
ax2.set_yticklabels(levels)
ax2.axvline(x=0,color='lightgray')
plt.ylabel('vertical layer (hPa)',fontsize=xy_label_fontsize)
plt.setp(ax2.get_xticklabels(),visible=True,fontsize=tick_label_fontsize)
plt.setp(ax2.get_yticklabels(),visible=True,fontsize=tick_label_fontsize)
#leg=ax2.legend(fontsize=legend_fontsize,ncol=4,scatterpoints=1,loc='upper center',bbox_to_anchor=(0.,-0.2,1.,.102))
leg=ax2.legend(fontsize=legend_fontsize,ncol=4,scatterpoints=1,loc='upper center')
leg.get_frame().set_alpha(0.9)


title=plt.suptitle('CONUS Radar winds OmF OmA statistics: %s \n %s t%sz tm%s' % (var,pdy,cyc,tmxx),fontsize=fig_title_fontsize,x=0.5,y=1.00)
plt.savefig('./'+var+'_'+pdy+'.namrr.t'+cyc+'z.fits_conusnest.tm'+tmxx+'.png',bbox_extra_artists=(leg,title,),bbox_inches='tight')


