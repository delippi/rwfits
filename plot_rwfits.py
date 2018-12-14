import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys

# This program is run by ./run_plot_rwfits.ksh. It passes pdy, cyc, tmxx, and var and then
# creates figures from radial wind fit files.


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

levs=7
# stats is defined as stats( exp, lev, stat ), where stat(count, rms, bias)
stats_omb=np.zeros([5,levs,3])
stats_oma=np.zeros([5,levs,3])
stats2_omb=np.zeros([5,1,3])
stats2_oma=np.zeros([5,1,3])

experiments=['test']

levels    =['1200.0','1000.0','900.0', '800.0', '600.0', '400.0', '300.0'] #, '250.0', '200.0', '150.0', '100.0']
levels2   =['2000.0']
levels_int=np.arange(0,levs,1)
levels2_int=np.arange(0,1,1)

common_dir='/gpfs/td3/emc/meso/noscrub/Donald.E.Lippi/com/namrr/'
common_dir='/scratch4/NCEPDEV/stmp3/Donald.E.Lippi/RUNDIRS/rw_001/2018050306/gdas/anal/'
common_dir='/scratch4/NCEPDEV/stmp3/Donald.E.Lippi/fv3gfs_dl2rw/anl/rh2018/201809/'+pdy+'/'+cyc

for expi in range(len(experiments)):
    exp=experiments[expi]
    print exp
    omb_it=1
    oma_it=2
    iti=0
    #filename=common_dir+'rw_'+exp+'/'+pdy+'/namrr.t'+cyc+'z.fits_conusnest.tm'+tmxx
    #filename=common_dir+'rw_'+exp+'/namrr.'+pdy+'/namrr.t'+cyc+'z.fits_conusnest.tm'+tmxx
    filename=common_dir+'/fort.209'
    
# GET STATS FROM FILE
    with open(filename,'r') as searchfile:
         skiprows=1
         for line in searchfile:
             skiprows=skiprows+1
             if "current vfit of radar wind data" in line:
                 iti=iti+1
                 if(omb_it==iti):
                    skiprows_omb=skiprows
                 if(oma_it==iti):
                    skiprows_oma=skiprows
                    break
    df_omb=pd.read_csv(filename,skiprows=skiprows_omb,delimiter=r"\s+",nrows=4)
    df_oma=pd.read_csv(filename,skiprows=skiprows_oma,delimiter=r"\s+",nrows=4)



    for levi in range(len(levels)):
        level=levels[levi] # string name for df[level]
        print(level)
        for stati in range(3):
            stats_omb[expi,levi,stati]=float(df_omb[level][stati+1])
            stats_oma[expi,levi,stati]=float(df_oma[level][stati+1])

    for levi2 in range(len(levels2)):
        level2=levels2[levi2] # string name for df[level]
        print(level2)
        for stati2 in range(3):
            stats2_omb[expi,levi2,stati2]=float(df_omb[level2][stati2+1])
            stats2_oma[expi,levi2,stati2]=float(df_oma[level2][stati2+1])



###################################
fig = plt.figure(1,figsize=(10,6))#
fig_title_fontsize=18             #
xy_label_fontsize=16              #
tick_label_fontsize=14            #
legend_fontsize=8.8               #8.8
dot_size=50                       #40
l_dot_size=7                      #5
linewidth=3                       #2
###################################




if(var=='COUNT'): vari=0
if(var=='BIAS'): vari=1
if(var=='RMS'): vari=2

plot_all_exps=True

#ax1=plt.subplot(1,1,1)
ax1 = fig.add_subplot(111)
ylow=0; yhigh=levs; ax1.set_ylim(ylow,yhigh)

if(var=='COUNT'):
   xlow=0; xhigh=350000; ax1.set_xlim(xlow,xhigh)
   plt.xlabel(var,fontsize=xy_label_fontsize)

if(var == 'BIAS'):
   xlow=-1.0; xhigh=1.; ax1.set_xlim(xlow,xhigh)
   plt.xlabel(var+' (m/s)',fontsize=xy_label_fontsize)

if(var=='RMS'):
   xlow=0; xhigh=3; ax1.set_xlim(xlow,xhigh)
   plt.xlabel(var+' (m/s)',fontsize=xy_label_fontsize)

if(True):
   # XP
   #omb
   ax1.plot(stats_omb[0,:,vari],levels_int,color='#000000',marker='o',markersize=l_dot_size,label='control omb',    linewidth=linewidth,linestyle='-')
#   ax1.plot(stats_omb[1,:,vari],levels_int,color='#ff0044',marker='o',markersize=l_dot_size,label='w_only omb',     linewidth=linewidth,linestyle='-')
#   ax1.plot(stats_omb[2,:,vari],levels_int,color='#55ff00',marker='o',markersize=l_dot_size,label='w_so_elev5 omb', linewidth=linewidth,linestyle='-')
#   ax1.plot(stats_omb[3,:,vari],levels_int,color='#00aaff',marker='o',markersize=l_dot_size,label='w_so_elev10 omb',linewidth=linewidth,linestyle='-')
#   ax1.plot(stats_omb[4,:,vari],levels_int,color='#8800ff',marker='o',markersize=l_dot_size,label='so_elev10 omb',  linewidth=linewidth,linestyle='-')
#   #oma
   ax1.plot(stats_oma[0,:,vari],levels_int,color='#000000',marker='^',markersize=l_dot_size,label='control oma',    linewidth=linewidth,linestyle='--')
#   ax1.plot(stats_oma[1,:,vari],levels_int,color='#ff0044',marker='^',markersize=l_dot_size,label='w_only oma',     linewidth=linewidth,linestyle='--')
#   ax1.plot(stats_oma[2,:,vari],levels_int,color='#55ff00',marker='^',markersize=l_dot_size,label='w_so_elev5 oma', linewidth=linewidth,linestyle='--')
#   ax1.plot(stats_oma[3,:,vari],levels_int,color='#00aaff',marker='^',markersize=l_dot_size,label='w_so_elev10 oma',linewidth=linewidth,linestyle='--')
#   ax1.plot(stats_oma[4,:,vari],levels_int,color='#8800ff',marker='^',markersize=l_dot_size,label='so_elev10 oma',  linewidth=linewidth,linestyle='--')

   #0-2000 hpa level
   y_of_dot_omb=stats2_omb[0,:,vari]*0+0.5
   y_of_dot_oma=stats2_omb[0,:,vari]*0+0.25

   #omb
   ax1.scatter(stats2_omb[0,:,vari],y_of_dot_omb, marker='o',s=dot_size,color="#000000",label='control omb (t. atm.)')
#   ax1.scatter(stats2_omb[1,:,vari],y_of_dot_omb, marker='o',s=dot_size,color="#ff0044",label='w_only omb (t. atm.)')
#   ax1.scatter(stats2_omb[2,:,vari],y_of_dot_omb, marker='o',s=dot_size,color="#55ff00",label='w_so_elev5 omb (t. atm.)')
#   ax1.scatter(stats2_omb[3,:,vari],y_of_dot_omb, marker='o',s=dot_size,color="#00aaff",label='w_so_elev10 omb (t. atm.)')
#   ax1.scatter(stats2_omb[4,:,vari],y_of_dot_omb, marker='o',s=dot_size,color="#8800ff",label='so_elev10 omb (t. atm.)')
   #oma
   ax1.scatter(stats2_oma[0,:,vari],y_of_dot_oma, marker='^',s=dot_size,color="#000000",label='control oma (t. atm.)')
#   ax1.scatter(stats2_oma[1,:,vari],y_of_dot_oma, marker='^',s=dot_size,color="#ff0044",label='w_only oma (t. atm.)')
#   ax1.scatter(stats2_oma[2,:,vari],y_of_dot_oma, marker='^',s=dot_size,color="#55ff00",label='w_so_elev5 oma (t. atm.)')
#   ax1.scatter(stats2_oma[3,:,vari],y_of_dot_oma, marker='^',s=dot_size,color="#00aaff",label='w_so_elev10 oma (t. atm.)')
#   ax1.scatter(stats2_oma[4,:,vari],y_of_dot_oma, marker='^',s=dot_size,color="#8800ff",label='so_elev10 oma (t. atm.)')


ax1.set_yticks(levels_int)
ax1.set_yticklabels(levels)
ax1.axvline(x=0,color='lightgray')
plt.ylabel('vertical layer (hPa)',fontsize=xy_label_fontsize)
plt.setp(ax1.get_xticklabels(),visible=True,fontsize=tick_label_fontsize)
plt.setp(ax1.get_yticklabels(),visible=True,fontsize=tick_label_fontsize)

include_legend=True
legend_is_separate_figure=True
if(include_legend and not legend_is_separate_figure):
   leg=ax1.legend(fontsize=legend_fontsize,ncol=4,scatterpoints=1,loc='upper center',bbox_to_anchor=(0.,-0.2,1.,.102))
   leg=ax1.legend(fontsize=legend_fontsize,ncol=4,scatterpoints=1,loc='upper center')
   leg.get_frame().set_alpha(0.9)
   title=plt.suptitle('Radar winds OmB OmA statistics: %s \n %s t%sz tm%s' % (var,pdy,cyc,tmxx),fontsize=fig_title_fontsize,x=0.5,y=1.00)
   #plt.savefig('./'+var+'_'+pdy+'.namrr.t'+cyc+'z.fits_conusnest.tm'+tmxx+'.png',bbox_extra_artists=(leg,title,),bbox_inches='tight')
   plt.savefig('./'+var+'_'+pdy+'.fv3gfs.t'+cyc+'z.rwfits.tm'+tmxx+'.png',bbox_extra_artists=(leg,title,),bbox_inches='tight')

elif(include_legend and legend_is_separate_figure):
   title=plt.suptitle('Radar winds OmB OmA statistics: %s \n %s t%sz tm%s' % (var,pdy,cyc,tmxx),fontsize=fig_title_fontsize,x=0.5,y=1.00)
   #plt.savefig('./'+var+'_'+pdy+'.namrr.t'+cyc+'z.fits_conusnest.tm'+tmxx+'.png',bbox_extra_artists=(title,),bbox_inches='tight')
   plt.savefig('./'+var+'_'+pdy+'.fv3gfs.t'+cyc+'z.rwfits.tm'+tmxx+'.png',bbox_extra_artists=(title,),bbox_inches='tight')
   plt.ion(); plt.show() #; plt.pause(0.001); raw_input("Press [enter] to continue.") #create a blocking figure and waits for user to inspect
   figlegend = plt.figure(2,figsize=(20,2))
   plt.figlegend(*ax1.get_legend_handles_labels(),loc='center',fontsize=legend_fontsize,ncol=4,scatterpoints=1,prop={'size': 18})
   plt.ion(); plt.show() #; plt.pause(0.001); raw_input("Press [enter] to continue.") #create a non-blocking figure
   figlegend.savefig('legend.png')

else: #no legend
   title=plt.suptitle('Radar winds OmB OmA statistics: %s \n %s t%sz tm%s' % (var,pdy,cyc,tmxx),fontsize=fig_title_fontsize,x=0.5,y=1.00)
   #plt.savefig('./'+var+'_'+pdy+'.namrr.t'+cyc+'z.fits_conusnest.tm'+tmxx+'.png',bbox_extra_artists=(title,),bbox_inches='tight')
   plt.savefig('./'+var+'_'+pdy+'.fv3gfs.t'+cyc+'z.rwfits.tm'+tmxx+'.png',bbox_extra_artists=(title,),bbox_inches='tight')

