from ypackage.filesystem import read_json, read_file, write_file

SETTİNG_FILE = "sumconfig.json"


def convert_url_form(filestr: str, url: str):
    return filestr.replace("./", url + "/").replace("README.md", "").replace(".md", "")


if __name__ == "__main__":
    settings_data = read_json(SETTİNG_FILE)
    for i in range(len(settings_data['internals'])):
        ipath = settings_data['internals'][i]
        epath = settings_data['externals'][i]
        url = settings_data['urls'][i]

        summarystr = read_file(epath)
        summarystr = convert_url_form(summarystr, url)
        write_file(ipath, summarystr)
