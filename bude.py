def __intit__(self):
    self.Vuokra = 0
    self.Vakuutukset = 0
    self.Kouluruokailu = 0
    self.Sahko = 0
    self.Liikkuminen = 0
    self.Muut = 0


def save(item):
    saved = item
    return saved



while True:
    Vuokra = int(input("Paljon rahaa vuokraan kuussa?"))
    Vakuutukset = int(input("Paljon rahaa vakuutuksiin kuussa?"))
    Kouluruokailu = int(input("Paljon rahaa kouluruokailuun kuussa?"))
    Sahko = int(input("Paljon rahaa sähköön kuussa="))
    Liikkuminen = int(input("Paljon rahaa liikkumiseen kuussa?"))
    Muut = int(input("Muita kuukausittaisia menoja?"))
    menot = Vuokra + Vakuutukset + Kouluruokailu + Sahko + Liikkuminen
    print(menot)
    choice = input("'edit' tai 'copy' tai ")