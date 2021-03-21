from songline import Sendline
from datetime import date
import pandas as pd


class LineManager:

    def __init__(self, token):
        self.token = token
        self.messenger = Sendline(self.token)

    def sendmsg(self, txt):
        self.messenger.sendtext(txt)

    def xmarkfilter(self):
        df = pd.read_csv("db/xmarks.csv")
        self.x_out_dict = {}

        for i in range(len(df)):
            if date.today().strftime("%d %b %Y") == df.loc[i, "date"]:
                if df.loc[i, "mark"] in self.x_out_dict:
                    self.x_out_dict[df.loc[i, "mark"]].append(df.loc[i, "symbol"])
                else:
                    self.x_out_dict[df.loc[i, "mark"]] = [df.loc[i, "symbol"]]

        return self.x_out_dict

    def xmarktdsum(self):
        content = [""]
        header = f"Hello, {date.today().strftime('%d %b %Y')}\nToday have:"
        content.append(header)
        for key in self.x_out_dict:
            num = len(self.x_out_dict[key])
            txt = f"{num} symbols with {key} mark"
            content.append(txt)
        self.td_sum = "\n".join(content)
        self.messenger.sendtext(self.td_sum)

    def xmarkbody(self):
        for key in self.x_out_dict:
            content = [""]
            header = f"{date.today().strftime('%d %b %Y')} {key} Mark:"
            content.append(header)
            for i in range(len(self.x_out_dict[key])):
                txt = f"{i + 1}. {self.x_out_dict[key][i]}"
                content.append(txt)
            out_txt = "\n".join(content)
            self.messenger.sendtext(out_txt)
