# main.py

from flask import Blueprint, render_template
from flask_login import login_required, current_user
import subprocess

main = Blueprint('main', __name__)

@main.route('/')
@login_required
def index():
    return render_template('profile.html', name=current_user.name)


@main.route('/whoishome')
@login_required
def whoishome():
    puts = []
    with open('out.txt', 'w+') as op:
        with open('err.txt', 'w+') as err:
            z = "ping -b 192.168.0.255 -c 5 -q"
            subprocess.call(z, universal_newlines=True, shell=True)
            a = "sudo arp-scan --interface=eth0 --localnet --plain | cut -f 2"  # Command to insert in promt
            subprocess.call(a, universal_newlines=True, shell=True, stdout=op,
                            stderr=err)  # Inserts command at promt with output in out.txt and errors in err.txt

    lijst = open("out.txt").readlines()  # Makes list of items in out.txt

    known = open("known.txt").readlines()  # Read lines at known mac adresses
    known_goed = []

    for z in known:
        known_goed.append(z.rstrip())

    for j in lijst:
        plaats = j.rstrip()
        if plaats in known_goed:
            x = known_goed.index(plaats)
            put = known_goed[x], "van", known_goed[x + 1].replace("_", " "), "is verbonden met het netwerk"
            put = " ".join(put)
            puts.append(put)

    if len(puts) > 0:
        return render_template("whoishome.html", len=len(puts), puts=puts)
    else:
        return render_template("whoishomef.html", fout="Niks gevonden :(")
