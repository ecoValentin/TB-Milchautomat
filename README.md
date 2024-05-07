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

# Bekannte Probleme
## Kommunikation zwischen RaspberryPi und Münzzähler
Es ist bekannt, dass der Betrag am Bildschirm nicht stimmt, wenn 2 Münzen gleichzeitig eingeworfen werden. 
Im Log findet sich:

      START,10.6
      NEWVEND,10.6START,10.7
      NEWVEND,10.6

Es sollte so aussehen:

      NEWVEND,10.6
      START,10.6
      NEWVEND,10.7
      START,10.7

Dies liegt höchstwahrscheinlich daran, dass die beiden Nachrichten gleichzeitig in verschiedene Richtungen am BUS gesendet werden. Eine mögliche Lösung wäre in paymentMasterDaemon.lua:288, nicht sofort zu senden, sondern erst eine Antwort (oder eine fixe Zeit) abzuwarten anstelle von

      sendToClient("START," .. tostring(newCredit) .. "\n")

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


# Offene ToDos

 * Cloud Verbindung 
 * Sinnvolle Fernwartung (ohne PC beim Nutzer)
