


def deft():
    cosmo = input()
    numberOfcosmo = 0

    cosmos = []

    while cosmo != '!':
        if cosmo == '!':
            break
        cosmo = input()
        if cosmo != '!':
            if int(cosmo) > 160 and int(cosmo) < 180:
                numberOfcosmo = numberOfcosmo + 1
                cosmos.append(int(cosmo))

    print(max(cosmos))
    print(min(cosmos))
    print(numberOfcosmo)


deft()
