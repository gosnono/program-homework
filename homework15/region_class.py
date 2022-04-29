import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



class PopGraph:
    def __init__(self, df_popkr):#데이터 전처리과정
        df_popkr = pd.read_csv("202203_202203_연령별인구현황_월간.csv", encoding="euc-kr")
        
        df_popkr["행정구역"] = df_popkr["행정구역"].str.split("(").str[0]
        df_popkr.replace(",", "", regex=True, inplace=True)
        df_popkr.replace(" ", "", regex=True, inplace=True)

        df_popkrM = df_popkr.filter(like="남").filter(like="세")
        df_popkrMT = df_popkrM.T
        df_popkrMT.columns = df_popkr["행정구역"].values
        df_popkrMT = df_popkrMT.astype(int)

        df_popkrMT["나이"] = df_popkrMT.index.str.split("_").str[2]
        df_popkrMT.reset_index(drop=True, inplace=True)

        df_popkrF = df_popkr.filter(like="여").filter(like="세")
        df_popkrFT = df_popkrF.T
        df_popkrFT.columns = df_popkr["행정구역"].values
        df_popkrFT = df_popkrFT.astype(int)
        df_popkrFT["나이"] = df_popkrFT.index.str.split("_").str[2]
        df_popkrFT.reset_index(drop=True, inplace=True)

        self.df_popkrMT = df_popkrMT
        self.df_popkrFT = df_popkrFT
        
    def plot_pop(self, loc, popmax=7e4, poptick=1e4):#plot 세부적으로 꾸미기
        fig, axs = plt.subplots(ncols=2, sharey = True, figsize=(10, 5), gridspec_kw={"wspace": 0})
        c_M = "#3366ff"
        c_F = "#ff6699"
        axs[0].barh(self.df_popkrMT["나이"], self.df_popkrMT[loc], color=c_M)
        axs[1].barh(self.df_popkrFT["나이"], self.df_popkrFT[loc], color=c_F)

        axs[0].set_xlim(popmax, 0)
        axs[1].set_xlim(0, popmax)
    
        xticks = np.arange(0, popmax, poptick)
        if poptick >= 1e6:
            factor, unit = 1e-6, "백만"
        elif 1e5 <= poptick < 1e6:
            factor, unit = 1e-5, "십만"
        elif 1e4 <= poptick < 2e5:
            factor, unit = 1e-4, "만"
        elif 1e3 <= poptick < 2e4:
            factor, unit = 1e-3, "천"

        for ax, title in zip(axs, ["남성", "여성"]):
            ax.set_xticks(xticks)
            ax.set_xticklabels([f"{int(x * factor)}{unit}" if x != 0 else "0" for x in xticks])
            ax.grid(axis="x", c="lightgray")
            ax.set_title(title, color="gray", fontweight="bold", pad=16)

        for ax in axs:
            for i, p in enumerate(ax.patches):
                w = p.get_width()
                if ax == axs[0]:
                    ha = "right"
                    c = c_M
                else:
                    ha = "left"
                    c = c_F

                ax.text(w, i, f" {format(w, ',')} ",
                        c=c, fontsize="x-small", va="center", ha=ha,
                        fontweight="bold", alpha=0.5)

        plt.suptitle(f"{loc}", fontweight="bold", x=0.56, y=0.92)
        fig.tight_layout()
        return fig
    
    
    def plot(self, loc):# 해당 데이터에 따른 popmax, poptick 맞춤
        data_where = self.df_popkrFT[loc]

        if max(data_where) < 5000:
            popmax = 6e3
            poptick = 1e3
            
            fig = self.plot_pop(loc, popmax, poptick)# def 함수도 self.함수 가능

        elif 5000< max(data_where) <10000:
            popmax = 12e3
            poptick = 2e3
            
            fig = self.plot_pop(loc, popmax, poptick)
            
        elif max(data_where) > 60000:
            popmax = 2e5
            poptick = 0.25e5
            
            fig = self.plot_pop(loc, popmax, poptick)
        else:
            fig = self.plot_pop(loc)
            
        fig.show()
        plt.show()#plot 보여줌
        
        
        

        
        


def main():
    # 시각화 설정
    sns.set_context("talk")
    sns.set_style("white")

    plt.rcParams['font.family'] = ['gulim', 'sans-serif']
    plt.rcParams['axes.unicode_minus'] = False# 여기까지는 plot 한글 및 스타일 설정
    
    where = "전라북도" + input("지역명을 입력하시오.")

    pop_jb = PopGraph("202203_202203_연령별인구현황_월간.csv")# 클래스
    pop_jb.plot(where)#plot함수 실행
    
if __name__ == "__main__":
    main()
