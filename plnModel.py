import bs4 as bs  
import urllib.request  
import re
import heapq  
import nltk

class PlnModel(object):
    
    def __init__(self):
        print("model")

    def get_scraper_text(self, url):  
        #Obtener Datos de pagina web
        scraped_data = urllib.request.urlopen(url)  
        article = scraped_data.read()
        #Analizar datos obtenidos de la pagina web
        parsed_article = bs.BeautifulSoup(article,'lxml')
        #Obtener Parrafos
        paragraphs = parsed_article.find_all('p')
        article_text = ""
        #Unir parrafos obtenidos
        for p in paragraphs:  
            article_text += p.text
        print(article_text)
        return article_text    

    def format_text(self, article_text):
        print("format_text")
        # elimina los corchetes y reemplaza los espacios múltiples por uno solo
        article_text = re.sub(r'\[[0-9]*\]', ' ', article_text)  
        article_text = re.sub(r'\s+', ' ', article_text)

        #Remover caracteres especailes y numeros
        formatted_article_text = re.sub('[^a-zA-Z]', ' ', article_text )  
        formatted_article_text = re.sub(r'\s+', ' ', formatted_article_text)

        # article_text --> artículo original 
        # formatted_article_text --> artículo con formato.
        # Convertir el articulo en oreaciones
        # formatted_article_textno no tiene signos puntuación, no se puede convertir en oraciones  
        # tokenización a oraciones
        self.sentence_list = nltk.sent_tokenize(article_text)  

        #Obtener diccionario de palabras vacias  o de uso comun ingles
        self.stopwords = nltk.corpus.stopwords.words('english')
        return formatted_article_text

    #Encontrar la frecuencia ponderada de ocurrencia
    def get_resum(self,formatted_article_text):
        word_frequencies = {}
        # Tokenizar formatted_article_text para obtener todas las palabras  
        for word in nltk.word_tokenize(formatted_article_text):
            # Verificamos word  no sea una  palabra vacia  
            if word not in self.stopwords:
                if word not in word_frequencies.keys():
                    word_frequencies[word] = 1
                else:
                    word_frequencies[word] += 1
        # frecuancia de la palabra que mas repite
        maximum_frequncy = max(word_frequencies.values())            

        
        # para encontrar la frecuencia ponderada --> dividir el número de ocurrencias de todas las palabras por 
        # la frecuencia de la palabra que aparece con mayor frecuencia

        for word in word_frequencies.keys():  
            word_frequencies[word] = (word_frequencies[word]/maximum_frequncy)            
        
        #Diccionario para agregar el puntaje de las oraciones
        sentence_scores = {}  
        for sent in self.sentence_list:  
            for word in nltk.word_tokenize(sent.lower()):
                if word in word_frequencies.keys():
                    #Se realiza el calculo para oraciones menores a 30 palabras
                    if len(sent.split(' ')) < 30:
                        if sent not in sentence_scores.keys():
                             #Si la oración no existe, la agregamos al sentence_scores diccionario como una clave y
                             #le asignamos la frecuencia ponderada de la primera palabra en la oración, como su valor.
                            sentence_scores[sent] = word_frequencies[word]
                        else:
                            #si la oración existe en el diccionario, simplemente agregamos la frecuencia ponderada de la palabra al valor existente.
                            sentence_scores[sent] += word_frequencies[word]

        #Recuperar las 7 oraciones principales 
        summary_sentences = heapq.nlargest(7, sentence_scores, key=sentence_scores.get)

        self.summary = ' '.join(summary_sentences)  
        
        print('\n')
        print('\n')
        print('\n')
        print('\n')
        print('\n Resumen')
        print('\n')
        #https://en.wikipedia.org/wiki/Artificial_intelligence  
        return self.summary

            
