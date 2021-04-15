**Prefer [native mingw instructions](https://github.com/miguelfreitas/twister-core/wiki/Build-native-Windows-client-using-Gitian), cygwin builds are known to have issues.**

1. Install cygwin from [http://cygwin.com/](http://cygwin.com/)

2. During setup the following packages must be selected:
 * autoconf
 * automake
 * libboost-devel
 * libdb4.8-devel
 * libtool
 * gcc-g++
 * git
 * make
 * openssl-devel
 * tar
 * (add here missing packages)

3. Download twister from github

 `git clone https://github.com/miguelfreitas/twister-core.git`

 `cd twister-core`

4. Compile twisterd

 `./bootstrap.sh`

 `make`

5. Create .twister directory and download HTML UI

 `mkdir ~/.twister`

 `cd ~/.twister`

 `git clone https://github.com/miguelfreitas/twister-html.git html`

6. Now configure your username and password for the daemon:

 `echo -e "rpcuser=user\nrpcpassword=pwd" > ~/.twister/twister.conf`

 (NOTE: The username/password combo seems temporarily hardcoded. Also, if you receive an error message about "cygwin1.dll", add your cygwin path to the PATH environmental variable, eg. "C:\Cygwin64\bin".)

7. Run the daemon:

 `./twisterd -daemon -rpcuser=user -rpcpassword=pwd -rpcallowip=127.0.0.1`

8. Open http://127.0.0.1:28332/index.html and use the user/pwd credentials.

## Notes
* windows users are reporting problems to bootstrap the network (no connections). Try to manually add peer from one of the following seeder (try both "add peer" and "add dns"): `seed.twister.net.co` `seed2.twister.net.co` `seed3.twister.net.co` `dnsseed.gombadi.com`

* You may need to edit file `/usr/lib/libdb_cxx-4.8.la` to remove a wrong dependency (cygwin bug).

 * Replace: `dependency_libs=' /usr/lib/libdb-4.8.la -lpthread /usr/lib/gcc/i686-pc-cygwin/4.5.3/libstdc++.la'`

 * With: `dependency_libs=' /usr/lib/libdb-4.8.la -lpthread'`

* The following dlls are needed in order to run twisterd.exe (the file is inside .libs directory):

 cygboost_filesystem-mt-1_53.dll cygboost_system-mt-1_53.dll cygcrypto-1.0.0.dll  cygdb_cxx-4.8.dll  cygssl-1.0.0.dll  cygwin1.dll cygboost_program_options-mt-1_53.dll  cygboost_thread-mt-1_53.dll  cygdb-4.8.dll cyggcc_s-1.dll cygstdc++-6.dll cygz.dll

@wrewolf can build in clean Win XP SP3 x86 with latest cygwin (with upper *note* /\), but modify original cygwin headers and insert defines from win32 headers.
insert in file
/usr/include/cygwin/in6.h
lines from
/usr/include/w32api/ws2ipdef.h

```c++
#define IPV6_HOPOPTS           1
#define IPV6_HDRINCL           2
#define IPV6_UNICAST_HOPS      4
#define IPV6_MULTICAST_IF      9
#define IPV6_MULTICAST_HOPS    10
#define IPV6_MULTICAST_LOOP    11
#define IPV6_ADD_MEMBERSHIP    12
#define IPV6_JOIN_GROUP        IPV6_ADD_MEMBERSHIP
#define IPV6_DROP_MEMBERSHIP   13
#define IPV6_LEAVE_GROUP       IPV6_DROP_MEMBERSHIP
#define IPV6_DONTFRAG          14
#define IPV6_PKTINFO           19
#define IPV6_HOPLIMIT          21
#define IPV6_PROTECTION_LEVEL  23
#define IPV6_RECVIF            24
#define IPV6_RECVDSTADDR       25
#define IPV6_CHECKSUM          26
#define IPV6_V6ONLY            27
#define IPV6_IFLIST            28
#define IPV6_ADD_IFLIST        29
#define IPV6_DEL_IFLIST        30
#define IPV6_UNICAST_IF        31
#define IPV6_RTHDR             32
#define IPV6_RECVRTHDR         38
#define IPV6_TCLASS            39
#define IPV6_RECVTCLASS        40
```

And build without any modifycation sources
```
./bootstrap.sh
make V=1
```