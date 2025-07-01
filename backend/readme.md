# Setup backend after ma-clone
### This setup is for pycharm only, di ko pa nasusubukan sa vscode.

**1. open your terminal in pycharm**
Then paste this command:

For Windows user:

    python -m venv .venv    

For linux user: 

    python3 -m venv .venv

This will create a virtual environment.

**2. Activate the venv.**
   
For Windows user:
    
    
    /.venv/Scripts/activate
    
If encountered error something like this "running scripts is disabled on this system".
run this command
    
    Set-ExecutionPolicy RemoteSigned
    
if not works, pukpok mo na sa ulo mo. de joke. Just search cmd in your windows search bar and run as administrator.
Then re-run again the command. pag ayaw talaga, I google na.

**3. Install all required packages.**

Paste this in your terminal.
        
    pip install -r ./backend/requirements.txt
