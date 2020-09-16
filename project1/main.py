#%%
import pandas as pd
from matplotlib import pyplot as plt


class Mapper:

    def __init__(self, file_path):
        self.__file_path = file_path

    def load_csv(self):
        table = pd.read_csv(self.__file_path)
        self.accel = list(table['Acceleration'])
        self.heart_rate = list(table['Heart Rate (beats per minute)'])
        self.latitude = list(table['latitude'])
        self.longitude = list(table['longitude'])

    def categorize_accel(self):
        self.max_cate_accel = int(max(self.accel) / 0.5)
        self.cate_accel = [int(x / 0.5) for x in self.accel]

    def categorize_heart(self):
        self.max_cate_heart = int(max(self.heart_rate) / 30)
        self.cate_heart = [int(x / 30) for x in self.heart_rate]

    def plot_accel(self):
        colors = ['g', 'gold', 'm', 'red', 'k']
        ax = plt.axes()
        for cate in range(self.max_cate_accel + 1):
            x = []
            y = []
            for idx in range(len(self.accel)):
                if cate == self.cate_accel[idx]:
                    x.append(self.latitude[idx])
                    y.append(self.longitude[idx])
            ax.scatter(x, y, c=colors[cate], marker='x', label='Category {}, {} - {}'.format(cate, 0.5 * cate,
                                                                                             0.5 * cate + 0.5))
        xmin = min(self.latitude) - 0.00001
        xmax = max(self.latitude) + 0.00001
        ymin = min(self.longitude) - 0.00001
        ymax = max(self.longitude) + 0.00001
        plt.xlim(xmin, xmax)
        plt.ylim(ymin, ymax)
        plt.xlabel("Latitude")
        plt.ylabel("Logitude")
        # plt.xlim(33.21519, 33.21628)
        # plt.ylim(-87.54485, -87.54379)
        plt.grid()
        plt.legend()
        plt.title("Acceleration")
        plt.show()

    def plot_heart(self):
        colors = ['g', 'gold', 'm', 'red', 'k']
        ax = plt.axes()
        for cate in range(self.max_cate_heart + 1):
            x = []
            y = []
            for idx in range(len(self.heart_rate)):
                if cate == self.cate_heart[idx]:
                    x.append(self.latitude[idx])
                    y.append(self.longitude[idx])
            ax.scatter(x, y, c=colors[cate], marker='x', label='Category {}, {} - {}'.format(cate, 30 * cate,
                                                                                             30 * cate + 30))
        xmin = min(self.latitude) - 0.00001
        xmax = max(self.latitude) + 0.00001
        ymin = min(self.longitude) - 0.00001
        ymax = max(self.longitude) + 0.00001
        plt.xlim(xmin, xmax)
        plt.ylim(ymin, ymax)
        plt.xlabel("Latitude")
        plt.ylabel("Logitude")
        # plt.xlim(33.21519, 33.21628)
        # plt.ylim(-87.54485, -87.54379)
        plt.grid()
        plt.legend()
        plt.title("Heart Rate")
        plt.show()

def main(filepath):
    mapper = Mapper(filepath)
    mapper.load_csv()
    mapper.categorize_accel()
    mapper.plot_accel()
    mapper.categorize_heart()
    mapper.plot_heart()


if __name__ == "__main__":
    main("ExcavatorOperatorData.csv")
    print('finish')
