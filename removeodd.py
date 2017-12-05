def removeodd(words):
    
    listtobuild = ''
    
    for i in range(len(words)):
        if i % 2 == 0:
            listtobuild = listtobuild + words[i]                
            
    print(listtobuild)
                        
title = 'Gilgamesh'
removeodd(title)
title = 'The Lord of the Rinks: The Fellowship of the Rink'
removeodd(title)