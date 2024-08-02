# Zugang zum Raspberry PI
## SSH Zugang verschaffen

Auf der zweiten Partition die Datei /home/pi/.ssh/autorized_keys um einen Key erweitern, dann hast du SSH (shell) Zugang und dann hast du mit "sudo su" auch Adminrechte und kannst alle PWs ändern.

## NodeRed Zugang:
Neuen PW hash generieren und in den Einstellungen von beiden NodeRed Instanzen einfügen (SSH):
   node-red-admin hash-pw

   nano home/pi/Automat/NodeRed/nodered1880_legal/settings.js
   nano home/pi/Automat/NodeRed/nodered1881_legal/settings.js

   sudo systemctl restart nodered

Login via Web-Browser:
   https://<IP des Automaten>:1880 bzw. https://<IP des Automaten>:1881
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

# Fernwartung

In "/home/pi/Automat/OpenVPN/" befindet sich eine Openvpn Konfigurationsdatei. Die kann durch eine andere ersetzt werden, Das Aufbauen einer VPN Verbindung muss ggf. im Node-Red aktiviert werden. Danach kann der Raspi, wenn er Internet hat im VPN von anderen Geräten im VPN verwaltet werden.

# Automat Aufbau

Das Herzstück bildet ein RaspberryPi mit CodeSYS. Dieser stellt den Bildschirm zur Verfügung, steuert die Motoren und überwacht die Temperatur.
Die Kommunikation mit den Beckhoff EtherCat Komponenten passiert über das angeschlossene Ethernet Kabel:

Der Raspi zeigt einen Webbrowser (localhost:8080) an.

# Versand Monatsabrechnung

Der ursprüngliche Versand funktioniert nichtmehr, da der notwendige Server nicht mehr reagiert. Als Alternative kann man monatliche Verkaufszahlen aus den Logs ermitteln und direkt vom Raspi versenden. Dazu kann das Skript "sales_per_month.py" verwendet werden.

# Offene ToDos
