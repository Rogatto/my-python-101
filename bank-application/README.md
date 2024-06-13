# This is a simple bank system to study python and machine learning algorithms

## Just be sure you have make commandline available in your machine

````
brew install make
````

## After it you can use the command bellow to download dependencies

````
make
````

## If you want to manual install the dependencies:

````
pip install qrcode
pip install "qrcode[pil]"
pip install mysql-connector-python
````

To install Python packages system-wide, try brew install
xyz, where xyz is the package you are trying to
install.
    
If you wish to install a Python library that isn't in Homebrew,
use a virtual environment:

````
python3 -m venv path/to/venv
source path/to/venv/bin/activate
python3 -m pip install xyz
````

### Features to be developed

1. Create the database and DML for all structure
2. The classes should be filled from the database
3. Expose an API to show all accounts