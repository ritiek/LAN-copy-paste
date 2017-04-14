# LAN-Copy-Paste

Copy and paste text across devices on LAN.

## Screenshots:

<img src="http://i.imgur.com/BQxzMov.png" width="350">
<img src="http://i.imgur.com/ciYhuyr.png" width="350">

## Installation & Usage:

- You need to install `Flask`:

`sudo pip install Flask`

- Clone this repository and cd into it:

`git clone https://github.com/Ritiek/LAN-Copy-Paste`

`cd LAN-Copy-Paste`

- Now just run the python script:

### Server:

`sudo python copy-paste-server.py`

- Goto `YourIP:6664` to start using this universal clipboard!

- You can edit out the script to use any custom port you like.

### Client:

- You can also use `copy-paste-client.py` to retrieve and post text directly via the command-line

  For example:
  
  - To retrieve text: `sudo python copy-paste-client.py > TextOnServer.txt`
  
  - To post text: `sudo python copy-paste-client.py 'This text goes on the server'`

## License:

`The MIT License`
