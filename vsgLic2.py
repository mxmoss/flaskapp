import json
import sys

class VsgLicense:
#    def __init__(self, sn):
#           self.sn = sn

    def data_dir(self):
        if sys.platform == 'linux':
            return sys.path[0]+'/'
        return sys.path[0]+'\\'

    def load_file(self):
        with open(self.data_dir()+'custs.json') as json_file:
            return json.load(json_file)

    def save_file(self, customers):
        with open(self.data_dir()+'custs.json', 'w') as f:
            json.dump(customers, f)
        return customers

    def get_customer(self, customer_id):
        # Search for customer
        with open(self.data_dir()+'custs.json') as json_file:
            customers = json.load(json_file)
            customer = customers.get(customer_id)
            if customer:
                return customer
            return []

    def validate(self, customer_id, secret_id):
        customer = self.get_customer(customer_id)
        if customer and customer['secret_id'] == secret_id:
            return True
        return False

    @staticmethod
    def cust_rec( cust_id, secret_id='0000', ver='2.01',
                 lease_dt='2023-01-01', temp_dt='2022-12-01',
                 dante_yn='Y', dante_lic='0000', sslo_yn='1', sslo_lic='0000',
                 general=[0, 0, 0, 0], replay=[0, 0, 0, 0], studio=[0, 0, 0, 0], review=[0, 0, 0, 0]):
        return {
            'sn': cust_id,
            'secret_id': secret_id,
            'ver': ver,
            'lease': lease_dt,
            'temp': temp_dt,
            'dante': dante_yn,
            'dante_lic': dante_lic,
            'sslo': sslo_yn,
            'sslo_lic': sslo_lic,
            'general': general,
            'replay': replay,
            'studio': studio,
            'review': review
        }

    def add(self, customer_id, custinfo):
        customers = self.load_file()
        customers[customer_id] = custinfo
        self.save_file(customers)
        return customers[customer_id]

    def update(self, customer):
        customers = self.load_file()
        customers[customer['sn']] = customer
        self.save_file(customers)
        return customers[customer['sn']]

    def delete(self, customer_id):
        customers = self.load_file()
        customers.pop(customer_id)
        self.save_file(customers)
        return customers

    def reset(self, customer):
        # TBD??
        return

    def check_out(self, customer):
        customer['in_use'] = 'Y'
        self.update(customer)

    def check_in(self, customer):
        customer['in_use'] = 'N'
        self.update(customer)

