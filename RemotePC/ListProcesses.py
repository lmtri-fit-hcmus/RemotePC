import psutil
#Trả về danh sách các process đang chạy trên máy
def ListProcesses():
    # Iterate over all running process
    for proc in psutil.process_iter():
        try:
            # Get process name & pid from process object.
            processName = proc.name()
            processID = proc.pid
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    #print('*** Create a list of all running processes ***')
    listOfProcessNames = list()
    # Iterate over all running processes
    for proc in psutil.process_iter():
       # Get process detail as dictionary
       pInfoDict = proc.as_dict(attrs=['pid', 'name', 'cpu_percent'])
       listOfProcessNames.append(pInfoDict)
    str = ''
    for elem in listOfProcessNames:
        str =str + elem['name'] +'\n'
    return str
