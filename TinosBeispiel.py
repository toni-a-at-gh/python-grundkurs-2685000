# Projektstrukturen 
# ****************** 
#
# Dieses Python-Skript hier ist an sich keine Skript wie in den anderen 
# Branches zuvor, sondern ist eher als Notiz zur Erläuterung der bereits erstellten
# Projektstruktur gedacht!
#
# Terminologie:
# ============
#
# 'Ordner':
# ---------
# Das sind die Ordner im Projekt. Sie können u.U. Packages sein.
#
# 'Packages':
# -----------
# Das sind diejenigen Ordner, die mit einer "__init.py__" versehen sind. Python erkennt 
# Packages anhand der Existenz dieser Datei! Es erwartet dann im gleichen Ordner Python-
# Code. Packages können weitere Packages enthalten. Die Package-Struktur in diesem Beispiel
# sieht folgendermaßen aus:
#
# src (P)
# |
#  -- python_grund_kurs (P)
#     |
#      -- utils (P)
# 
# 'Module':
# ---------
# Das sind diejenigen .py Dateien, die tatsächlich Code enthalten (z.B. Klassendefinitionen oder
# Funktionsdefinitionen) und die auf der gleichen Ordnerebene liegen wie die "__init.py__", die
# somit zum selben Package gehören.
#
# 'Scripts':
# ----------
# Das sind diejenigen .py Dateien, die die "main"-Funktion enthalten sollten.
# Dazu ist darin definiert:
#
# a)
#   def main():
#   ... die Codezeilen des Skripts
#
# b)
# if __name__ == "__main__":
#     main()
#
# a) Das ist die Definition der Hauptfunktion, die aufgerufen wird bei Aufruf des Skripts
# b) Daran erkennt Python, dass in der .py Datei eine Hauptfunktion definiert ist
#
#
# Import-Syntax:
# ==============
#
# In Modulen und Skripten können Codezeilen nach folgendem Muster auftauchen:
#
#   from <Package>.<Modul> import <Klasse | Funktion>
#
# Beispiele:
# 
#   "from python_grund_kurs.kategorien import KategorieManager"
#   --> importiert aus dem Package "python_grund_kurs" und dem darin befindlichen Modul "kategorien"
#       die KLASSE "KategorieManager"
#
#   "from python_grund_kurs.utils.sortieren import sortiere_nach_prio"
#   --> importiert aus dem Package "python_grund_kurs", dessen Unterpackage "utils" das darin befind-
#       liche Modul "sortieren" die darin befindliche FUNKTION "sortiere_nach_prio"
#
#
# Versionsbezeichner:
# ===================
#
# Packages haben Versionen. Format: a.b.c
#
#   a: Major Inkrement
#   b: Mino Inkrement
#   c: Patch
#
# Beispiel: 1.0.1