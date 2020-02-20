# WhoIsHome

Een Flask-site die weergeeft welke gebruikers thuis met het internet zijn verbonden.

## Wat is het?

WhoIsHome is een site gemaakt met Flask die door middel van een arp-scan ophaalt welke gebruikers er verbonden zijn met het internet thuis.
De voorwaarde is wel dat de server waar de site opstaat lokaal verbonden is met de router thuis.

## Waarom ben ik hier aan begonnen?

Ik ben aan dit project begonnen omdat ik buiten school ook nog graag wilde leren. Ik vind python, netwerken, linux en webdesign erg interessant,
ook wilde ik graag weten wie er thuis was. Daarom ben ik begonnen aan dit project. Ik ben van plan om er nog veel functies aan toe te voegen over tijd
en de bestaande functies te verbeteren en onderhouden.

## Hoe werkt het?

Allereerst heb ik een simpele site gemaakt met [Flask](https://flask.palletsprojects.com/en/1.1.x/) dit is een webapplicatie framework geschreven in python.
[Flask](https://flask.palletsprojects.com/en/1.1.x/) is erg goed gedocumenteerd, dus ik heb daar heel veel informatie en uitleg kunnen krijgen. Ook heb ik verschillende tutorials kunnen raadplegen.
Aan de site heb ik een login scherm met een userdatabase aan toegevoegd. 

Op 2 verschillende manieren wordt er gekeken naar wie er thuis is.

#### - Telenet site met cookies

Op de site van telenet bij de instellingen van jou router kan je precies zien wie er verbonden is. 
Om deze methode te kunnen gebruiken in mijn site gaat het script na de druk van de knop een curl doen van de telenet site waar de router instellingen staan door gebruik te maken van mijn cookies.
Daarna zoekt hij naar verschillende mac adressen ( die ik een bestand heb staan met de naam van de persoon ) in het bestand waar de curl naar wordt ge-output. 
Deze zet hij dan in een array die daarna gereturned wordt naar de site. Zodat je precies ziet wie er thuis is.

Omdat ik nog nooit met curl gewerkt heb en ik weinig kennis van cookies heb kan het soms zijn dat er een probleem is met de cookies waardoor hij geen curl kan doen.
Daarom heb ik nog een extra methode toegevoegd.

``` linux
curl -L -b cookies.txt "https://mijn.telenet.be/mijntelenet/rgw/settings.do?identifier=z087809&action=showAdvancedSettings" > c_out.txt
```
#### - Arp-scan

Als de curl om een of andere manier niet werkt gaat het script een arp-scan doen en vergelijkt de gevonden mac adressen met het bestand met bekende mac adressen.

```python
import subprocess
subprocess.call("sudo arp-scan --interface=wlan0 --localnet --plain | cut -f 2", universal_newlines=True, shell=True, stderr=error) 
```

### Wat heb ik ervan geleerd?

Ik heb veel meer geleerd van dit project dan dat ik verwacht had, maar toen ik steeds verder kwam met "WhoIsHome" en verschillende problemen tegenkwam die ik moest proberen op te lossen was het toch een stuk moeilijker dan verwacht.
Door de lessen 'Linux Essentials" op school was ik al een beetje bekend met Linux, maar door dit project heb ik zeer veel bijgeleerd. Zo heb ik bijvoorbeeld een bash script moeten schijven die de server automatisch opnieuw start als het proces gestopt is.


####  Ik heb onder andere ook veel bijgeleerd over:

- [Flask](https://flask.palletsprojects.com/en/1.1.x/) 
- Het werken in een [Linux](https://www.linux.org/) omgeving
- [Python](https://www.python.org/)
- [Waitress](https://docs.pylonsproject.org/projects/waitress/en/stable/#) (De WSGI server die ik gebruikt heb)
- [Curl](https://curl.haxx.se/)
- Netwerken 
- HTML templates maken

Ik heb erg veel tijd in dit project gestoken en ik ben er nog niet klaar mee. Ik wil graag zorgen dat alles altijd goed werkt, omdat er nog een aantal fouten inzitten of dingen die beter kunnen. 
Ook ben ik van plan om nog meerdere functies aan de site toe te voegen. En wil ik graag gebruik maken van nginx in plaats van waitress, maar dit was nog een beetje moeilijk.

### Wat vond ik nog moeilijk?

Aan het begin wist ik nog helemaal niks over Flask, maar na heel veel filmpjes gezien te hebben, en voorbeelden van code in Flask te hebben bekeken heb ik een aardig beeld gekregen over hoe het in elkaar steekt.

Ook wilde ik graag in het begin een ngnix server gebruiken, maar dit bleek nog wat te moeilijk te zijn. Daarom heb ik waitress gebruikt omdat het wat eenvoudiger is en het toch maar een lichte webapplicatie was.
Het netwerk gedeelte vond ik ook wat moeilijk aan het begin, omdat ik graag mijn site ook van buiten mijn thuisnetwerk wilde kunnen bereiken, maar ik niet wist hoe ik hier aan moest beginnen.


