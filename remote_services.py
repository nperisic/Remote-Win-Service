import config


def remoteservices(command = 'query', service ):
    '''
    https://ss64.com/nt/sc.html
    :param command: start, stop, query
    :service : service name
    :return:
    >>> s = nexusStartStopStatus()
    4
    '''
    configFile = config.get_config() #open config file
    serverAdressHub = configFile['serverAdressHub']
    usernameMS = configFile['usernameMS']
    passwordMS = configFile['passwordMS']
    cp_command = r"net use \\{}\ipc$ {} /user:{} | sc \\{} {} {}".format(serverAdressHub, passwordMS, usernameMS,
                                                                            serverAdressHub, command, service)
    cp_output = subprocess.check_output(cp_command, shell = True)
    cp_output = ((str(cp_output)).split('\\r\\n'))
    for output in cp_output:
        patern = re.search("^.*STATE.*:.[0-9]..", output)
        if patern:
            state = (output[patern.span()[1]:-1])
            return (state)
