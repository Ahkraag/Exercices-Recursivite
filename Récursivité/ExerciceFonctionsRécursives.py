#Triangle de pascal

def C(n,p):
    if p==0: return 1
    elif p>n: return 0
    else: return C(n-1,p-1)+C(n-1,p)

def afficher(x):
    for j in range(x+1):
        for k in range(j+1):
            print(C(j,k),end=" | ")
        print("\n")

# Test #
afficher(12)

#Palindromes

def est_palindrome(bfh,i=0):
    if bfh[i]!=bfh[-i-1]: return False
    elif bfh[i]==bfh[abs(-i-1)]: return True
    elif i>len(bfh)//2: return True
    else: return est_palindrome(bfh,i+1)

# Test #

print(est_palindrome('laval'))
print(est_palindrome('hello'))
print(est_palindrome('ressasser'))
print(est_palindrome('anna'))
print(est_palindrome('bonsoir'))
print(est_palindrome('radar'))
print(est_palindrome('merci'))
print(est_palindrome('reifier'))
print(est_palindrome('ressasser'))

mot="KarineallaenIrak"
mot=mot.lower()
print(est_palindrome(mot))



# Boucle

def boucle(i,k):
    if i>k:
        return
    else:
        print(i,end=",")
        boucle(i+1,k)

# Test #

#Vos tests ici...
print('avec des négatifs : ',end="")
boucle(-12,2)
print('\n----------------------')
print('cas normal : ',end="")
boucle(0,5)
print('\n-----------------------')
print('bornes égales : ',end="")
boucle(6,6)
print('\n------------------------')
print('borne inférieure trop grande : ',end="")
boucle(7,5)

# Fonction appartient qui renvoi True si la valeur v est présente dans la liste t entre l'indice i et la fin du tableau

def appartient(v,t,i):
    if i>len(t)-1:
        return False
    elif t[i]==v: return True
    else: return appartient(v,t,i+1)

# Test #

tab = [5,4,78,56,23,14,47,9,7,2,3,6,5,89,0,1]
val=14
print(appartient(val,tab,2))
print(appartient(val,tab,5))
print(appartient(val,tab,6))
print(appartient(val,tab,len(tab)-1))

# Fonction recherche de minimum

def minimum(t,i):
    petit=i
    for k in range(i,len(t)):
        if t[k]<=t[petit]:
            petit=k
    return petit

def tri_recursif(t,i=0):
    if len(t)==0:
        return t
    elif i==len(t)-2:
        return t
    else:
        m=minimum(t,i)
        t[i],t[m]=t[m],t[i]
        return tri_recursif(t,i+1)

# Test #

print(tab)
t = tri_recursif(tab, 0)
print(' devient après le tri ', t)
print('------------------------')
tt = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print(tt)
t = tri_recursif(tt, 0)
print(' devient après le tri ', t)
print('------------------------')
t3 = [5, 2]
print(t3)
t = tri_recursif(t3, 0)
print(' devient après le tri ', t)
print('------------------------')
t4 = []
print(t4)
t = tri_recursif(t4, 0)
print(' devient après le tri ', t)

m = [2, 4, 8, 6, 9, 3, 7, 1]
n = 0
for k in range(len(m)):
    i = minimum(m, n)
    print(i)
    m[i], m[k] = m[k], m[i]
    n += 1

print("\n", m)