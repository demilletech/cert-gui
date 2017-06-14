from OpenSSL import crypto
from OpenSSL.crypto import load_certificate_request, FILETYPE_PEM, X509, X509Req, PKey

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


def signCSR(csr: X509Req, ca: PKey): return csr.sign(ca, b"sha256")


def importCSR(csrText): return crypto.load_certificate_request(FILETYPE_PEM, csrText)
    # return components['cn']


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