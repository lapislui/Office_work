# sudo apt-get update -y && sudo apt-get upgrade -y

# sudo adduser frappe && usermod -aG sudo frappe && su hp cd /home/frappe

# sudo apt-get install git

# sudo apt-get install python3-dev python3-dev python3-setuptools python3-pip python3-distutils

# echo "python-versio:"
#  python3 --version

#  sudo apt-get install python3.10-venv

# sudo apt-get install software-properties-common

# sudo apt install mariadb-server mariadb-client

# sudo apt-get install redis-server

# sudo apt-get install xvfb libfontconfig wkhtmltopdf 
# sudo apt-get install libmysqlclient-dev

# sudo mysql_secure_installation

# sudo nano /etc/mysql/my.cnf

# sudo service mysql restart

# sudo apt install curl

# curl https://raw.githubusercontent.com/creationix/nvm/master/install.sh | bash 
# curl https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash
# nano ~/.profile 
# add following at end:
# export NVM_DIR="$HOME/.nvm"
# [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  
# [ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"

# source ~/.profile 
# nvm install 18

# sudo apt-get install npm

# sudo npm install -g yarn

# pip3 install frappe-bench

# bench init frappe-bench --frappe-path https://github.com/jaydeep-sigzen/frappe.git --version version-15

cd frappe-bench

sudo apt install supervisor -y

bench get-app --branch version-15 erpnext