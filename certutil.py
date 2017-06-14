import OpenSSL.crypto
from OpenSSL.crypto import load_certificate_request, FILETYPE_PEM

from os import listdir, popen
from os.path import isfile, join

import certconfig
import certsettings

def createKey(params):
    command = certconfig.cd + "; " + certconfig.generateKey + "; " + certconfig.generateKeyPerms
    fcommand = certconfig.createCommand(command, params)
    stream = execute(fcommand)

def genCSR(params):
    command = certconfig.cd + "; " + certconfig.generateCSR
    fcommand = certconfig.createCommand(command, params)
    stream = execute(fcommand)
    
def signCSR(cn):
    csr = open(certsettings.settings['crlRequestsDir'] + cn + ".csr.pem")
    req = load_certificate_request(FILETYPE_PEM, csr)
    params = getCSRParams(req)
    
    command = certconfig.cd + "; " + certconfig.signCSR + "; " + certconfig.signCSRPerms
    fcommand = certconfig.createCommand(command, params)
    stream = execute(fcommand)

def importCSR(csrText):
    req = load_certificate_request(FILETYPE_PEM, csrText)
    key_type = 'RSA' if key.type() == OpenSSL.crypto.TYPE_RSA else 'DSA'
    components = getCSRParams(req)
    
    filename = components['CN'] + ".csr.pem"
    file = open(filename)
    file.write(csrText)
    
    return components['cn']
    
def getCSRParams(cn):
    subject = req.get_subject()
    components = dict(subject.get_components())
    return components

def getAllCSR():
    csrdir = certsettings.settings['certRequestsDir']
    onlyfiles = [f for f in listdir(csrdir) if isfile(join(csrdir, f))]
    return onlyfiles

def execute(command):
    return os.popen(command)