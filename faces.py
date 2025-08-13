def main():
    mood = input("how do you feel today?")
    print (emoji(mood))

def emoji(newmood):
    return newmood.replace(":(",'🙁').replace(":)",'🙂')

main()
