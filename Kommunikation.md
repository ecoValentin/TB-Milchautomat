# Kommunikationsdoku

Hier wird beschrieben was in home/pi/Automat/DEBUG/LIQUIDUS/Logging/mdbLog/netcatFullLog_[DATUM]_[Uhrzeit].txt geschrieben wird.

## Münzeinwurf 
### 1 €
    START,1

    NEWVEND,1.0

### 1€ + 2€
    START,1

    NEWVEND,1.0
    START,3

    NEWVEND,3.0

## Abbruch des Bezahlvorgangs
    VEND,0.0
    VEND,SUCCESS,COIN

    RESULT,1
    RESULT,SUCCESS,1

# Daemon Log
Hier wird beschrieben was in home/pi/Automat/DEBUG/LIQUIDUS/Logging/mdbLog/MDBdLog_[DATUM]_[Uhrzeit].txt geschrieben wird. Log Level: Trace

### Münzeinwurf langsam (erfolgreich)
    coinchanger.lua:380: VALUE1:  53
    coinchanger.lua:401: COIN_CHANGER,COIN_DEPOSITED,3,5
    paymentMasterDaemon.lua:312: Coin deposited, value:1 coinType:3
    paymentMasterDaemon.lua:492: Send: D,READER,0
    serial-connector-pi.lua:567: [Serial] send: D,READER,0
    coinchanger.lua:94: Coin changer state change ENABLED -> CREDIT
    paymentMasterDaemon.lua:514: Receive: d,ERR,"-1" 
    paymentMasterDaemon.lua:705: TCP Receive: NEWVEND,1.0
    paymentMasterDaemon.lua:514: Receive: p,5407
    coinchanger.lua:380: VALUE1:  54
    coinchanger.lua:401: COIN_CHANGER,COIN_DEPOSITED,4,7
    paymentMasterDaemon.lua:312: Coin deposited, value:2 coinType:4
    paymentMasterDaemon.lua:705: TCP Receive: NEWVEND,3.0

### Münzeinwurf schnell (nur erste Münze erkannt)
    coinchanger.lua:380: VALUE1:  53
    coinchanger.lua:401: COIN_CHANGER,COIN_DEPOSITED,3,2
    paymentMasterDaemon.lua:312: Coin deposited, value:1 coinType:3
    paymentMasterDaemon.lua:492: Send: D,READER,0
    serial-connector-pi.lua:567: [Serial] send: D,READER,0
    coinchanger.lua:94: Coin changer state change ENABLED -> CREDIT
    paymentMasterDaemon.lua:514: Receive: d,ERR,"-1" 
    paymentMasterDaemon.lua:514: Receive: p,4405
    coinchanger.lua:380: VALUE1:  44
    coinchanger.lua:401: COIN_CHANGER,COIN_DEPOSITED,4,5
    paymentMasterDaemon.lua:312: Coin deposited, value:2 coinType:4
    paymentMasterDaemon.lua:705: TCP Receive: NEWVEND,1.0
