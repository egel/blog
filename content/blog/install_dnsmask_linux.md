Title:		Install and configure dnsmasq on linux
Slug:			install-and-configure-dnsmasq-on-linux
Date:			2016-11-05
Status:	  Published
Category: How to
Tags:	    linux, frontend
Authors:	Maciej Sypień
Summary:  In few small steps I will try to show you how to setup your own instance of dnsmasq.


If you previously using `/etc/hosts` to manage your local domains and not heard about more effective way of managing local domains, you should try the old and good `dnsmasq` program to improve your development workflow.


### Installation process
Using the `apt-get` manager we will install core program.

```bash
sudo apt-get install dnsmasq
```

### Configuring dnsmasq as DNS server
Then when we have program installed, now we can get strict to the configuration. But before we will create backup file.


```bash
sudo cp /etc/dnsmasq.conf /etc/dnsmasq.conf.backup
```

In the example we want to use `loc` domain as our local domain (I not use `.dev` anymore due to now it is into standard global domains) and into `/etc/dnsmasq.conf` file we add:

```conf
listen-address=127.0.0.1
address=/loc/127.0.0.1
```

That is pretty much it. Next restart the service by:

```bash
sudo service dnsmasq restart
```

Final check if everything is ok and you are good to go.
```
ping wp.loc
PING wp.loc (127.0.0.1) 56(84) bytes of data.
64 bytes from localhost (127.0.0.1): icmp_seq=1 ttl=64 time=0.010 ms
64 bytes from localhost (127.0.0.1): icmp_seq=2 ttl=64 time=0.016 ms
64 bytes from localhost (127.0.0.1): icmp_seq=3 ttl=64 time=0.036 ms
64 bytes from localhost (127.0.0.1): icmp_seq=4 ttl=64 time=0.038 ms
```
