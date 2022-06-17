"""
Ildledning for Observatør OP.
Beregner justering fra sin posisjon.
Kanon må vite OP-posisjon og sin egen posisjon.

"""
#Første angivelse av mål.
retning = int(input("Angi retning:"))
avstand = int(input("Angi avstand:"))
print("Her kommer treffet som korrigeres.")

#Beregning av korreksjon som sendes til kanon.
retningAvvik =int(input("Angi sideveis avvik:"))
avstandTreff = int(input("Angi avstand til nedslag:"))

retningKorr = -retningAvvik
avstandKorr = avstand - avstandTreff

print("Korriger ",retningKorr," grader og ",avstandKorr," i avstand") 

