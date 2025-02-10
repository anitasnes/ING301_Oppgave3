from pathlib import Path
import sys


# Dette er start-koden til den første programmeringsoppgave i ING 301
#
# Du skal utvikle et programm som finner det hyppigste ordet i en gitt tekstfil.
# Dette høres kanskje litt komplisiert ut, men fortvil ikke!
# Vi har forberedt den grove strukturen allerede. Din oppgave er å implementere
# noen enkelte funskjoner som trengs for det hele til å virke.
# Enhver funksjon kommer med en dokumentasjon som forklarer hva skal gjøres.


def read_file(file_name):
    """
    Denne funksjonen får et filnavn som argument og skal gi
    tilbake en liste av tekststrenger som representerer linjene i filen.
    """
    file = open(file_name,  encoding="utf-8")
    innhold = file.read()
    linjer = innhold.split("\n")
    
    linjer = [linje for linje in linjer if linje.strip()]
    
    # Tips: kanksje "open"-funksjonen kunne være nyttig her: https://docs.python.org/3/library/functions.html#open
    return linjer  


def lines_to_words(lines):
    """
    Denne funksjonen får en liste med strenger som input (dvs. linjene av tekstfilen som har nettopp blitt lest inn)
    og deler linjene opp i enkelte ord. Enhver linje blir delt opp der det er blanktegn (= whitespaces).
    Desto videre er vi bare interessert i faktiske ord, dvs. alle punktum (.), kolon (:), semikolon (;),
    kommaer (,), spørsmåls- (?) og utråbstegn (!) skal fjernes underveis.
    Til sist skal alle ord i den resulterende listen være skrevet i små bokstav slik at "Odin" og "odin"
    blir behandlet likt.
    OBS! Pass også på at du ikke legger til tomme ord (dvs. "" eller '' skal ikke være med) i resultatlisten!

    F. eks: Inn: ["Det er", "bare", "noen få ord"], Ut: ["Det", "er", "bare", "noen", "få", "ord"]
    """
    # Tips: se på "split()"-funksjonen https://docs.python.org/3/library/stdtypes.html#str.split
    # i tillegg kan "strip()": https://docs.python.org/3/library/stdtypes.html#str.strip
    words = []
    for linje in lines:
        # Split the line into words
        line_words = linje.split(" ")

        # Loop over each word in the line
        for word in line_words:
            # Remove punctuation and convert to lowercase
            word = word.strip(".:;,?!- ")
            word = word.lower()
            # Add the word to the words list
            if word:
                words.append(word)
             
    # og "lower()": https://docs.python.org/3/library/stdtypes.html#str.lower være nyttig
    return words


def compute_frequency(words):
    """
    Denne funksjonen tar inn en liste med ord og så lager den en frekvenstabell ut av den. En frekvenstabell
    teller hvor ofte hvert ord dykket opp i den opprinnelige input listen. Frekvenstabllen
    blir realisert gjennom Python dictionaires: https://docs.python.org/3/library/stdtypes.html#mapping-types-dict

    F. eks. Inn ["hun", "hen", "han", "hen"], Ut: {"hen": 2, "hun": 1, "han": 1}
    """
    frequency = {}  # Initialiser dictionaryen for å lagre frekvenser
    for word in words:
        # Hvis ordet allerede finnes i dictionaryen, øk verdien med 1
        if word in frequency:
            frequency[word] += 1
        # Hvis ordet ikke finnes, legg det til med verdien 1
        else:
            frequency[word] = 1
    return frequency


FILL_WORDS = ['og', 'dei', 'i', 'eg', 'som', 'det', 'han', 'til', 'skal', 'på', 'for', 'då', 'ikkje', 'var', 'vera']


def remove_filler_words(frequency_table):
    """
    Ofte inneholder tekst koblingsord som "og", "eller", "jeg", "da". Disse er ikke så spennende når man vil
    analysere innholdet til en tekst. Derfor vil vi gjerne fjerne dem fra vår frekvenstabell.
    Vi har gitt deg en liste med slike koblingsord i variablen FILL_WORDS ovenfor.
    Målet med denne funksjonen er at den skal få en frekvenstabll som input og så fjerne alle fyll-ord
    som finnes i FILL_WORDS.
    """
    frequency_table2 = frequency_table.copy();
    for word in frequency_table:
        if word in FILL_WORDS:
            del frequency_table2[word]
    return frequency_table2 


def largest_pair(par_1, par_2):
    """
    Denne funksjonen får som input to tupler/par (https://docs.python.org/3/library/stdtypes.html#tuple) der den
    første komponenten er en string (et ord) og den andre komponenten er en integer (heltall).
    Denne funksjonen skal sammenligne heltalls-komponenten i begge par og så gi tilbake det paret der
    tallet er størst.
    """
    # OBS: Tenk også på situasjonen når to tall er lik! Vurder hvordan du vil handtere denne situasjonen
    # kanskje du vil skrive noen flere test metoder ?!
    if par_1 >= par_2:
        return par_1
    else:
        return par_2


def find_most_frequent(frequency_table):
    """
    Nå er det på tide å sette sammen alle bitene du har laget.
    Den funksjonen får frekvenstabllen som innputt og finner det ordet som dykket opp flest.
    """
    # Tips: se på "dict.items()" funksjonen (https://docs.python.org/3/library/stdtypes.html#dict.items)
    # og kanskje du kan gjenbruke den "largest_pair" metoden som du nettopp har laget
    max_word = ""
    max_count = 0

    # Iterer gjennom dictionaryen
    for word, count in frequency_table.items():
        
        if largest_pair(max_count, count) == count:
            max_word = word
            max_count = count

    return max_word


#############################################################
#                                                           #
# Her slutter den delen av filen som er relevant for deg ;-)#
#                                                           #
#############################################################


def main():
    if len(sys.argv) > 1 and Path(sys.argv[1]).exists():
        file = sys.argv[1]
    else:
        file = str(Path(__file__).parent.absolute()) + "/voluspaa.txt"
    lines = read_file(file)
    words = lines_to_words(lines)
    table = compute_frequency(words)
    table = remove_filler_words(table)
    most_frequent = find_most_frequent(table)
    print(f"The most frequent word in {file} is '{most_frequent}'")


if __name__ == '__main__':
    main()
