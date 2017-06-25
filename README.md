# LAN-Copy-Paste

A very minimalistic way to copy-paste text across LAN devices.

## Screenshots:

<img src="http://i.imgur.com/BQxzMov.png" width="350">
<img src="http://i.imgur.com/ciYhuyr.png" width="330">

## Installation & Usage:

```
git clone https://github.com/Ritiek/LAN-Copy-Paste
cd LAN-Copy-Paste
pip install -r requirements.txt
```

### Server:

- To run the copy-paste server:

`python copy-paste-server.py`

- Go to `localhost:6664` to start using this universal clipboard!

- You can edit out the script to use any custom port you like.

### Client:

- You can also use `copy-paste-client.py` to retrieve and post text directly via the command-line

For example:
  
- To retrieve text: `python copy-paste-client.py > text_from_server.txt`
  
- To post text: `python copy-paste-client.py 'This text goes on the server'`

## License:

`The MIT License`
