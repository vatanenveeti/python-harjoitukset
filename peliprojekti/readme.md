# Sakari ja kadonnut villapaita
**Veeti Vatanen**


## Pelin idea ja tavoite

Sakari ja kadonnut villapaita -pelissä tavoite on etsiä sakarin kadonnut villapaita. Tarina sai vahvasti inspiraatiota Sakarin villapaita -pelistä. Peli on yksinkertainen tekstiseikkailupeli, jossa edetään "huoneittain" eteenpäin. Pelaaja saa valita kahdesta vaihtoehdosta, miten Sakari etenee pelissä. Pelin voi voittaa ainoastaan löytämällä villapaidan. Pelillä on 8 eri lopputulemaa, joista vain yhdellä voittaa.

## Toimintaperiaatteet ja toiminnallisuudet

Peli käynnistetään ajamalla main-tiedosto. Pelin tekstit on tallennettu teksti-tiedostoihin. Main-tiedoston lisäksi pelillä on peli, pelaaja ja maailma -tiedostot. Pelissä tallenetut tiedostot kirjoitetaan json-tiedostoon. Json-tiedostoon tallennetaan vain pelaajan nimi ja sijainti sekä sillä on tieto siitä, onko edellistä tallennusta vai ei.

Main tiedosto alustaa tallennustiedoston, kysyy pelaajan nimen ja iän sekä aloittaa itse pelin luomalla Peli-olion. Se voi myös sulkea pelin, jos pelaaja on alle 12v. Peli-olio on koko pelin ydin. Se luo Maailma-olion ja Pelaaja-olion. Peli luo terminaaliin kaikki valikot, lataa ja tallentaa pelin sekä aloittaa pelin. 

Itse peli toimii yksinkertaisella silmukalla, jonka luo pelin_kierto()-funktio. Funktio tarkistaa aina onko pelitilanne “läpi”. Jos pelitilanne on “kesken”, se suorittaa käynnistä_alue()-funktion. Käynnistä_alue()-funktio esittelee pelin alueen/tilanteen ja antaa mahdollisuuden valita seuraavan alueen. Alueet ovat omia olioita, jotka on luodaan maailma-tiedostossa. Niille on määritelty omat nimet, esittelytekstit, onko viimeinen alue ja seuraavat alueet. Kaikki esittelytekstit on tallennettu samaan tekstitiedostoon. Kun päästään alueelle, joka on viimeinen alue, peli päättyy ja ohjelma sulkeutuu. Pelaaja-olio tallentaa vain nimen ja sijainnin sekä sen ainoa funktio on vaihtaa sijaintia. Maaailma-olio luo pelin maailman, alueet ja yhdistää alueet alueiden määrittele_alueet()-funktion avulla. 

## Kestävä kehitys pelissä

Kestävä kehitys on otettu melko huonosti huomioon pelissä, koska tajusin aika myöhään, että sen näkökulma on otettava huomioon. Pelissä otetaan huomioon ainoastaan Vastuullista kuluttamista -osa-alue, joka näkyy vain siten, että Sakari ei halua hukata villapaitaa vaan säilyttää sen.

## Kehitettävää

Pelissä on mielestäni paljon kehitettävää, sillä se on todella yksinkertainen ja sisällöltään ei kovin kummoinen. Toisaalta se sopii “Sakarin villapaita” -teemaan. Jos minulla olisi ollut enemmän aikaa tehdä peliä, olisin halunnut tehdä alueihin erillaisia toimintoja ja mahdollisesti jonkin taistelumekaniikan. Nyt siinä vain yksinkertaisesti edetään alueesta alueeseen. Pelisilmukka ja alueet olivat myös luotu siten, että niihin on melko vaikea lisätä muuta sisältöä ellei halua muokata koodia merkittävästi.
