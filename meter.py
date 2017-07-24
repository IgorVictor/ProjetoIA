import requests
import time
import os.path

req = requests.Session()


#Gets all jobs, useful for the ocasional debugging
def getalljobs() :
    n = req.get("http://##.##.##.##:#####/arrebol/nonce")
    header = { "X-auth-credentials":"{ username: ########, password: #######, nonce: "+ n.text+" }"}
    r = req.get("http://##.##.##.##:#####/arrebol/job", headers=header)
    return r

#Posts the sleep.jdf job, it's a simple job that asks the target machine to sleep por 10 seconds, with no in-out operations
def postjob(jobpath) :
    n = req.get("http://##.##.##.##:#####/arrebol/nonce")
    header = { "X-auth-credentials":"{ username: ########, password: #######, nonce: "+ n.text+" }"}
    r = req.post("http://##.##.##.##:#####/arrebol/job",
         files={
             "jdffilepath": ("", jobpath),
             "X-auth-credentials": ("", "{ username: ########, password: #######, nonce: "+ n.text+ "}")}, headers=header)
    return r

#Gets the info on the sleepjob, job233 it's the label name of this job
def getjob(jobname) :
    n = req.get("http://##.##.##.##:#####/arrebol/nonce")
    header = { "X-auth-credentials":"{ username: ########, password: #######, nonce: "+ n.text+" }"}
    r= req.get("http://##.##.##.##:#####/arrebol/job/"+jobname, headers=header)
    return r


#Deletes the sleepjob from arrebol, cleaning the system for future tests, since a job isn't removed unless asked and no two jobs can have the same label
def deletejob(jobname) :
    n = req.get("http://##.##.##.##:#####/arrebol/nonce")
    header = { "X-auth-credentials":"{ username: ########, password: #######, nonce: "+ n.text+" }"}
    r= req.delete("http://##.##.##.##:#####/arrebol/job/"+jobname,
       files={
              "X-auth-credentials": ("", "{ username: ########, password: #######, nonce: "+ n.text+ "}")}, headers=header)
    return r



def checkjob(reqstring) :
    if "COMPLETED" in reqstring:
        return True
    return False

def positivesleepresult() :
    print "PASSOU SLEEP!"

def negativesleepresult() :
    print "NAO PASSOU SLEEP!"

def positiveinoutresult() :
    print "PASSOU INOUT!"

def negativeinoutresult() :
    print "NAO PASSOU INOUT!"
# {"tenk1m", "tenk10m", "hun1m", "hun10m", "one1m", "one10m"}
def main():
    timer = 0
	postjob("/home/igorvcs/jdfs/tenk1ma.jdf")
	while (!checkjob(getjob("tenk1ma")):
	  time.sleep(1)
	  timer++
	resultfile = open("results.txt", "a")
	resultfile.write("tenk1m "+ timer+ "\n")
	deletejob("tenk1ma")
	timer = 0
	postjob("/home/igorvcs/jdfs/tenk10ma.jdf")
	while (!checkjob(getjob("tenk10ma")):
	  time.sleep(1)
	  timer++
	resultfile.write("tenk10m "+ timer+ "\n")
	deletejob("tenk10ma")
	timer = 0
	postjob("/home/igorvcs/jdfs/hun10ma.jdf")
	while (!checkjob(getjob("hun10ma")):
	  time.sleep(1)
	  timer++
	resultfile.write("hun10m "+ timer+ "\n")
	deletejob("hun10ma")
	timer = 0
	postjob("/home/igorvcs/jdfs/hun1ma.jdf")
	while (!checkjob(getjob("hun1ma")):
	  time.sleep(1)
	  timer++
	resultfile.write("hun1m "+ timer+ "\n")
	deletejob("hun1ma")
	timer = 0
	postjob("/home/igorvcs/jdfs/one10ma.jdf")
	while (!checkjob(getjob("one10ma")):
	  time.sleep(1)
	  timer++
	resultfile.write("one10m "+ timer+ "\n")
	deletejob("one10ma")
	timer = 0
	postjob("/home/igorvcs/jdfs/one1ma.jdf")
	while (!checkjob(getjob("one1ma")):
	  time.sleep(1)
	  timer++
	resultfile.write("one1m "+ timer+ "\n")
	deletejob("one1ma")
    resultfile.close()
	resultten = open("resultten.txt", "a")
	jdfdict = {"tenk1m", "tenk10m", "hun1m", "hun10m", "one1m", "one10m"}
	for a in jdfdict:
		letterdict = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j"}
		for k in letterdict:
		  postjob("/home/igorvcs/jdfs/"+a+k+".jdf")
        timer = 0
        while len(letterdict) > 0:
			removelist = []
			for m in letterdict :
			  if (checkjob(getjob(a+m)) :
			    resultten.write(a+m + " "+ timer+ "\n")
                removelist.append(m)				
            for g in removelist:
			  del letterdict[g]

if __name__ == "__main__":
    main()