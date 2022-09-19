'''A brief explanation of sentiment analysis.
    Polarity: the sentiment analysis will have a scale of polarity -1 meaning
    a bad sentiment, 0 meaning neutral sentiment and 1 meaning a relly good sentiment
    Subjectivity: also a subjectivity analysis will be given, 0 meaning that are facts 
    what's beeing given and 1 meaning that's a personal opinion what's beeing given'''


from textblob import TextBlob #sentiment analysis library
import matplotlib.pyplot as plt #graphs


def graphs(polarity_l:list, subjectivity_l:list):
    try:
        plt.plot(polarity_l, c = 'blue', label= "polarity") #graph polarity with blue
        plt.plot(subjectivity_l, c = "orange", label = "subjectivity") #graph subjectivity with orange
        plt.legend()
        plt.show() #showing the graph
    except ValueError as ve:
        print(ve)


def analysis(comments:list):
    polarity_l = [] #list of given polarities from the comments
    subjectivity_l = [] #list of given subjectivities from the comments
    try:
        for comment in range(0,len(comments)):
            text = TextBlob(comments[comment])
            polarity = text.sentiment.polarity #polarity of the comment
            subjectivity = text.sentiment.subjectivity #subjectivity of the comment
            #english = text.translate(to="en") # if article is given in Spanish I've to transalte it to english
            #print(english) #print to see the translation
            polarity_l.append(polarity) #add polarity to list
            subjectivity_l.append(subjectivity) #add subjectivity to list
            print(f"Comment number {comment + 1} \nPolarity analysis: {polarity}" + 
                f"\nSubjectivity analysis: {subjectivity}") ##print to see the sentiment analysis
        return polarity_l, subjectivity_l
    except ValueError as ve:
        print(ve)