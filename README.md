# Notes

## Docker

### Installation

```
sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
sudo apt-get update && sudo apt-get install docker-ce
sudo usermod -a -G docker $(whoami)
```

## Molecule

### Installation

```
sudo apt-get update && sudo apt-get install gcc python-pip libssl-dev libffi-dev virtualenv
virtualenv .
source bin/activate
pip install ansible
pip install docker
pip install molecule
```

### Development

```sh
cd src/roles/mopidy
molecule test
```

In the container:
```sh
nohup /usr/bin/mopidy --config /etc/mopidy/mopidy.conf &
```

Useful commands:

docker exec -it mopidy bash
apt-cache madison mopidy


## Running it

```sh
# ansible-galaxy install -r requirements.yml
ansible-playbook site.yml --ask-vault-pass
```
