# main.py

import subprocess
import time

from flask import Blueprint, render_template
from flask_login import login_required, current_user
from waitress import serve
import sys

localtime = time.asctime(time.localtime(time.time()))
main = Blueprint('main', __name__)


@main.route('/')
@login_required
def index():
    return render_template('profile.html', name=current_user.name)


@main.route('/whoishome')
@login_required
def whoishome():
    log = open('err.txt', 'a')
    log.write("Server gestart       " + localtime + '\n')
    log.write(current_user.name + ' is aangemeld  ' + localtime + '\n')
    drop = open('/dev/null', 'w')

    adressen = {'A8:DB:03:BE:84:12': "Moussas_telefoon", "70:C9:4E:61:D5:5F": "Moussas_pc",
                "24:18:1D:8D:19:82": "Mamas_telefoon", "6C:AB:31:19:48:79": "Dounyas_telefoon",
                "24:18:1D:76:02:60": "Papas_telefoon", "F0:79:59:72:69:83": "Papas_PC"}

    commando_out = open('command_out.txt')
    command_out = commando_out.readline()

    puts = []
    with open('c_out.txt', 'w+') as c_out:
        subprocess.call(command_out, universal_newlines=True, shell=True, stdout=c_out, stderr=drop)
        cm_out = c_out.readlines()
        ar = []
        for c in adressen:
            for regels in cm_out:
                if c in regels:
                    ar.append(adressen[c.rstrip()])

        commando_out.close()
        c_out.close()
        drop.close()

        if len(ar) > 1:
            log.write('Curl gebruikt        ' + localtime + '\n')
            log.close()
            return render_template('whoishome.html', len=len(ar), puts=ar)
        else:
            log.write("Curl niet gelukt     " + localtime + '\n')


    # Start methode 2, als methode 1 niet lukt

    lijs = open("out.txt")
    know = open("known.txt")


    subprocess.call("sudo arp-scan --interface=wlan0 --localnet --plain | cut -f 2", universal_newlines=True,
                    shell=True, stdout=lijs)

    lijst = lijs.readlines()
    known = know.readlines()

    known_goed = []
    for z in known:
        known_goed.append(z.rstrip())

    for j in lijst:
        plaats = j.rstrip()
        if plaats in known_goed:
            x = known_goed.index(plaats)
            put = known_goed[x + 1].replace("_", " "), "is thuis"
            put = " ".join(put)
            puts.append(put)


    know.close()
    lijs.close()

    if len(puts) > 0:
        log.write('Arpscan gebruikt     ' + localtime + '\n')
        log.close()
        return render_template("whoishome.html", len=len(puts), puts=puts)
    else:
        log.write('Niks gevonden   ' + localtime + '\n')
        log.close()
        return render_template("whoishomef.html", fout="Niks gevonden :(")
