guest_list = ['tim', 'michelle', 'regina', 'carlotta', 'roel', 'tom']

guest_list.insert(0,'aragorn')
guest_list.insert(3, 'gandalf') 
guest_list.insert(5, 'saruman') 

print ("Hereby I extend an inivitation to " + guest_list[0] + " to join my dinner.")
print ("Hereby I extend an inivitation to " + guest_list[1] + " to join my dinner.")
print ("Hereby I extend an inivitation to " + guest_list[2] + " to join my dinner.")
print ("Hereby I extend an inivitation to " + guest_list[3] + " to join my dinner.")
print ("Hereby I extend an inivitation to " + guest_list[4] + " to join my dinner.")
print ("Hereby I extend an inivitation to " + guest_list[5] + " to join my dinner.")
print ("Hereby I extend an inivitation to " + guest_list[6] + " to join my dinner.")
print ("Hereby I extend an inivitation to " + guest_list[7] + " to join my dinner.")
print ("Hereby I extend an inivitation to " + guest_list[8] + " to join my dinner.")

non_attending = guest_list.pop() 

print ("Sorry " +  non_attending.title() + " but your inivitation has been retracted")