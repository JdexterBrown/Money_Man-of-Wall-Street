# this validates the country typed in is real
import pycountry as pc


my_country = []
pycountrylist = list(pc.countries)
alpha_2 = []
alpha_3 = []
name = []
common_name = []
official_name = []
# invalid_countryname = []
valid_country = []
country_state = []


class My_Country:
    def __init__(self, country):
        self.country = country
        self.my_country = my_country
        my_country.append(country)
        self.invalid_countryname = []
        self.name = name
        self.alpha_2 = alpha_2
        self.alpha_3 = alpha_3
        self.pycountrylist = pycountrylist
        self.country_state = country_state

        for i in pycountrylist:
            alpha_2.append(i.alpha_2)
            alpha_3.append(i.alpha_3)
            name.append(i.name)
            # print(f'Alpha 2: {alpha_2}')
            # print(f'Alpha 3: {alpha_3}')

            if hasattr(i, "common_name"):
                common_name.append(i.common_name)
                # print(common_name)
            else:
                common_name.append("")
            if hasattr(i, "official_name"):
                official_name.append(i.official_name)
                # print(official_name)
            else:
                official_name.append("")

        for j in self.my_country:
            if j not in map(str.upper, self.alpha_2) and j not in map(str.upper, self.alpha_3) and j not in map(
                    str.upper, self.name):
                # if j not in map(str.upper, alpha_2) and j not in map(str.upper, alpha_3) and j not in map(str.upper, name):
                self.invalid_countryname.append(j)
                invalid_countryname = list(self.invalid_countryname)
                #return print(f"You entered in invalid country name of {j}")

                self.my_country.clear()
                return print("This isn't a real country. Please type in another country")

                # return print("This isn't a real country. Please type in another country")
            else:
                self.my_country.clear()
                return print(f'Country name of {j} is valid. You may proceed on')

            self.my_country.clear()
#test = "FRANCE"
#My_Country(test)

# val_country = My_Country(test)
# print(val_country.country)
# m_country = valid_country.country
