import requests
import bs4

description = 'to get the latest earthquake information from bmkg.go.id'

def data_extraction():
    """
    Date: 16 Agustus 2024
    Time: 08:16:04 WIB
    Magnitude: 5.1
    Depth: 226 km
    Location: LS=8.07 BT=123.01
    Epicentre: 27 km Timur Laut LARANTUKA-NTT
    Tsunami Alert: tidak berpotensi TSUNAMI
    :return:
    """
    try:
        content = requests.get('https://bmkg.go.id/')
    except Exception:
        return None

    if content.status_code == 200:

        soup = bs4.BeautifulSoup(content.text, 'html.parser')

        date_time = soup.find('span', {'class': 'waktu'})
        date = date_time.text.split(', ')[0]
        time = date_time.text.split(', ')[1]

        scrap = soup.find('div', {'class': 'col-md-6 col-xs-6 gempabumi-detail no-padding'})
        scrap = scrap.findChildren('li')
        i = 0
        magnitude = None
        depth = None
        ls = None
        bt = None
        epicentre = None
        mercalli_scale = None
        for eq in scrap:
            if i == 1:
                magnitude = eq.text
            elif i == 2:
                depth = eq.text
            elif i == 3:
                coordinate = eq.text.split(' - ')
                ls = coordinate[0]
                bt = coordinate[1]
            elif i == 4:
                epicentre = eq.text
            elif i == 5:
                mercalli_scale = eq.text
            i = i + 1

        extract = dict()
        extract['date'] = date
        extract['time'] = time
        extract['magnitude'] = magnitude
        extract['depth'] = depth
        extract['location'] = {'ls': ls, 'bt': bt}
        extract['epicentre'] = epicentre
        extract['mercalli_scale'] = mercalli_scale
        return extract
    else:
        return None



def show_data(result):
    if result is None:
        print("There are no new earthquake detected")
        return
    print('BMKG latest earthquake detection:')
    print(f"Date: {result['date']}")
    print(f"Time: {result['time']}")
    print(f"Magnitude: {result['magnitude']}")
    print(f"Depth (in km): {result['depth']}")
    print(f"Location: LS = {result['location']['ls']}, BT = {result['location']['bt']}")
    print(f"Epicentre: {result['epicentre']}")
    print(f"Mercalli Scale: {result['mercalli_scale']}")


if __name__ == '__main__':
    print('Package description is', description)
    result = data_extraction()
    show_data(result)
