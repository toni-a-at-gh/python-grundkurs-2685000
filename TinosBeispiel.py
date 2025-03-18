# Dieses "Skript" hier dient lediglich Dokumentationszwecken. Daher enthält es nur Kommentare.
#
# Konzept hinter dem Testing in Python
# ====================================
#
# Es soll geprüft werden, ob Funktionen das tun, was sie tun sollen. Dazu werden
# Testfälle defininiert, die sich in speziellen Python-Skripten im Ordner
# "tests" befinden müssen. Als "Engine" wird hier das Python-Package "pytest"
# verwendet, das ggf. erst noch installiert werden muss. Dazu "pip install pytest"
# ausführen.
#
#
# Definition von Testfällen
# =========================
#
# Testfälle müssen immer in einem Ordner "tests" abgelegt sein. 