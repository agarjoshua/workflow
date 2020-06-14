

# Imports for selective yt playlist
from selenium import webdriver
from getpass import getpass
from webdriver_manager.chrome import ChromeDriverManager
# Imports for internal subprocesses
import subprocess


# Script that opens my favourite youtube playlist
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://www.youtube.com/playlist?list=PLvNfwQlwCdEpfHOZWckGcJ76E_wSKRK8S')

driver = driver.find_element_by_css_selector('#img')
driver.click()


# this section opens my vscode workstation and last project
input('press y to open a new vs window')

subprocess.Popen('C:...\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe')
