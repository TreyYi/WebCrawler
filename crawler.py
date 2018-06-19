from bs4 import BeautifulSoup
import os

def htmlText():
    page_nums = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 138, 148, 158]
    tmp = []
    html_paths = []

    # generate file names
    for a in range(0,len(page_nums)):
        strn = 'cited_papers(start_'+str(page_nums[a])+').html'
        tmp.append(strn)

    #generate paths with generated files
    for i in range(0,len(page_nums)):
        tmp_filename = os.path.join(r'C:\Users\Trey\Desktop\Web Crawler\papers_HTML\Cited_Papers_HTML', tmp[i])
        html_paths.append(tmp_filename)

    html_lists=[]   # html to text type to use bs4
    for html_path in html_paths:
        filename = (html_path)
        html_text = str(open(filename, 'r', encoding='utf-8').read())
        html_lists.append(html_text)
    # print ("############\n", html_lists)

    return html_lists

def title_plus_address(html_string):
    soup=BeautifulSoup(html_string, 'html.parser')
    # print(soup.prettify())
    h3 = soup.findAll('h3', attrs={'class':'gs_rt'})

    # collect links or just titles in cases when link doesn't exist
    hrefList = []
    for i in h3:
        try:  # Remove span tags to get only <a>'s text
            tmp = i.find('span')
            tmp.extract()
            time.sleep(1)
            temp = i.find('a')['href']  # Web address
            title = i.find('a', attrs={'href':i}).text  # Its title
            hrefList.append(title+"("+temp+")"+"\n")
        except:
            try:    # If there is no span tag, then just get a text from <a>
                temp = i.find('a')['href']  # Web address
                title = i.find('a', attrs={'href':temp}).text  # Its title
                hrefList.append(title+"("+temp+")"+"\n")
            except: # If there is no link at all
                title = i.text
                hrefList.append("<Citation / No Links>"+title+"\n") # it's not a link, hence just append the title
    return hrefList


if __name__ == '__main__':
    file_ = open(r'C:\Users\Trey\Desktop\Web Crawler\papers_HTML\Cited_Papers_HTML\tmp2.txt', "a", encoding='utf-8')
    a = htmlText()  # HTML pages array in string type of element
    for a1 in a:
        b = title_plus_address(a1)
        # write the elements in the list
        for li in b:
            file_.write(li)
    file_.close()
