import config
import urllib2
import json


class ShutterStockClient(object):
    access_token = None
    last_resp = None

    def get_access_token(self):

        payload = "grant_type=client_credentials&client_id=%s&client_secret=%s&scope=licenses.view%% 20user.view" % (
            config.client_id, config.client_secret)

        url = 'https://accounts.shutterstock.com/oauth/access_token'

        req = urllib2.Request(url, data=payload, headers={"Content-Type": "application/x-www-form-urlencoded"})

        resp = urllib2.urlopen(req)
        data = json.load(resp)
        self.access_token = data
        resp.close()
        return data

    def api_call(self, endpoint, method='GET'):
        req = urllib2.Request('https://api.shutterstock.com/v2/%s' % endpoint)
        req.add_header("Authorization", "Bearer %s" % self.access_token['access_token'])
        resp = urllib2.urlopen(req)
        data = json.load(resp)
        resp.close()
        self.last_resp = data
        return data


def main():
    client = ShutterStockClient()
    client.get_access_token()
    print client.api_call('user/access_token')


if __name__ == '__main__':
    main()