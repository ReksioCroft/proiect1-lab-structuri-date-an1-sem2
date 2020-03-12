import time
import random


def bubblesort( v ):
    ok = 0
    poz = 0
    while ok == 0:
        ok = 1
        for i in range ( 1, len(v)-poz):
            if v[i-1] > v[i]:
                v[i] ^= v[i-1]
                v[i-1] ^= v[i]
                v[i] ^= v[i-1]
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


def radixsort1( v, shift ):     # radixsort recursiv in baza 256
    lista = [ [] for i in range(256) ]
    mask = ( 1 << 8 ) - 1
    for i in v:
        lista[ ( i >> shift ) & mask ].append( i )
    v = []
    for i in range(256):
        if shift > 0 and len( lista[i] ) > 1:
            lista[i] = radixsort1( lista[i], shift-8 )
        v.extend( lista[i] )
    return v


fin = open( "date.in" )
co = 0
try:
    for i in fin:
        co += 1
        print( "TESTUL NUMARUL " + str(co) )
        l = [int(x) for x in i.split() ]
        l1 = l.copy()
        start = time.time()
        l1.sort()
        stop = time.time()
        print( "Am sortat folosind functia de biblioteca " + str( len(l1) ) + " numere <= " + str( l1[-1] ) + " in " + str( stop - start ) + " secunde " )

        if len(l) < 1000000:
            l2 = l.copy()
            start = time.time()
            l2 = bubblesort( l2 )
            stop = time.time()
            if l2 != l1:
                print( "eroare bubblesort" )
            else:
                print("Am sortat folosind bubblesort " + str( len(l2) ) + " numere <= " + str( l2[-1] ) + " in " + str( stop - start ) + " secunde ")
        #else:
         #   raise Exception ( "bubblesort skiped for " + str( len(l) ) + "numbers" )

        if max(l) - min(l) < 10000000:
            l2 = l.copy()
            start = time.time()
            l2 = countsort(l2)
            stop = time.time()
            if l2 != l1:
                print("eroare countsort")
            else:
                print("Am sortat folosind countsort " + str(len(l2)) + " numere <= " + str(l2[-1]) + " in " + str( stop - start ) + " secunde ")
       # else:
        #    raise Exception ( "countsort skipped for " + str( max(l)-min(l) ) + " memory" )

        l2 = l.copy()
        start = time.time()
        l2 = quicksort(l2)
        stop = time.time()
        if l2 != l1:
            print("eroare quicksort")
        else:
            print("Am sortat folosind quicksort " + str(len(l2)) + " numere <= " + str(l2[-1]) + " in " + str( stop - start ) + " secunde ")

        l2 = l.copy()
        start = time.time()
        l2 = mergesort(l2)
        stop = time.time()
        if l2 != l1:
            print("eroare mergesort")
        else:
            print("Am sortat folosind mergesort " + str(len(l2)) + " numere <= " + str(l2[-1]) + " in " + str( stop - start ) + " secunde ")

        l2 = l.copy()
        start = time.time()
        l2 = radixsort1(l2, 32-8 )
        stop = time.time()
        if l2 != l1:
            print("eroare radixsort1", end=" ")
            print(l2)
        else:
            print("Am sortat folosind radixsort " + str(len(l2)) + " numere <= " + str(l2[-1]) + " in " + str( stop - start ) + "s ecunde ")
        print()
except Exception as e0:
    print( e0 )