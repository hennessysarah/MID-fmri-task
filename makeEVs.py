#This program will make EV files from the logfile collected during MID Task in fmri

#Sarah Hennessy, 2018


import os
import sys
import csv
import pandas as pd
import numpy as np

#reload(sys)



datafolder = "MID/data"
subjectlist = [elem for elem in os.listdir(datafolder) if "run" in elem]


print ('your subject list is:',subjectlist)


for subject in subjectlist: #subject = indiv file
    subj = subject[:-13]
    run = subject[-5]
    
    
    log = datafolder + '/%s_MID_run%s.txt' %(subj,run)
    evpath = "MID/EV"
    
    evfolder = evpath + '/%s_%s_evs' %(subj, run) 
    if os.path.exists(evfolder):
        print('Subject %s already has ev folder' %subj)
        continue
    else:
        os.makedirs(evfolder)
       

    #read in the text file

    data = pd.read_csv(log, delim_whitespace = True, comment = "#", header = "infer", skip_blank_lines = True, engine = "python")

   
    print('you are on run:',run)
    print('you are on subject:',subj)

    maxlen = data.shape[0]

    for index, row in data.iterrows():

        #WIN HIGH CORRECT
            if row.condition == 'win' and row.level == "large" and row.accuracy == 1:
               
                wevfilename = evfolder + '/winhighcorrect_run%s.txt' %(run)
                wevfile = open(wevfilename, 'a')
                wevfile.write('%0.4f\t%0.4f\t1\n' %(row.stim_onset, row.fb_length))
                wevfile.close()


            #WIN LOW CORRECT
            elif row.condition == 'win' and row.level == "small" and row.accuracy == 1:
                
                wevfilename = evfolder + '/winlowcorrect_run%s.txt' %(run)
                wevfile = open(wevfilename, 'a')
                wevfile.write('%0.4f\t%0.4f\t1\n' %(row.stim_onset, row.fb_length))
                wevfile.close()


            #LOSE HIGH CORRECT
            elif row.condition == 'lose' and row.level == "large" and row.accuracy == 1:
              
                wevfilename = evfolder + '/losehighcorrect_run%s.txt' %(run)
                wevfile = open(wevfilename, 'a')
                wevfile.write('%0.4f\t%0.4f\t1\n' %(row.stim_onset, row.fb_length))
                wevfile.close()

                
            #LOSE LOW CORRECT
            elif row.condition == 'lose' and row.level == "small" and row.accuracy == 1:
               
                wevfilename = evfolder + '/loselowcorrect_run%s.txt' %(run)
                wevfile = open(wevfilename, 'a')
                wevfile.write('%0.4f\t%0.4f\t1\n' %(row.stim_onset, row.fb_length))
                wevfile.close()

                

            #NEUTRAL 
            elif row.condition == 'neutral':
               
                wevfilename = evfolder + '/neutral_run%s.txt' %(run)
                wevfile = open(wevfilename, 'a')
                wevfile.write('%0.4f\t%0.4f\t1\n' %(row.stim_onset, row.fb_length))
                wevfile.close()


        #WIN HIGH INCORRECT
            elif row.condition == 'win' and row.level == "large" and row.accuracy == 0:
               
                wevfilename = evfolder + '/winhigh_incorrect_run%s.txt' %(run)
                wevfile = open(wevfilename, 'a')
                wevfile.write('%0.4f\t%0.4f\t1\n' %(row.stim_onset, row.fb_length))
                wevfile.close()


            #WIN LOW INCORRECT
            elif row.condition == 'win' and row.level == "small" and row.accuracy == 0:
                
                wevfilename = evfolder + '/winlow_incorrect_run%s.txt' %(run)
                wevfile = open(wevfilename, 'a')
                wevfile.write('%0.4f\t%0.4f\t1\n' %(row.stim_onset, row.fb_length))
                wevfile.close()


            #LOSE HIGH INCORRECT
            elif row.condition == 'lose' and row.level == "large" and row.accuracy == 0:
              
                wevfilename = evfolder + '/losehigh_incorrect_run%s.txt' %(run)
                wevfile = open(wevfilename, 'a')
                wevfile.write('%0.4f\t%0.4f\t1\n' %(row.stim_onset, row.fb_length))
                wevfile.close()

                
            #LOSE LOW INCORRECT
            elif row.condition == 'lose' and row.level == "small" and row.accuracy == 0:
               
                wevfilename = evfolder + '/loselow_incorrect_run%s.txt' %(run)
                wevfile = open(wevfilename, 'a')
                wevfile.write('%0.4f\t%0.4f\t1\n' %(row.stim_onset, row.fb_length))
                wevfile.close()


                

          

       


            

                

                            

                             
    
        
    
    
                       
    
