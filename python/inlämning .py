from tkinter import N

#antal pengar per person
pelle = 25
lisa = 25
josef = 25
sarah = 25

alla4 = pelle+lisa+josef+sarah
# värde på varje frukt
banan = 10
äpple = 20
apelsin = 15
kiwi = 10
varukorgen = 2*äpple + 3*banan + apelsin 
pengar_kvar = alla4 - varukorgen 

#1 (

print ("Alla 4 går in på en mataffär och lägger 2 äpplen, 3 bananer och 1 apelsin i varukorgen",
    "som totalt kostar 85kr , då har de 15kr kvar som sen kan gå tillbaka och köpa en Kiwi.",
    
    " Sen har de ", alla4 - 2*äpple - 3*banan - apelsin - kiwi ,"kr kvar."
)

print( 
    
    "Gruppen skulle behöva", apelsin*2123 - pengar_kvar ," mer för att kunna köpa 2123 apelsiner "

)


#2
#skyldighet
pelle_lisa = 3
sarah_josef = 1
pelle_sarah= 4
lisa_josef = 4
josef_pelle = 4 

gruppen_skyldiga = pelle_lisa + sarah_josef + pelle_sarah + lisa_josef + josef_pelle 

#stats
pelle_lisa2  = pelle-3, lisa+3
sarah_josef2 = sarah-1, josef+1
pelle_sarah2 = pelle-4, sarah+4
lisa_josef2 = lisa-4, josef+4
josef_pelle2 = josef-4, pelle +4

#pengar efter skyldighet 
pengar_kvar2 = pengar_kvar / 4
sarah_ad = pengar_kvar2 +3
pelle_ad = pengar_kvar2 -3
lisa_ad = pengar_kvar2 -1
josef_ad = pengar_kvar2 +1



print(
"De är skyldiga ", gruppen_skyldiga,"kr.", " Pelle var skyldig mest pengar, han var skyldig 7kr totalt.",
" Sarah har mest pengar, hon har 6.75kr."

)
#så mycket pengar har varje person
print(
    "Sarah har :", sarah_ad,"kr." "\n"
    "Pelle har :", pelle_ad ,"kr." "\n"
    "Lisa har :", lisa_ad,"kr." "\n"
    "Josef har :", josef_ad,"kr."
)

#3

Lamborghini_Huracán_Evo = 2849900
broke_kids = Lamborghini_Huracán_Evo - pengar_kvar

print(
" Senare tänkte gruppen gå ock köpa en Lamborghini Huracán Evo som kostar", Lamborghini_Huracán_Evo, "kr." "\n"
" När de gick där så hade de inte tillräckligt mycket, då behövde de", broke_kids, "kr."
" Då gick de tillbaka till matafärren ledsna och köpte en kiwi som kostade", kiwi, "kr."
" Sen åkte de till Auschwitz och kom aldrig tillbaks."
)
