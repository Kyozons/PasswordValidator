import sys
import os
import subprocess
import time
import webbrowser

def UsuariosVici(macro, timeout_seconds = 10, var1 = '-', var2 = '-', var3 = '-', autorun_html = None):

    assert os.path.exists(autorun_html)

    args = r'file:///' + autorun_html + '?macro=' + macro + '&cmd_var1=' + var1 + '&cmd_var2=' + var2 + '&cmd_var3=' + var3 + '&closeRPA=1&direct=1'
    
    webbrowser.register('chrome',
                        None,
                        webbrowser.BackgroundBrowser("/usr/bin/google-chrome"))
    webbrowser.get('chrome').open(args)

if __name__ == '__main__':

   UsuariosVici('Usuarios_VICI', timeout_seconds = 20, autorun_html = r'/home/pedro.bustos.l/RPA/ui.vision.html')  
