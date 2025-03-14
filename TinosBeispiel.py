# HINWEIS:
# Dieses Python-"Skript" hier dient wieder nur als "Mitschrift" zum Thema des Branches
# "Setup.py benutzen". Die Notizen aus dem Branch "05_02-Projektstruktur" wurden hierher
# kopiert und fortgesetzt. Damit ist eine zusammenhängende Mitschrift zu den Themen "Projekt-
# struktur" und dazugehörigen Themen sichergestellt.


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
#   b: Minor Inkrement
#   c: Patch
#
# Beispiel: 1.0.1
#
#
# Was ist ein "Python-Projekt"?
# =============================
#
# Antwort on Microsoft Copilot:
#
# Ein "Python-Projekt" ist eine Sammlung von Python-Dateien und Ressourcen, die zusammenarbeiten, 
# um eine bestimmte Anwendung oder ein bestimmtes Modul zu erstellen. Hier sind einige wichtige 
# Aspekte eines Python-Projekts:
# 
#   Code-Dateien: 
#   Die Hauptbestandteile eines Python-Projekts sind die Python-Skripte (.py-Dateien), 
#   die den eigentlichen Code enthalten.
#
#   Verzeichnisstruktur: 
#   Ein gut organisiertes Projekt hat eine klare Verzeichnisstruktur, z.B. ein src-Verzeichnis für 
#   den Quellcode, ein tests-Verzeichnis für Testfälle und ein docs-Verzeichnis für Dokumentation.
#
#   Abhängigkeiten: 
#   Ein Projekt kann externe Bibliotheken und Module verwenden, die in einer requirements.txt-Datei 
#   oder pyproject.toml-Datei aufgelistet sind.
#
#   Konfigurationsdateien: 
#   Dateien wie setup.py oder pyproject.toml enthalten Metadaten und Konfigurationsinformationen 
#   für die Paketierung und Verteilung des Projekts.
#
#   Dokumentation: 
#   Eine gute Dokumentation, oft in Form von README.md-Dateien, beschreibt das Projekt, wie man es 
#   installiert und verwendet.
#
#   Tests: 
#   Testfälle und Testskripte sind wichtig, um sicherzustellen, dass der Code korrekt funktioniert. 
#   Diese befinden sich oft in einem tests-Verzeichnis.
#
# Anmerkung dazu: 
# Ein Projekt wird über diese Konfigurationsdateien "setup.py" bzw. "pyproject.toml" konfiguriert.
#
#
# Projekt konfigurieren mittels 'setup.py':
# =========================================
#
# Ein Python-Projekt wird über verschiedene Eigenschaften eindeutig charakterisiert/definiert/konfiguriert.
# Zur Konfiguration eines Python-Projekts gehören u.a. dazu:
# 
#   a) Abhängigkeiten zu anderen Packages, Modulen und Funktionen
#   b) Name des Projekts
#   c) Vergebene Versionsnummer des Projekts
#   d) Informationen zum Autor des Projekts (Name, Email ...)
#   e) Beschreibung des Projekts
#   f) Packages, die zum Projekt gehören
#   g) Lizenzinformationen
#   h) Benötigte Python-Version
#   
# Im Beispiel der 'setup.py' in diesem Branch hier werden die genannten Informationen über folgende Codezeilen 
# definiert:
#
#   zu a): 
#   Diejenigen Packages (Name und Versionsnummer), von denen das eigene Projekt abhängig ist, sind in der
#   Datei "requirements.txt" definiert. Der folgende Code liest diese Datei ein und erstellt eine Liste daraus:
#
#       with open('requirements.txt') as f:
#       requirements = f.read().splitlines()
#
#   Über die Funktion setup() wird danach diese Liste in das Setup des Projekt übernommen. Siehe diese Codezeile:
#
#       install_requires=requirements,
#
#   zu b):
#   Über die Funktion setup() wird u.a. die vergebene Versionsnummer für das Python-Projekt festgelegt in dieser Codezeile:
#
#       version='1.0.0',
#
#   zu c):
#   Über die Funktion setup() wird u.a. der Name des Projekts festgelegt in dieser Codezeile:
#
#       name='python_grund_kurs',
#
#   zu d):
#   Über die Funktion setup() werden u.a. auch die Informationen zum Autor des Projekts festgelegt in diesen Codezeilen:
#
#       author='Julia Imlauer',
#       author_email='info@linkedinlearning.com',
#
#   zu e):
#   Über die Funktion setup() wird u.a. die Beschreibung des Projekts festgelegt in diese Codezeilen:
#
#       long_description=open('README.md').read(),
#       long_description_content_type='text/markdown',
#
#   zu f):
#   Über die Funktion setup() werden u.a die Packages, die zum Projekt gehören, in diesen Codezeilen definiert:
#
#       package_dir={'': 'src'},
#       packages=find_packages(where='src'),
#
#   zu g):
#   Über die Funktion setup() werden u.a. Lizenzinformationen zum Projekt festgelegt in diese Codezeilen:
#
#       license_files=('LICENSE',),
#       license='LinkedIn Learning Exercise Files License',
#
#   zu h):
#   Über die Funktion setup() wird u.a. auch die Python-Version, die das Projekt benötigt, festgelegt in dieser Codezeile:
#
#       python_requires='>=3.6',  # Specify Python version requirement
#
#
# Was ist ein "Python Environment"?
# =================================
#