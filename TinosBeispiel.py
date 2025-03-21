# Dieses "Skript" hier dient lediglich Dokumentationszwecken. Daher enthält es nur Kommentare.
#
# Konzept hinter dem Testing in Python
# ====================================
#
# Mit Tests kann geprüft werden, ob Funktionen das tun, was sie tun sollen. Dazu werden
# Testfälle defininiert, die sich in speziellen Python-Skripten im Ordner
# "tests" befinden müssen. Als "Engine" wird hier das Python-Package "pytest"
# verwendet, das ggf. erst noch installiert werden muss. Testfälle werden dann
# in dedizierten Python-Dateien definiert und mittels pytest ausgeführt. Pytest
# zeigt dann die Ergebnisse an. Anmerkung in eigener Sache: es scheint zweckmäßig
# zu sein, für die Testumgebung eine dedizierte virtuelle Python-Umgebung einzurichten.
#
# 
# Aufsetzen der Testumgebung
# ==========================
# 
# Am besten eine virtuelle Python-Umgebung anlegen, in der die benötigten Python-
# Packages (z.B. "pytest") angezogen werden und die auch sicherstellt, dass eine
# bestimmte Python-Version genutzt wird für die Tests. Dazu folgendermaßen vorgehen:
# 
# Schritt 1: Virtuelle Python-Umgebung einrichten
# 
#   Im Beispiel hat sich gezeigt, dass Python 3.13.0 funktioniert. Daher sollte
#   die virtuelle Umgebung so eingerichtet werden, dass dann auch diese Version
#   genutzt wird, egal, welche Version nativ in VS Code angezogen wird. Dazu muss
#   Python 3.13.0 auf dem Rechner installiert sein (neben ggf. anderen Versionen!).
#   Hier im Beispiel ist sie installiert im Ordner "C:\Program Files\Python313".
#   Die virtuelle Umgebung wird folgendermaßen eingerichtet (Windows Powershell 
#   Kommando in diesem Bsp. hier):
# 
#    C:\"Program Files"\Python313\python -m venv .vPy313Env_Testing
# 
# Schritt 2: Virtuelle Python-Umgebung aktivieren für die Nutzung
#
#   Nun die virtuelle Python-Umgebung aktivieren mittels:
#
#   .\.vPy313Env_Testing\Scripts\activate
#
# Schritt 3: Projekt (inkl. "pytest") installieren
#
#   Nun das Projekt installieren, d.h. benötigten Packages laden mit der "pyproject.toml":
#
#   pip install .
#
# Fertig :). Python 3.13.0 sollte nun aktiv sein, und auch das Package "pytest" sollte
# nun zur Verfügung stehen.
#
#
# Definition von Testfällen
# =========================
#
# Testfälle müssen immer in einem Ordner "tests" abgelegt sein. Sie werden in dedizierten
# Funktionen definiert, die wiederum in Python-Files beginnend mit "test_" stehen müssen.
# Hier im Beispiel sind dies die Dateien "tests\test_einfach.py" und "tests\test_rechenoperationen.py".
# Dort werden folgende Konstrukte zum Abfragen der Testergebnisse genutzt:
#
# a) Abfragen eines korrekten numerischen Erebnisses:
#   
#       Dies geschieht mittels der "assert"-Anweisungen
#
# b) Testen, ob eine bestimmte Exception geworfen wird:
#
#       Dies geschieht mittels der "with ..." - Anweisung
#
#
# Ausführen der Tests
# ===================
#
# Im Visual Studio Code gibt es links ein Erlenmeierkolbensymbol für den Bereich "Testing".
# Wenn "pytest" korrekt installiert wurde und die Testfälle definiert wurden, werden
# diese Testfälle dort angezeigt und können ausgeführt werden. Die Ergebnisse (bestanden
# oder nicht bestanden) werden farblich angezeigt. Details zu Ergebnissen werden durch
# "pytest" direkt in den Testdateien angezeigt.