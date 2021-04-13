import copy

class memoryblock:
    def __init__(self,blockname,size):
        self.size = size
        self.blockname = blockname
        self.status = True #free
        self.unused = size
        self.job = job(0,"None","None")

    def setjob(self,currentjob):
        self.job = currentjob
        self.unused = self.unused - self.job.size

    def property(self):
        print(str(self.size) + " ",end='')
        if self.status == True:
            print("Available")
        else: print("Occupied")
        # true = Available
        # false = Occupied
        
    def setstatus(self,currentstatus):
        self.status = currentstatus

class job:
    def __init__(self,size,location,jobname):#index will represent the location
        self.size = size
        self.location = location
        self.jobname = jobname

    def setlocation(self,newlocation):
        self.location = newlocation

# receive num of block
nblocks = int(input("number of memory block: "))
mem = []

# receive size of memory of each block
for i in range(0,nblocks,1):
    mem.append(memoryblock("Block "+str(i+1),int(input("size of block " + str(i+1) + ": "))))

# duplicate a memory for First fit search
mem2 = copy.deepcopy(mem)

# receive num of jobs
njobs = int(input("number of jobs: "))
jobs = []

# receive size of each job
for i in range(0,njobs,1):
    jobs.append(job(int(input("size of jobs " + str(i+1) + ": ")),None,"Job"+str(i+1)))

# duplicate job for first fit search
jobs2 = copy.deepcopy(jobs)

# Best fit searh
print("\nBest fit search:\n")
if(len(mem)==0):
    print("    There is no memory block")
else:
    for i in range(0,len(jobs),1):
        for j in range(0,len(mem),1):
            if mem[j].status == True:#true is available
                if jobs[i].size <= mem[j].size:
                    if jobs[i].location == None:
                        jobs[i].setlocation(j)
                    elif mem[jobs[i].location].size > mem[j].size:
                        jobs[i].setlocation(j)
   
        if jobs[i].location != None:
            mem[jobs[i].location].setjob(jobs[i])
            mem[jobs[i].location].setstatus(False)
        else:
            print("    not enough memory for "+jobs[i].jobname)

print("\nInside Memory\n")
print(" block    size    jobs     used    unused")
for i in mem:
    print(i.blockname+"    "+str(i.size)+"    "+i.job.jobname+"   "+'{0: >5}'.format(str(i.job.size))+"   "+'{0: >5}'.format(str(i.unused))) 

#First fit search
print("\n\nFirst fit search:\n")
if(len(mem2)==0):
    print("    There is no memory block")
else:
    for k in range(0,len(jobs2),1):

        for j in range(0,len(mem2),1):
            if mem2[j].status== True:#true is available
                if jobs2[k].size<=mem2[j].size:
                    jobs2[k].setlocation(j)
                    break

        if jobs2[k].location != None:
            mem2[jobs2[k].location].setjob(jobs2[k])
            mem2[jobs2[k].location].setstatus(False)
        else:
            print("    not enough memory for "+jobs2[k].jobname)

print("\nInside Memory\n")
print(" block    size    jobs     used    unused")
for m in mem2:
    print(m.blockname+"     "+str(m.size)+"     "+m.job.jobname+"  "+'{0: >5}'.format(str(m.job.size))+"  "+'{0: >5}'.format(str(m.unused)))  

print("\n\n")