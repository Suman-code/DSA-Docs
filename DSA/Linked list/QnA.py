from QnAlinkedlist import LinkedList
def checkdup(ll):
    tav = ll.head
    while tav:
        tav1 = tav
        while tav1.next:
            if tav1.next.value == tav.value:
                tav1.next = tav1.next.next
            else:
                tav1 = tav1.next
        tav = tav.next
    return ll.head

linkedLis = LinkedList()
linkedLis.generate(10,10,20)
print(linkedLis)
checkdup(linkedLis)
print(linkedLis)
            
