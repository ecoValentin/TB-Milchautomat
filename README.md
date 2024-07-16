# Zugang zum Raspberry PI
## SSH Zugang verschaffen

Auf der zweiten Partition die Datei /home/pi/.ssh/autorized_keys um einen Key erweitern, dann hast du SSH (shell) Zugang und dann hast du mit "sudo su" auch Adminrechte und kannst alle PWs ändern.

## NodeRed Zugang:
Neuen PW hash generieren und in den Einstellungen einfügen (SSH):
   node-red-admin hash-pw

   nano ~/.node-red/settings.js

   sudo systemctl restart nodered

Login via Web-Browser:
   https://<IP des Automaten>:1880
   User: admin
   PW: <pw>

## Umschalten zwischen Konsole und Bildschirm
Mit STRG+ALT+F1 kommst du zu einer Konsole, in der auch Dinge geloggt werden
Mit STRG+ALT+F6 wieder retour

## Firewallregeln
Folgenede Firewallregel erlaubt Vollzugriff über VPN:

    nano /etc/iptables/rules.v4
    -A INPUT -s 10.8.0.0/24 -j ACCEPT
    iptables-restore /etc/iptables/rules.v4

# Bekannte Probleme
## Kommunikation zwischen RaspberryPi und Münzzähler
Es ist bekannt, dass der Betrag am Bildschirm nicht stimmt, wenn 2 Münzen gleichzeitig eingeworfen werden. 

Siehe Kommunikation.md

## Kommunikation zwischen Münzzähler und RaspberyyPi beobachten
      cd /home/pi/Automat/DEBUG/LIQUIDUS/Logging/mdbLog

      tail -f netcatFullLog_[DATUM]_[Uhrzeit].txt
      tail -f MDBdLog_[DATUM]_[Uhrzeit].txt

      e.g.
      tail -f MDBdLog_2024-05-07_12-56-29.txt

## Neustart kurz nach Start:
sudo systemctl disable setHostname.service

# Wo ist was
Das Projekt ist in \home\pi\Automat\ bzw. /home/pi/Device

Node Red Settings (Passwort/IP/Port)

      nano /home/pi/Device/NodeRed/settings.js

Mailzugangsdaten

      nano /home/pi/Device/NodeRed/env.txt

Die Dateien die per Mail verschickt werden sind hier:
      
      /home/pi/Automat/Logging/MailLog

Die Excel/csv von den Verkaufszahlen/Temperaturwerten ist hier:

      /home/pi/LIQUIDUS/Logging/

# PiHat

## MDB Daemon 
Der Raspi benutzt einen MDB PiHat um den Münzzähler (und das Kartenterminal) zu steuern. DIes ist die Doku davon:

https://docs.qibixx.com/mdb-products/mdb-payment-master-daemon

## Firmware Update
https://docs.qibixx.com/mdb-products/mdb-pi-hat-firmware-update

# Fernwartung

In "/home/pi/Automat/OpenVPN/" befindet sich eine Openvpn Konfigurationsdatei. Die kann durch eine andere ersetzt werden, Das Aufbauen einer VPN Verbindung muss ggf. im Node-Red aktiviert werden. Danach kann der Raspi, wenn er Internet hat im VPN von anderen Geräten im VPN verwaltet werden.

# Automat Aufbau

Das Herzstück bildet ein iPC (z.B. CX8190). Der hat ein Windows 7 CE Embedded drauf installiert, da drinnen läuft eine Softwareumgebung die einiges tut:
Webserver (Anzeige am Automaten)
Ethernet (Kommunikation mit Raspi)
Programmierung und Aktualisierung des auch eingebauten SPS

Er kann nicht über mdbd mit dem Münzzähler und dem Kartenleser kommunizieren, deswegen macht der Raspi da eine Brücke. Er kann auch nicht direkt den Bildschirm ansteueren, deswegen zeigt der Raspi einen Webbrowser an, der wiederum die Seite vom iPC aufruft.

# Offene ToDos

 * Cloud Verbindung 
 * Schneller Münzeinwurf Fehlersuche
