## Configure

### Token for creating repo

Login Github and go to  account setting to create a peasonal  access token:

Settings -> Developer settings -> Personal access tokens -> Generate new token

And then add the token to the video-dl repo’s secrets

file-dl repo -> setting -> Secrets -> Action secrets -> New repository secret

name: ACCESS_TOKEN

value: content of the token

### SSH key for uploading video to repo

Use ssh-keygen tool to create a pair of ssh key with your github email:

```shell
ssh-keygen -t rsa -C "your@email.addr"
```

And then add the public key of the ssh key pair to your github setting:

Settings -> SSH and GPG keys -> New SSH key

Last, add the private key of the ssh key pair to the video-dl repo’s secrets

file-dl repo -> setting -> Secrets -> Action secrets -> New repository secret

name: SSH_PRIVATE_KEY 

value: content of ssh private key

### Setting user info for git environment

  Add the user name and user email to the file-dl repo’s secrets

file-dl repo -> setting -> Secrets -> Action secrets -> New repository secret

name: USER_NAME

value: your name of github account

name:USER_EMAIL

value: your email of github account

## Usage

In task.txt，

First line, fill link of **HTTP/HTTPS**, **BitTorrent** or **Metalink**,

Secend line, fill the target file path,

third line fill repo name.