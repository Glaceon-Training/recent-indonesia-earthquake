import requests
import bs4


class LatestEarthquake:

    def __init__(self):
        self.description = 'to get the latest earthquake information from bmkg.go.id'
        self.result = None

    def data_extraction(self):
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
            self.result = extract
        else:
            return None

    def show_data(self):
        if self.result is None:
            print("There are no new earthquake detected")
            return
        print('BMKG latest earthquake detection:')
        print(f"Date: {self.result['date']}")
        print(f"Time: {self.result['time']}")
        print(f"Magnitude: {self.result['magnitude']}")
        print(f"Depth (in km): {self.result['depth']}")
        print(f"Location: LS = {self.result['location']['ls']}, BT = {self.result['location']['bt']}")
        print(f"Epicentre: {self.result['epicentre']}")
        print(f"Mercalli Scale: {self.result['mercalli_scale']}")

    def run(self):
        self.data_extraction()
        self.show_data()

if __name__ == '__main__':
    indonesia_earthquake = LatestEarthquake()
    print('Package description is', indonesia_earthquake.description)
    indonesia_earthquake.run()
    # indonesia_earthquake.data_extraction()
    # indonesia_earthquake.show_data()


