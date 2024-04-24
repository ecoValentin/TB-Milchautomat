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


# Wo ist was
Das Projekt ist in \home\pi\Automat\ bzw. /home/pi/Device

Node Red Settings (Passwort/IP/Port)

      nano /home/pi/Device/NodeRed/settings.js

Mailzugangsdaten

      nano /home/pi/Device/NodeRed/env.txt


# Offene ToDos

 * Cloud Verbindung 
 * Sinnvolle Fernwartung (ohne PC beim Nutzer)