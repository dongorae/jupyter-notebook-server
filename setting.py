from notebook.auth import passwd

passwd_encrypted = passwd()

jupyter_config = f"""
c = get_config()
c.NotebookApp.ip = '0.0.0.0'
c.NotebookApp.password = u'{passwd_encrypted}'
c.NotebookApp.open_browser = False
c.NotebookApp.port = 8888
"""

with open("jupyter_notebook_config.py", "w") as f:
    f.write(jupyter_config)
