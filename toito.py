data = [1,8,345,765,123,54,34,76,34]

def bubble_sort(lista):
    for i in range(0, len(lista)): #przejście przez wszystkie indeksy listy
        flag = False #ustawienie flagi sprawdzającej, czy zaszła zamiana na False
        for j in range(0, len(lista) - i - 1): #przejście przez wszystkie elementy, które mogły jeszcze nie zostać posortowane (po każdej iteracji rośnie liczba elementów posortowanych na końcu)
            if lista[j] > lista[j + 1]: #sprawdzenie czy obecny element jest większy od następnego
                lista[j], lista[j + 1] = lista[j + 1], lista[j] #jeżeli obecny element jest większy od następnego to zamień je miejscami
                flag = True #ustaw flagę sprawdzającą na True
        if flag == False: #sprawdzenie czy flaga sprawdzająca jest równa False
            break #jeżeli nie zaszla żadna zamiana (flaga jest na False), to przerwij wykonywanie pętli, w celu oszczędzenia czasu
    return lista

print(bubble_sort(data))




def selection_sort(lista):
    flag = False
    for unordered_element in range(len(lista)): #pętla for dla wartości od 0 do ostatniego elementu listy
        min = unordered_element #min oznacza element, który nie został jeszcze posrtowany

        for element in range(unordered_element + 1, len(lista)): #pętla wywoła się dla wszystkich elementów nieuporządkowanych oprócz tego, który zostanie sprawdzony
            if lista[min] > lista[element]: #sprawdzenie czy element z najmniejszą wartością jest większy od obecnego elementu
                min = element #jeżeli jest to obecny element staje się minimalnym
                flag = True #zaktualizowanie flagi, żeby wskazać, że w tej iteracji będzie zamiana
        if flag == True: #sprawdzenie flagi, jeżeli flaga jest prawdziwa to sprawdzany nieuporządkowany element zamienia się miejscem z najmniejszym elementem
            lista[unordered_element], lista[min] = lista[min], lista[unordered_element] #zamiana elementów
            flag = False #zmiana flagi znowu na 0
    return lista

lista = [8,5,4,1,3,9,10] #lista, która zostanie posortowana

print(selection_sort(lista))




def insertionSort(lista):
    for i in range(1, len(lista)): #zaczynamy od 1, ponieważ pierwszy (zerowy) element uznajemy za posortowany
        key = lista[i] #wartość klucza przyjmuje element, który będziemy w danej iteracji sortować

        j = i - 1 #j wyznacza pierwszy indeks posortowanej części listy
        while j >= 0 and key < lista[j]: #wykonujemy pętlę dopóki są jeszcze jakieś elementy w posorotwanej części listy lub dopóki wartość w posortowanej tablicy nie okaże się mniejsza
            lista[j + 1] = lista[j] #zgodnie z przechodzeniem pętli po liście przesuwamy elementy
            j -= 1 #przejście do następnego elementu
        lista[j + 1] = key #po zakończeniu pętli klucz trafia w miejsce ostatniego elementu spełniającego warunek z pętli while
    return lista    

lista = [5,4,3,2,1,7,3,4,11,234]

print(insertionSort(lista))




def mergeSort(lista):
    if len(lista) > 1: #jeżeli lista ma długość równą 1, to nie da się jej bardziej podzielić
        mid = len(lista) // 2 #znalezienie środka listy poprzez podzielenie długośi listy przez dwa i zaokrąglenie w dół

        left = lista[:mid] #lewa strona, to lista do środkowego elementu
        right = lista[mid:] #prawa strona, to lista od środkowego elementu

        mergeSort(left) #wywołanie funkcji ponownie dla lewej strony
        mergeSort(right) #wywołanie funkcji ponownie dla prawej strony

        i = j = k = 0 #wartości pomocniczne służące do przeszukiwania poszczególnych elementów tablic
        while i < len(left) and j < len(right): #wykonujemy pętlę dopóki znajdują się elementy zarówno po lewej i prawej stronie
            if left[i] <= right[j]: #jeżeli element z lewej strony jest mniejszy lub równy prawemu, to powinien trafić w obecny element sortowanej listy
                lista[k] = left[i] #jeżeli spełniony został warunek, to obecny element z lewej strony trafia na miejsce sortowanej listy.
                i += 1 #przejście o jeden indeks do przodu dla lewej strony
            else:
                lista[k] = right[j] #jeżeli warunek nie został spełniony, to element z listy prawej trafia w obecny element sortowanej listy
                j += 1 #przejście o jeden indeks do przodu dla prawej strony
            k += 1 #przejście o jeden indeks do przodu dla sortowanej listy
        
        while i < len(left): #pętla dodająca do sortowanej listy pozostałe elementy z lewej strony
            lista[k] = left[i]
            i += 1
            k += 1 
        
        while j < len(right): #pętla dodająca do sortowanej listy pozostałe element z prawej strony
            lista[k] = right[j]
            j += 1
            k += 1
    # print(lista)

    lista = [5,4,3,2,1,10,15,11,13,14,18,19,20,23,26,27]
mergeSort(lista)
print(lista)





def linearSearch(lista, last_element, searched_value):
    return_value = False #wartość boolowska, która zostanie zwrócona przez funkcję
    for i in range(0, last_element): #przeszukanie wszystkich elementów listy
        if lista[i] == searched_value: #sprawdzenie czy obecny element jest równy szukanemu elementowi
            return_value = True #jeżeli jest to wartość zmiennej przechodzi na True
    return return_value #zwrócenie True lub False w zależności od rezultatu
lista = [1,23,13,2,321,321,21,321,21,4,2,345,32,53,534,5,436,436,43,643,643643,5,23,5432,32,432,4,234,1,312,321]

linearSearch(lista, len(lista), 21)





def sentinelSearch(lista, list_len, key): #funkcja przyjmuje 3 argumenty, listę, długość listy 
    is_found = False #zainicjalizowanie flagi czy znaleziono wartość
    last = lista[list_len - 1] #przechowanie w pamięci ostatniego elementu listy

    lista[list_len - 1] = key #zamiana ostatniego elementu listy na wartość wyszukiwaną
    i = 0 #ustawienie zmiennej do przechodzenia przez kolejne indeksy na 0 (pierwszy element listy) 
    while (lista[i] != key): #przechodzenie przez poszczególne elementy listy dopóki nie zostanie znaleziona wartość wyszukiwana
        i += 1 #zwiększenie zmiennej i o 1 

    lista[list_len - 1] = last #powrót ostatniego elementu listy na swoje miejsce
    #warunek sprawdzający czy wartość występuje w liście. Jeżeli i jest mniejsze od długości listy, to znaczy, że pętla przerwała się przed końcem, a to oznacza znalezienie elemenetu
    if ((i < list_len - 1) or (lista[list_len - 1] == key)): #drugi warunek to sprawdzenie czy ostatni element listy to poszukiwana wartość
        is_found = True #zmiana flagi czy znaleziono wartość na True
    return is_found #zwrócenie flagi 

lista = [1,2,3,4,5,6,7,8,10,11,9,100,50,40,30,75]
list_len = len(lista)
key = 20
print(sentinelSearch(lista, list_len, key))






from math import sqrt, floor

def jump_search(lista, value):
    length = len(lista)
    jump = floor(sqrt(length))
    previous_step = 0

    while lista[min(jump, length - 1)] < value:
        previous_step = jump
        jump += floor(sqrt(length))
        if previous_step > length:
            return None
    for i in range(previous_step, min(jump, length) + 1):
        if lista[i] == value:
            return i
    return None

lista=[1,2,3,4,4,5,5,6,7,8,9,10,11]

print(jump_search(lista, 4))





def binarySearch(lista, searched_value):
    left = 0 #ustawienie wartości lewej strony na 0
    right = len(lista) - 1 #ustawienie wartości prawej strony na ostatni indeks listy
    if lista[left] == searched_value or lista[right] == searched_value: #sprawdzenie czy minimalna lub maksymalna wartość jest równa poszukiwanej wartości
        return True
    
    if lista[left] > searched_value or lista[right] < searched_value: #sprawdzenie czy poszukiwana wartość może znajdować się w zbiorze
        return False

    while left <= right: #wykonywanie pętli dopóki możliwe jest dalsze dzielenie

        mid = left + (right - left)//2 #znalezienie środkowego elementu

        if lista[mid] == searched_value: #jeżeli środkowy element jest równy poszukiwanej wartości, zwróć True
            return True

        elif lista[mid] < searched_value: #jeżeli środkowy element jest mniejszy od poszukiwanej wartości, to przyjmij środek + 1 jako lewą stronę
            left = mid + 1

        else:
            right = mid - 1 #jeżeli środkowy element jest większy od poszukiwanej wartości, to przyjmij środek - 1 jako prawą stronę

    return False #zwróć False, jeżeli wartości nie ma w liście

lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]

for i in lista:
    print(binarySearch(lista, i))
#binarySearch(lista, 7)






def ternarySearch(lista, searched_value):
    left = 0
    right = len(lista) - 1

    if lista[left] == searched_value or lista[right] == searched_value: #sprawdzenie czy minimalna lub maksymalna wartość jest równa poszukiwanej wartości
        return True
    
    if lista[left] > searched_value or lista[right] < searched_value: #sprawdzenie czy poszukiwana wartość może znajdować się w zbiorze
        return False

    while left <= right:

        mid1 = left + (right-left) // 3
        mid2 = right - (right-left) // 3
        #print(lista[mid1:mid2+1])

        if searched_value == lista[mid1]:
            return True
        
        if searched_value == lista[mid2]:
            return True
        
        if searched_value < lista[mid1]:
            right = mid1 - 1

        elif searched_value > lista[mid2]:
            left = mid2 + 1
        
        else:
            left = mid1 + 1
            right = mid2 - 1
  
    return False

lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29, 30]

print(ternarySearch(lista, 29))




#    https://eduinf.waw.pl/inf/alg/003_sort/0025.php