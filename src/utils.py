import requests
from bs4 import BeautifulSoup
import re
from re import Pattern
import sys
from enum import Enum


versionStr = ''.join([f'{x}' for x in sys.version_info[0:2]])
regexCPython = re.compile(r'-cp(\d+)-')
regexLinux = re.compile(r'-linux_')
# regexSegment = re.compile(r'-([a-zA-Z0-9]+)')

reDevice = re.compile(r'([cpuda]{2,3}\d)')
class EPlatformPytorch(str, Enum):
    DARWIN = 'macosx'
    LINUX = 'linux'
    pass

URL_PYTORCH_DOWNLOAD = 'https://download.pytorch.org'

def getPytorchWheelHtml(package, device) -> str:
    r = requests.get(f'{URL_PYTORCH_DOWNLOAD}/whl/{device}/{package}', headers={ 'accept': 'text/html' })
    return r.text

def getBsObject(htmlTxt) -> BeautifulSoup:
    return BeautifulSoup(htmlTxt, 'html.parser')

def getPytorchWheelLinks(
        package, 
        device,
        version
        # platform=EPlatformPytorch.LINUX
    ) -> list[str]:
    res = getPytorchWheelHtml(package, device)
    bs = getBsObject(res)
    tousLesLiens: list[str] = [x.get('href') for x in bs.find_all('a')]

    ret = [
        x for x in tousLesLiens 
        if x.startswith(f'/whl/{device}/{package}-{version}') 
        and versionStr in regexCPython.findall(x)
        # and regexLinux.findall(x)
        # and str(platform) in regexSegment.findall(x)
    ]
    return ret


def rmTrailingHash(link: str) -> str:
     return link.split('#')[0]


if __name__ == '__main__':
    device='cu121' #'cpu'
    # 
    liensTorch: list[str] = getPytorchWheelLinks('torch', device, '2.2.0')
    liensVision: list[str] = getPytorchWheelLinks('torchaudio', device, '2.2.0')
    liensAudio: list[str] = getPytorchWheelLinks('torchvision', device, '0.17.0')
    
    if len(liensTorch) == 1:
        print(f"torch @ {URL_PYTORCH_DOWNLOAD}{rmTrailingHash(liensTorch[0])}")

    if len(liensVision) == 1:
        print(f"torchaudio @ {URL_PYTORCH_DOWNLOAD}{rmTrailingHash(liensAudio[0])}")

    if len(liensAudio) == 1:
        print(f"torchvision @ {URL_PYTORCH_DOWNLOAD}{rmTrailingHash(liensVision[0])}")
    # 
    pass