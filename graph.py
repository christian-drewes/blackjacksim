import matplotlib.pyplot as plt

def createGraph(p1, d1, p2, d2):
    fig, ax = plt.subplots()

    ax.bar(2, p1, 0.35, yerr=d1,
        color='Blue', label='Less than 17')
    ax.bar(3, p2, 0.35, yerr=d2,
        color='Blue', label='Less than 12')
    ax.bar(2.35, d1, 0.35, yerr=d1,
        color='Red', label='dealer')
    ax.bar(3.35, d2, 0.35, yerr=d2,
        color='Red', label='dealer')
    
    plt.ylabel("Number of Wins")
    plt.title("BlackJack Strategies")
    #plt.xticks(('1', '2'))
    plt.legend()

    plt.show()
