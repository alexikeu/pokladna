#prázdné odstavce
print("")
print("")
print("")

#otázky
vztup = input("Chcete zkusit naš nový internetový systém? 1 = souhlas, 2 = nesouhlas: ")

#int
vztup = int(vztup)

#if
if vztup == 1:
    #prázdný odstavce
    print("")

    #prázdné odstavce
    print("Děkujeme za snahu!")

    #prázdné odstavce
    print("")
    print("")
    print("")

    #ceník
    print("Zde je ceník potrvin:")

    #prázdné odstavce
    print("")

    #ceník
    print("- rohlík   2Kč")
    print("- houska   3Kč")
    print("- čaj      54Kč")
    print("- jogurt   14Kč")
    print("- sýr      25Kč")
    print("- šunka    29Kč")
    print("- jahody   59Kč")
    print("- borůvky  49Kč")
    print("- mléko    18Kč")
    print("- Fanta    32Kč")

    #prázdné odstavce
    print("")
    print("")

    #otázky
    a = input("Počet rohlíků: ")
    b = input("Počet housek: ")
    c = input("Počet čajů: ")
    d = input("Počet jogurtů: ")
    e = input("Počet sýrů: ")
    f = input("Počet šunky: ")
    g = input("Počet jahod: ")
    h = input("Počet borůvek: ")
    i = input("Počet mlék: ")
    j = input("Počet Fant: ")

    #int
    a = int(a)
    b  =int(b)
    c = int(c)
    d = int(d)
    e = int(e)
    f = int(f)
    g = int(g)
    h = int(h)
    i = int(i)
    j = int(j)

    #vypočítávání cen
    k = a*2
    l = b*3
    m = c*54
    n = d*14
    o = e*25
    p = f*29
    q = g*59
    r = h*49
    s = i*18
    t = j*32

    #prázdné odstavce
    print("")
    print("")
    print("")

    #účtenka
    print("Vaše účtenka:")

    #prázdné odstavce
    print("")

    #účtenka
    print("-", a, "rohlík")
    print("-", b, "houska")
    print("-", c, "čaj")
    print("-", d, "jogurt")
    print("-", e, "sýr")
    print("-", f, "šunka")
    print("-", g, "jahody")
    print("-", h, "borůvky")
    print("-", i, "mléko")
    print("-", j, "Fanta")

    #prázdné odstavce
    print("")

    #celková částka
    print("Celková částka vašeho nákupu je", k + l + m + n + o + p + q + r + s + t, "Kč!")

    #prázdné odstavce
    print("")
    print("")

    #otázka
    vstup = input("Jste spokojeni s cenou? 1 = spokojenost, 2 = nespokojenost: ")

    #prázdné odstavce
    print("")

    #int
    vstup = int(vstup)

    #if, elif, else
    if vstup == 1:
        print("To nás těší!")
    elif vstup == 2:
        print("To nás mrzí, proto Vám dáváme slevu 5% na celý nákup!")
    else:
        print("Chyba při zadávání čísla!")
    
    #emote
    print("¯\_(ツ)_/¯")

#elif a else
elif vztup == 2:
       #prázdné odstavce
    print("")
    print("Nejste vhodným zákazníkem!")
else:
    print("")
    print("Špatně zadané číslo, pro opakování zmáčkněte F5!")

#prázdné odstavce
print("")
print("")
print("")