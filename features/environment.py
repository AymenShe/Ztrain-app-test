import undetected_chromedriver as uc

def before_all(context):
    opts = uc.ChromeOptions()
    opts.add_argument("--window-size=1020,900")
    opts.add_argument("--incognito")
    opts.add_argument("--disable-popup-blocking")

    context.driver = uc.Chrome(options=opts, use_subprocess=True)