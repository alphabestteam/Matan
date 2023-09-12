

import time
import requests
import threading


def timmer(func):
    def inner(*args, **kwargs):
        t0 = time.time()
        func(*args, **kwargs)
        t1 = time.time()
        print(f"total running time: {t1 - t0}")
    return inner


def single_file_downloader(file_url: str, name_of_file: str):
    """
    this function downloads a single file from the internet
    input: file url and the name you want to give the file
    output: None
    """
    r = requests.get(file_url, stream=True)

    with open(name_of_file, "w") as file:
        file.write(r.text)


@timmer
def main():
    urls = ["https://upload.wikimedia.org/wikipedia/commons/thumb/e/e2/Matzov-unit-insignia-2020.png/330px-Matzov-unit-insignia-2020.png",
            "https://ssl.gstatic.com/ui/v1/icons/mail/rfr/ logo_gmail_lockup_default_1x_rtl.png",
            "https://github.githubassets.com/images/modules/open_graph/github-mark.png",
            "https://www.google.co.il/images/branding/googlelogo/2x/googlelogo_color_160x56dp.png"]
    
    count = 0
    thread_list = []
    for url in urls:
        count += 1
        thread = threading.Thread(target=single_file_downloader, args=(url, f"file{count}"))
        thread_list.append(thread)

    for thread in thread_list:
        thread.start()

#running time without threading : total running time: 0.790532112121582
#running with threading : total running time: 0.0003731250762939453

if __name__ == "__main__":
    main()