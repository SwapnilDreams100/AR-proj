1) TO RUN IT ON LOCALHOST:
-> python -m http.server 1337

2) TO CONNECT LOCALHOST TO MOBILE:
-> make sure they are connected to the same network
-> make sure network is set to PRIVATE(network settings), to allow sharing of assets
-> get your pc's ip address using ifconfig - ipv4
-> then in your browser go https://ip:port

3) TO ADD TUNNELLING:
-> ./ngrok http 1337