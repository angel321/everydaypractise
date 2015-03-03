# -*- coding: utf-8 -*-

import urllib2
import urlparse
import time
import os
import sys

from bs4 import BeautifulSoup # get html links
from selenium import webdriver


input_url = ""
result_url = {}
max_sites = 10
current_visited = 0
driver = webdriver.PhantomJS()
screenshot_directory = './screenshots/'



def take_screenshot(url):
    filename = screenshot_directory + str(current_visited) + '.png'
    print 'saving screenshot of', url, ' as ', filename
    driver.get(url)
    driver.save_screenshot(filename)


def process_one_url(url):
    try:
    # in case of 404 error
        html_page = urllib2.urlopen(url)
        soup = BeautifulSoup(html_page)
        for link in soup.findAll('a'):
            full_url = urlparse.urljoin(url, link.get('href'))
            if full_url.startswith(input_url) and full_url not in result_url:
                result_url[full_url] = False
        result_url[url] = True       # set as crawled
        return True
    except:
        result_url[url] = True   # set as crawled
        print 'Unable to reach the site'
        return False


def more_to_crawl():
    for url, crawled in iter(result_url.iteritems()):
        if not crawled:
            return url
    return False


def initiate():
    global input_url
    global result_url
    if len(sys.argv) > 1:
        input_url = sys.argv[1]
        result_url = {input_url: False}
    else:
        print 'Please provide a URL to crawl.'
        return False
    global max_sites
    max_sites = int(sys.argv[2]) if len(sys.argv) > 2 else 10
    print 'maximum number of sites:', max_sites
    if not os.path.exists(screenshot_directory):
        os.makedirs(screenshot_directory)
        print 'directory created'
    return True


def crawl():
    global current_visited
    if not initiate():
        return
    print 'max_sites :', max_sites
    while True:
        to_crawl = more_to_crawl()
        if not to_crawl:
            break
        if process_one_url(to_crawl):
            take_screenshot(to_crawl)
        current_visited += 1
        if current_visited == max_sites:
            break
        time.sleep(2)


crawl()
driver.quit()
print 'crawling done'