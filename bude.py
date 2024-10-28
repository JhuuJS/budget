
Vuokra = int(input("Paljon rahaa vuokraan kuussa?"))
Vakuutukset = int(input("Paljon rahaa vakuutuksiin kuussa?"))
Kouluruokailu = int(input("Paljon rahaa kouluruokailuun kuussa?"))
Sahko = int(input("Paljon rahaa sähköön kuussa="))
Liikkuminen = int(input("Paljon rahaa liikkumiseen kuussa?"))
Muut = int(input("Muita kuukausittaisia menoja?"))
menot = Vuokra + Vakuutukset + Kouluruokailu + Sahko + Liikkuminen
print("Kuukausi menosi ovat", menot)