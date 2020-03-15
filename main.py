import time
import random


def bubblesort( v ):
    ok = 0
    poz = 0
    while ok == 0:
        ok = 1
        for i in range ( 1, len(v)-poz):
            if v[i-1] > v[i]:
                aux = v[i]
                v[i] = v[i-1]
                v[i-1]=aux
                ok = 0
        poz += 1
    return  v


def countsort( v ):
    mini = min(v)
    maxi = max(v)
    frecv = [0 for i in range(maxi - mini + 1 )]
    for i in v:
        frecv[i - mini] += 1

    poz = 0
    for i in range( len(frecv) ):
        for j in range( frecv[i] ):
            v[poz] = i + mini
            poz += 1
    return v


def quicksort( v ):
    def quick( start, stop ):
        i = start
        j = stop
        p1 = random.choice( v[start:stop+1] )
        p2 = random.choice( v[start:stop+1] )
        p3 = random.choice( v[start:stop+1] )
        if p1 <= p2 <= p3 or p1 >= p2 >= p3:
            pivot = p2
        elif p2 <= p1 <= p3 or p2 >= p1 >= p3:
            pivot = p1
        else:
            pivot = p3

        while i <= j:
            while v[i] < pivot:
                i += 1
            while v[j] > pivot:
                j -= 1
            if i <= j:
                aux = v[i]
                v[i] = v[j]
                v[j] = aux
                i += 1
                j -= 1
        if i < stop:
            quick( i, stop )
        if j > start:
            quick( start, j )

    quick( 0, len(v) - 1 )
    return v


def mergesort( v ):
    def interclasare( l1, l2 ):
        i = j = 0
        l = []
        while i < len(l1) and j < len(l2):
            if l1[i] < l2[j]:
                l.append( l1[i] )
                i += 1
            else:
                l.append( l2[j] )
                j += 1
        while i < len( l1 ):
            l.append( l1[i] )
            i += 1
        while j < len( l2 ):
            l.append( l2[j] )
            j += 1
        return  l

    if len( v ) == 1:
        return v

    v1 = v[ :len(v)//2]
    v2 = v[len(v)//2:]

    v1 = mergesort( v1 )
    v2 = mergesort( v2 )

    return interclasare( v1, v2 )

def radixsort1_rec( v ):
    def Radixsort1_rec( v, shift ):     # radixsort recursiv in baza 256
        bucket = [ [] for i in range(256) ]
        mask = ( 1 << 8 ) - 1
        for i in v:
            bucket[ ( i >> shift ) & mask ].append( i )
        v = []
        for i in range(256):
            if shift > 0 and len( bucket[i] ) > 1:
                bucket[i] = Radixsort1_rec( bucket[i], shift-8 )
            v.extend( bucket[i] )
        return v
    return Radixsort1_rec( v, 32 - 8 )


def radixsort1_itr( v ):    #radix sort iterativ in baza 256, incepand cu cifra nesemnificativa
    base = 256
    shift = 0
    mask = ( 1 << 8 ) - 1

    maxi = max(v)
    co = 0
    while maxi > 0:
        maxi >>= 8
        co += 1

    for i in range( co ):
        bucket = []
        for j in range( base ):
            bucket.append( [] )
        for j in v:
            nr = ( j >> shift ) & mask
            bucket[nr].append(j)
        v = []
        for j in range(base):
            v.extend( bucket[j] )
        shift += 8
    return v


def radixsort2( v ):
    def Radixsort2( v, shift, pozstart, pozstop ):  #radix sort in baza 256, fara vector suplimentar
        base = 1 << 8
        mask = (1 << 8) - 1

        start = [ 0 for i in range(base) ]
        stop = [ 0 for i in range(base) ]

        start[0] = stop[0] = pozstart

        for i in range(pozstart,pozstop):
            stop[(v[i] >> shift) & mask] += 1              # calculam cate numere sunt in bucket-ul i

        for i in range( 1, base ):                       # precalculam unde incepe si unde se termina fiecare bucket i: [ start[i], stop[i] )
            start[i] = stop[i-1]
            stop[i] += start[i]

        for i in range(base):
            while start[i] < stop[i]:                     # cat timp numerele din bucket-ul i se afla in alta parte
                nr = v[ start[i] ]
                nr_bucket = ( nr >> shift ) & mask
                while nr_bucket != i:                     # cat timp nu am gasit un nr care intra in bucket-ul i
                    aux = v[ start[nr_bucket] ]

                    v[ start[ nr_bucket] ] = nr
                    start[nr_bucket] += 1

                    nr = aux
                    nr_bucket = ( nr >> shift ) & mask
                v[ start[i] ] = nr
                start[i] += 1

        if shift > 0:
            for i in range(base):
                prev = stop[i-1] if i > 0 else pozstart
                if stop[i] - prev > 1:
                     v = Radixsort2( v, shift - 8, prev, stop[i] )

        return v
    return Radixsort2(l2, 32 - 8, 0, len(l2))


def heapsort( v ):
    heap = [-1]

    def inserare_heap( nr ):
        heap.append( nr )
        poz = len( heap ) - 1
        while heap[poz] < heap[poz//2]:
            aux = heap[poz]
            heap[poz] = heap[poz//2]
            heap[poz//2] = aux
            poz //=2

    def extragere_heap():
        nr = heap[1]
        ultim = heap.pop()
        if len( heap ) > 1:
            heap[1] = ultim
            poztata = 1
            ok = True
            while ok:
                if poztata * 2 > len(heap) - 1:
                    ok = False
                elif poztata * 2 == len(heap) - 1:
                    if heap[poztata*2] < heap[poztata]:
                        aux = heap[poztata*2]
                        heap[poztata*2] = heap[poztata]
                        heap[poztata] = aux
                    ok = False
                else:
                    minifiu = ( 2 * poztata ) if heap[2 * poztata] < heap[2 * poztata + 1] else (2 * poztata + 1)
                    if heap[minifiu] < heap[poztata]:
                        aux = heap[poztata]
                        heap[poztata] = heap[minifiu]
                        heap[minifiu] = aux
                        poztata = minifiu
                    else:
                        ok = False
            return [nr]
        elif len(heap) == 1:
            return [nr]
        else:
            return []

    for i in v:
        inserare_heap( i )

    v = []
    while len( heap ) > 1:
        v.extend( extragere_heap() )
    return v


teste = open( "teste.in" )
co = 0
co1 = co2 = 0
sortari = [ bubblesort, countsort, quicksort, mergesort, heapsort, radixsort1_rec, radixsort1_itr, radixsort2 ]

for i in teste:
    co += 1
    print( "TESTUL NUMARUL " + str(co) )
    l = [int(x.strip(",")) for x in i.split() ]

    # sortare de biblioteca, fata de care vom compara celelalte sortari pentru verificare corectitudinii
    l1 = l.copy()
    start = time.time()
    l1.sort()
    stop = time.time()
    t1 = stop - start
    print( "Am sortat folosind functia de biblioteca " + str( len(l1) ) + " numere <= " + str( l1[-1] ) + " in " + str( stop - start ) + " secunde " )

    t2 = 1 << 32 # Infinit
    for sortare in sortari:
        if sortare == bubblesort and len(l) >= 100000:
            print("bubblesort skiped for " + str(len(l)) + " numbers")
        elif sortare == countsort and max(l) - min(l) >= 10000000:
            print("countsort skipped for " + str(max(l) - min(l)) + " memory")
        else:
            l2 = l.copy()
            start = time.time()
            l2 = sortare(l2)
            stop = time.time()
            t2 = min( t2, stop - start )
            if l2 != l1:
                print("eroare " + str(sortare) )
                print(l2)
            else:
                print("Am sortat folosind " + str(sortare) + " " + str(len(l2)) + " numere <= " + str(l2[-1]) + " in " + str( stop - start ) + " secunde ")
    if t1 < t2:
        co1 += 1
    else:
        co2 += 1
    print()

print( "Concluzia:")
if co2 > co1:
    print( "Programatorul merita un premiu!" )
elif co2 == co1:
    print( "Merita sa implementezi sortarea de mana ca sa te dai mare!" )
else:
    print( "In python, renunta la asemenea idei. Nu poti bate limbajul =))) !" )

print( "That's all folks!" )