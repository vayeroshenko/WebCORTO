# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.shortcuts import render_to_response
from django import forms
import subprocess
import commands
import sys


from django.conf import settings

# Create your views here.

#Main page

def index(request):
    settings.ANAFOLDER = "/home/gred/corto_win2/ana"
    screentext = gettemplog()
    lanstatus=isinlan()
    cstatus = cismounted()
    lstatus = lismounted()
    crontabstatus = isconvert()
    lanchecked = 'checked' if lanstatus else ''
    cischecked = 'checked' if cstatus else ''
    lischecked = 'checked' if lstatus else ''
    isconverting = 'checked' if crontabstatus else ''
    changestatec = '/cunmount/' if cstatus else '/cmount/'
    changestatel = '/lunmount/' if lstatus else '/lmount/'
    changelabelc = 'Unmount' if cstatus else 'Mount'
    changelabell = 'Unmount' if lstatus else 'Mount'
    changecrontab = 'Turn off' if crontabstatus else 'Turn on'
    changecrontabadress = '/crontaboff/' if crontabstatus else '/crontabon/'
   
    if (varvalue('SYNCISOVER') and varvalue('CONVISOVER') and varvalue('RECOISOVER') and (not varvalue('RUNISSTARTED'))):
        runheader = 'Start new run'
        runnumfield = '<input id="runnum" type="text" name="runnumber" size="5" placeholder="Run number">'
        newid = 'start'
        newclickable=''
    elif varvalue('RUNISOVER'):
        runheader = 'Stop run'
        newid = 'stop'
        newclickable=''
        runnumfield=''
    else:
        runnumfield=''
        newid='hidden'
        runheader ='Run is in process'
        newclickable = 'disabled'
    

    return render(request,'corto/index.html', {'templog':screentext,'cismounted':cischecked,'lismounted':lischecked, 'changestatec':changestatec, 'changestatel':changestatel, 'changelabelc':changelabelc,'changelabell':changelabell, 'changecrontab':changecrontab,'changecrontabadress':changecrontabadress,'isconvert':isconverting, 'isinlan':lanchecked, 'runheader':runheader, 'newid':newid, 'runnumfield':runnumfield, 'newclickable':newclickable, 'newlabel':newid.upper() })

#Buttons 

def button1(request):
    return HttpResponseRedirect ('http://134.158.91.46')

def cmount(request):
    run = '/home/gred/corto_win2/ana/setupmount.bash'
    screentext = commands.getoutput(run)
    writelog(screentext)
    return HttpResponseRedirect ('http://134.158.91.46')

def lmount(request):
    run = '/home/gred/corto_win2/ana/setupmount.bash'
    screentext = commands.getoutput(run)
    writelog(screentext)
    return HttpResponseRedirect ('http://134.158.91.46')

def cunmount(request):
    run = '/home/gred/corto_win2/ana/setupunmount.bash'
    screentext = commands.getoutput(run)
    writelog(screentext)
    return HttpResponseRedirect ('http://134.158.91.46')

def lunmount(request):
    run = '/home/gred/corto_win2/ana/setupunmount.bash'
    screentext = commands.getoutput(run)
    writelog(screentext)
    return HttpResponseRedirect ('http://134.158.91.46')

def crontabon(request):
    run = 'su -c "crontab /home/gred/corto_win2/ana/crontab.file" -s /bin/bash gred'
    screentext = commands.getoutput(run)
    writelog(screentext)
    return HttpResponseRedirect ('http://134.158.91.46')

def crontaboff(request):
    run = 'su -c "crontab -r" -s /bin/bash gred'
    screentext = commands.getoutput(run)
    writelog(screentext)
    return HttpResponseRedirect ('http://134.158.91.46')

def convert(request):
    run = 'su -c ". /home/gred/corto_win2/ana/rawdataconv/rawdataconv.screen.bash" -s /bin/bash gred'
    reload(sys)
    sys.setdefaultencoding('utf8')
    screentext = commands.getoutput(run)
    writelog(screentext)
    return HttpResponseRedirect ('http://134.158.91.46')

def forcesync(request):
    run = 'su -c "/home/gred/corto_win2/ana/makeFilesync.screen.bash" -s /bin/bash gred'
    reload(sys)
    sys.setdefaultencoding('utf8')
    screentext = commands.getoutput(run)
    writelog(screentext)
    return HttpResponseRedirect ('http://134.158.91.46')

def forceconv(request):
    run = 'su -c "/home/gred/corto_win2/ana/makeFileconv.screen.bash" -s /bin/bash gred'
    reload(sys)
    sys.setdefaultencoding('utf8')
    screentext = commands.getoutput(run)
    writelog(screentext)
    return HttpResponseRedirect ('http://134.158.91.46')


def make(request):
    run = 'su -c ". /home/gred/corto_win2/ana/make.bash" -s /bin/bash gred'
    reload(sys)
    sys.setdefaultencoding('utf8')
    screentext = commands.getoutput(run) 
    writelog(screentext)
    return HttpResponseRedirect ('http://134.158.91.46')

def makeclean(request):
    run = 'su -c ". /home/gred/corto_win2/ana/makeclean.bash" -s /bin/bash gred'
    screentext = commands.getoutput(run)
    writelog(screentext)
    return HttpResponseRedirect ('http://134.158.91.46')


def clear(request):
    templogfile = open('/home/gred/corto_win2/WebCorto/templog.txt', 'w')
    templogfile.close()
    return HttpResponseRedirect ('http://134.158.91.46/')

def startrun(request):
    runnumber = str(request.POST['runnumber'])
    run = '/home/gred/corto_win2/ana/startRun.bash ' + runnumber
    screentext = commands.getoutput(run) 
    reload(sys)
    sys.setdefaultencoding('utf8')
    writelog(screentext)
    return HttpResponseRedirect ('http://134.158.91.46/')

def stoprun(request):
    run = '/home/gred/corto_win2/ana/stopRun.bash '
    screentext = commands.getoutput(run) 
    writelog(screentext)
    return HttpResponseRedirect ('http://134.158.91.46/')

def wccheck(request):
    run = '/home/gred/corto_win2/ana/check-USB-WC-status.bash'
    screentext = commands.getoutput(run) 
    writelog(screentext)
    return HttpResponseRedirect ('http://134.158.91.46/')



#Checkboxes

def cismounted():
    run = '/home/gred/corto_win2/ana/check-PC-SERDI6-ismount.bash C'
    if commands.getoutput(run) == '1':
        return True
    else:
        return False

def lismounted():
    run = '/home/gred/corto_win2/ana/check-PC-SERDI6-ismount.bash L'
    if commands.getoutput(run) == '1':
        return True
    else:
        return False

def isinlan():
    run = '/home/gred/corto_win2/ana/check-LAL-network.bash'
    if commands.getoutput(run) == '1':
        return True
    else:
        return False

#Crontab job

def isconvert():
    string = commands.getoutput('su -c "crontab -l" -s /bin/bash gred')
    return False if (string.find('convert')==(-1)) else True


#Check status file

def varvalue(varname):
    statusfile = open('/home/gred/corto_win2/ana/dataanastatus')
    status = statusfile.read().split()
    for i, w in enumerate(status):
        if w == varname:
            return eval(status[i+1])
    


#Writing and reading log files

def gettemplog():
    templogfile = open('/home/gred/corto_win2/WebCorto/templog.txt', 'r')
    templog = templogfile.read()
    templogfile.close()
    return templog

def writelog(log):
    templogfile = open('/home/gred/corto_win2/WebCorto/templog.txt', 'a')
    logfile = open('/home/gred/corto_win2/WebCorto/log.txt', 'a')
    templogfile.write(log.replace('\n', '<br>').replace(' ', '&nbsp')+'<br>');
    logfile.write(log.replace('<b>','').replace('</b>','')+'\n');
    templogfile.close()
    logfile.close()
    return 0

class StartRunForm(forms.Form):
    runnumber = forms.CharField(label='Run number', max_length=100)
    
