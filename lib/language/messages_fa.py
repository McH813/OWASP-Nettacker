#!/usr/bin/env python
# -*- coding: utf-8 -*-


def all_messages():
    return \
        {
            "0": "انجین Nettacker شروع به کار کرد...\n\n",
            "1": "python nettacker.py [گزینه ها]",
            "2": "نشان دادن منوی راهنمای Nettacker",
            "3": "لطفا مجوز و موافقت نامه را مطالعه فرمایید https://github.com/viraintel/OWASP-Nettacker\n",
            "4": "انجین",
            "5": "گزینه های ورودی انجین",
            "6": "لطفا یک زبان انتخاب کنید {0}",
            "7": "اسکن کل آی پی ها در رنج",
            "8": "یافتن و اسکن کردن ساب دامین ها",
            "9": "تعداد ریسه ها برای ارتباطات با یک هاست",
            "10": "تعداد ریسه ها برای اسکن هاست ها",
            "11": "ذخیره کردن کل لاگ ها در فایل (result.txt، result.html، results.json)",
            "12": "هدف",
            "13": "گزینه های ورودی هدف",
            "14": "لیست هدف (ها)، با \",\" جدا کنید",
            "15": "خواندن هدف (ها) از فایل",
            "16": "گزینه های متود های اسکن",
            "17": "متود اسکن را انتخاب کنید {0}",
            "18": "انتخاب متود اسکن استثنا {0}",
            "19": "لیست نام کاربری (ها)، با \",\" جدا شود",
            "20": "خواندن نام کاربری (ها) از لیست",
            "21": "لیست کلمه عبور (ها)، با \",\" جدا شود",
            "22": "خواندن کلمه عبور (ها) از فایل",
            "23": "لیست درگاه (ها)، با \",\" جدا شود",
            "24": "خواندن کلمه عبور (ها) از فایل",
            "25": "زمان مکث بین هر درخواست",
            "26": "عدم توانایی در مشخص کردن هدف (ها)",
            "27": "عدم توانایی در مشخص کردن هدف (ها)، عدم توانایی در بازکردن فایل: {0}",
            "28": "بهتر است که از تعداد ریسه کمتر از 100 استفاده کنید، به هر حال ما ادامه می دهیم...",
            "29": "زمان وقفه {0} ثانیه قرار داده شد، زیادی بزرگ است، نیست؟ به هر حال ما ادامه می دهیم...",
            "30": "این ماژول اسکن [{0}] پیدا نشد!",
            "31": "این ماژول اسکن [{0}] پیدا نشد!",
            "32": "شما نمی توانید همه متود های اسکن را استثنا کنید",
            "33": "شما نمی توانید همه متود های اسکن را استثنا کنید",
            "34": "ماژول {0} که شما جهت استثنا کردن انتخاب کردید پیدا نشد!",
            "35": "ورودی های متود ها را وارد کنید، مثال: "
                  "\"ftp_brute_users=test,admin&ftp_brute_passwds=read_from_file:/tmp/pass.txt&ftp_brute_port=21\"",
            "36": "عدم توانایی در خواندن فایل {0}",
            "37": "عدم توانایی مشخص کردن نام کاربری (ها)، عدم توانایی در بازکردن فایل: {0}",
            "38": "{0} پیدا شد!({2}:{1})",
            "39": "عدم توانایی مشخص کردن کلمه عبور (ها)، عدم توانایی در بازکردن فایل: {0}",
            "40": "فایل \"{0}\" قابل نوشتن نیست",
            "41": "متود اسکن خود را انتخاب کنید!",
            "42": "در حال پاک کردن فایل های موقتی!",
            "43": "در حال مرتب سازی نتایج!",
            "44": "انجام شد!",
            "45": "شروع حمله به {0}، {1} از {2}",
            "46": "این ماژول \"{0}\" در دسترس نیست",
            "47": "متاسفانه این ورژن از نرم افزار فقط می تواند بر روی لینوکس/او اس ایکس/ویندوز اجرا شود.",
            "48": "از ورژن پایتون شما پشتیبانی نشده!",
            "49": "چشم پوشی از هدف تکراری (بعضی از ساب دامین ها/دامین ها آی پی و یا رنج یکسان دارند)",
            "50": "نوع هدف ناشتناخته است [{0}]",
            "51": "در حال بررسی رنج {0} ...",
            "52": "در حال بررسی {0} ...",
            "53": "هاست",
            "54": "نام کاربری",
            "55": "کلمه عبور",
            "56": "درگاه",
            "57": "نوع",
            "58": "توضیحات",
            "59": "سطح حالت پرگویی (0-5) (پیشفرض 0)",
            "60": "نمایش ورژن نرم افزار",
            "61": "چک کردن جهت آپدیت",
            "62": "پراکسی ارتباطات خروجی (socks)"
                  " مثال: 127.0.0.1:9050، socks://127.0.0.1:9050، socks5:127.0.0.1:9050 یا socks4: socks4://127.0.0.1:9050,"
                  " احراز هویت: socks://username:password@127.0.0.1, socks4://username:password@127.0.0.1, "
                  "socks5://username:password@127.0.0.1",
            "63": "لطفا آدرس و پورت معتبر socks را وارد کنید. socks5"
                  " مثال: 127.0.0.1:9050، socks://127.0.0.1:9050، "
                  "socks5:127.0.0.1:9050 یا socks4: socks4://127.0.0.1:9050,"
                  " احراز هویت: socks://username:password@127.0.0.1, socks4://username:password@127.0.0.1, "
                  "socks5://username:password@127.0.0.1",
            "64": "سعی مجدد وقتی که ارتباط قطع شد (پیشفرض 3)",
            "65": "ارتباط ftp به {0}:{0} قطع شد، چشم پوشی از {2}:{3}",
            "66": "با موفقیت وارد شده!",
            "67": "با موفقیت کامل شده، اجازه برای دستور LIST داده نشد.",
            "68": "ارتباط ftp به {0}:{1} نا موفق بود،"
                  " از کل مرحله [روند {2} از {3}] چشم پوشی شد! در حال رفتن به مرحله بعد",
            "69": "ورودی هدف برای ماژول {0} باید DOMAIN، HTTP یا SINGLE_IPv4 باشد، از {1} چشم پوشی شد",
            "70": "نام کاربری: {0} کلمه عبور: {1} هاست: {2} درگاه: {3} پیدا شد!",
            "71": "(عدم دسترسی جهت لیست کردن فایل ها)",
            "72": "تلاش برای {0} از {1} در روند {2} از {3} {4}:{5} {6}",
            "73": "ارتباط smtp به {0}:{1} قطع شد، جشم پوشی از {2}:{3}",
            "74": "ارتباط smtp به {0}:{1} ناموفق بود، "
                  "از کل مرحله [روند {2} از {3}]! چشم پوشی شد! در حال رفتن به مرحله بعد",
            "75": "ورودی هدف برای ماژول {0} باید از نوع HTTP باشد، از {1} چشم پوشی",
            "76": "ارتباط ssh به {0}:{1} قطع شد، چشم پوشی از {2}:{3}",
            "77": "ارتباط ssh به {0}:{1} ناموفق بود، "
                  "از کل مرحله [روند {2} از {3}]! چشم پوشی شد! در حال رفتن به مرحله بعد",
            "78": "ارتباط ssh به %s:%s ناموفق بود، از کل مرحله [روند %s از %s]! چشم پوشی شد! در حال رفتن به مرحله بعد",
            "79": "درگاه باز",
            "80": "هاست: {0} درگاه: {1} پیدا شد!",
            "81": "هدف {0} ارسال شد!",
            "82": "عدم توانایی در باز کردن فایل لیست پروکسی ها: {0}",
            "83": "عدم توانایی در پیدا کردن فایل لیست پروکسی ها: {0}",
            "84": "شما در حال اجرای OWASP Nettacker ورژن {0}{1}{2}{6} با اسم کد {3}{4}{5} می باشید",
            "85": "این ویژگی هنوز فعال نشده است! لطفا \"git clone https://github.com/viraintel/OWASP-Nettacker.git\""
                  " یا \"pip install -U OWASP-Nettacker\" را جهت گرفتن اخرین ورژن اجرا کنید.",
            "86": "ساخت گراف از همه فعالیت ها و اطلاعات، شما باید از خروجی HTML استفاده کنید. گراف های در دسترس: {0}",
            "87": "جهت استفاده از ویژگی گراف نام فایل خروجی شما باید با\".html\" یا \".htm\" تمام شود! ",
            "88": "در حال ساخت گراف ...",
            "89": "پایان ساخت گراف!",
            "90": "گراف تست نفوذ",
            "91": "این گراف توسط OWASP Nettacker ایجاد شده است. گراف شامل فعالیت همه ماژول ها، نقشه شبکه "
                  "و اطلاعات حساس می باشد، لطفا با کسی که قابل اعتماد نیست به اشتراک تگذارید.",
            "92": "گزارش OWASP Nettacker",
            "93": "جزییات نرم افزار: OWASP Nettacker ورژن {0} [{1}] در {2}",
            "94": "هیچ درگاه بازی پیدا نشد!",
            "95": "هیچ نام کاربری/پسوردی پیدا نشد!",
            "96": "{0} ماژول بارگزاری شد ...",
            "97": "این ماژول گراف پیدا نشد: {0}",
            "98": "این ماژول گراف \"{0}\" در دسترس نیست",
            "99": "پینگ کردن هست قبل از اسکن",
            "100": "از هدف {0} و متود اسکن {1} به دلیل true بودن --ping-before-scan و عدم دریافت پاسخ صرف نظر شد! ",
            "101": "شما از آخرین ورژن OWASP Nettacker استفاده نمی کنید، لطفا بروز رسانی کنید.",
            "102": "عدم توانایی جهت چک کردن برای بروز رسانی، لطفا ارتباط اینترنت خود را چک کنید.",
            "103": "شما از آخرین نسخه OWASP Nettacker استفاده می کنید ...",
            "104": "دایرکتوری لیستینگ در {0} پیدا شد",
            "105": "لطفا پورت را به وسیله سویچ -g یا --methods-args به جای url وارد کنید",
            "106": "ارتباط http در {0} قطع شد!",
            "107": "شروع به حالت ویزارد مود",
            "108": "دایرکتوری یا فایلی برای {0} در پورت {1} پیدا نشد",
            "109": "عدم توانایی در باز کردن {0}",
            "110": "مقدار dir_scan_http_method باید GET یا HEAD باشد، به صورت پیشفرض GET تنظیم شد.",
            "111": "لیست کردن کل args مربوط به متود ها",
            "112": "عدم توانایی در گرفتن ورودی های ماژول {0} ",
            "113": "تلاش {0} از {1} در پراکسز {2} of {3} در {4} {5}",
            "114": "دامین پیدا شد: {0}",
            "115": "زمان",
            "116": "دسته",
            "117": "ماژولی با پترن {0} پیدا نشد!",
            "118": "مقدار {0} را وارد کنید | پیشفرض[{1}] > ",
            "119": "مقدار {0} را وارد کنید | گزینه ها[{1}] | پیشفرض[{2}] > ",
            "120": "هدف",
            "121": "تعداد ریسه ها",
            "122": "تعداد ریسه ها برای اسکن همزمان هاست ها",
            "123": "نام فایل خروجی",
            "124": "متود اسکن",
            "125": "متود اسکن استثنا",
            "126": "نام های کاربری",
            "127": "رمز های عبور",
            "128": "زمان وقفه به ثانیه",
            "129": "شماره درگاه ها",
            "130": "سطح حالت پرگویی",
            "131": "پراکسی ساکس",
            "132": "تعداد تلاش های مجدد",
            "133": "یک گراف",
            "135": "سابدامین پیدا شد: {0}",
            "136": "انتخاب پروفایل {0}",
            "137": "پروفایل \"{0}\" پیدا نشد!",
            "138": "در حال انتظار برای {0}",
            "139": "آسیب پذیر به {0}",
            "140": "هدف {0}:{1} آسیب پذیر است به {2}!",
            "141": "آسیب پذیری پیدا نشد! ({0})",
            "142": "متود",
            "143": "API",
            "144": "API گزینه های",
            "145": "شروع سرویس API",
            "146": "آدرس هاست API",
            "147": "شماره درگاه API",
            "148": "حالت اشکال زدایی API",
            "149": "کلید دسترسی API",
            "150": "اجازه دادن فقط به لیست سفید هاست ها برای ارتباط با API",
            "151": "تعریف کردن لیست سفید، با \",\" جدا کنید (مثال: 127.0.0.1, 192.168.1.1/24, 10.0.0.1-10.0.0.255)",
            "152": "تولید لیست دسترسی به API",
            "153": "اسم فایل لیست دسترسی به API",
            "154": "شماره درگاه API باید عدد باشد!",
            "155": "نوع ورودی ناشناخته، نوع شناخته شده قابل قبول SINGLE_IPv4, RANGE_IPv4, CIDR_IPv4 می باشد.",
            "156": " * API Key: {0}\n",
            "157": "شماره درگاه ها باید عدد باشند! (مثال: 80 || 80,1080 || 80,1080-1300,9000,12000-15000)",
            "158": "از طریق OWASP Nettacker API",
            "159": "لطفا داکیومنت ها را مطالعه فرمایید https://github.com/viraintel/OWASP-Nettacker/wiki",
            "160": "کلید API نادرست!",
            "161": "آدرس IP شما مجاز نیست",
            "162": "یافت نشد!",
            "163": "subdomain_scan: سابدامینی پیدا نشد!",
            "164": "viewdns_reverse_ip_lookup_scan: دامنه ای پیدا نشد!",
            "165": "سیشن شما معتبر است!"
        }
