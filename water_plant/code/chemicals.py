'''web scraping de precios quimicos a usar en el tratamiento de agua'''


from lxml import html as html
import requests


links = { #lista paginas web precio quimicos
    'sulfate' : 'https://listado.mercadolibre.com.co/sulfato-de-aluminio#D[A:sulfato%20de%20aluminio]',
    'limestone' : 'https://listado.mercadolibre.com.co/piedra-caliza#D[A:piedra%20caliza]',
    'chlorine' : 'https://listado.mercadolibre.com.co/hipoclorito-de-sodio#D[A:hipoclorito%20de%20sodio]'
}

prices = {
    'sulfate' : '//span[@class = "price-tag-fraction" and contains(.,68.000)]/text()',
    'limestone' : '//span[@class = "price-tag-fraction" and contains(.,149.000)]/text()',
    'chlorine' : '//span[@class = "price-tag-fraction" and contains(.,13.500)]/text()',
}


def scraper(site, path):
    response = requests.get(site)
    try:
        if response.status_code == 200:
            doc = response.content.decode('utf-8')
            x_doc = html.fromstring(doc)
            price = x_doc.xpath(path)#precio de sulfato de mercadolibre
            return price
        else:
            raise ValueError (f'Error: {response.status_code}')
    except ValueError as err:
        print(err)


def colector():
    sulfate = scraper(links['sulfate'],prices['sulfate'])
    sulfate = sulfate[0].replace('.','')
    sulfate_mg = price(25000000, float(sulfate)) #precio de 1mg de sulfato
    limestone  = scraper(links['limestone'], prices['limestone'])
    limestone = limestone[0].replace('.','')
    limestone_mg = price(2267961.67, float(limestone)) #precio de 1mg de piedra caliza
    chlorine = scraper(links['chlorine'],prices['chlorine'])
    chlorine = chlorine[0].replace('.','')
    chlorine_ml = price(3800,float(chlorine))/100 #precio de 0.01ml de cloro
    values = [sulfate_mg, limestone_mg, chlorine_ml]
    return values
    

def price(compound, price): #precio por unidad
    charge = compound/price
    return charge

if __name__ == '__main__':
    colector()