from bank_account.jugend_account import JugendBankAccount

def main():
    # Testen des JugendBankAccounts
    jugend_konto = JugendBankAccount("Max Mustermann Junior", "50")
    print(jugend_konto)
    jugend_konto.einzahlen(100)

    try:
        jugend_konto.abheben(30)
    except ValueError as e:
        print(e)

    try:
        jugend_konto.abheben(20)
    except ValueError as e:
        print(e)

    print(jugend_konto.get_kontostand())


if __name__ == "__main__":
    main()