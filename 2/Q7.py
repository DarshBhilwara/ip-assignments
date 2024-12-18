import re
directory = {}
pages = open('pages.txt', 'r')
for a in pages:
    b = a.split(': ', 1)
    c = b[0].strip()
    c = c.split(', ')
    url = c[0]
    init_importance = float(c[1])
    if len(b) > 1:
        h = b[1].strip()
    else:
        h = ''
    m = ''
    for w in h:
        if w not in [',', '.']:
            m = m+w
    links = []
    ex = m.split()
    for y in ex:
        if 'URL' in y:
            if y not in links:
                links.append(y)
    directory[url] = {'init_importance': init_importance,
                      'overall_importance': 0,
                      'links': links}
for x, y in directory.items():
    for linked in y['links']:
        if linked in directory:
            n = len(directory[x]['links'])
            if n > 0:
                directory[linked]['overall_importance'] += y['init_importance']/n

d = []
for j, k in directory.items():
    d.append((j, k['overall_importance']))

for l in range(len(d)):
    for m in range(len(d)-l-1):
        if d[m][1] < d[m+1][1]:
            d[m], d[m+1] = d[m+1], d[m]

x = int(input('Number of top pages to show : '))


def _test():
    assert x <= len(
        directory), 'The number of URLs are less than the pages you asked for'


_test()
out = d[:x]
print('Top', x, 'Pages')
for url, imp in out:
    print(url, ' Overall Importance : ', imp)
