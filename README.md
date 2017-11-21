### How to install
```sh
# download source
git clone https://github.com/kana-sama/translit.git

# move to dir with source
cd translit

# download dependencies
pip install -r requirements.txt

# make file for tests executable
chmod +x gen.sh

# create test folder
./gen.sh

# translit all files in test folder
python main.py
```