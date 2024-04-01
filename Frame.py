import matplotlib.pyplot as plt

class Frame:
    diagram_ages = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
    diagram_weights = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]

    centiles_age = [3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, 10.5, 11, 11.5, 12, 12.5, 13, 13.5, 14, 14.5, 15, 15.5, 16, 16.5, 17, 17.5, 18]
    centile_3_weight = [12, 13, 14, 14.5, 15, 16, 17, 18, 18.5, 19, 20.5, 21.5, 22.5, 23.5, 24.5, 26, 27, 28, 30, 31.5, 33.5, 35, 38, 40, 43, 45, 47, 49.5, 51, 52.5, 54]

    centile_10_weight = [13, 13.75, 14.75, 15.5, 16, 17, 18, 19, 20.25, 21.25, 22.5, 23.5, 24.75, 25.75, 27, 28, 29.75, 31.25, 33, 35, 37, 39.75, 42, 44.75, 47, 49.25, 51.5, 53.5, 55.25, 57, 58.25]

    centile_25_weight = [13.75, 14.75, 15.75, 16.5, 17.25, 18.5, 19.5, 20.5, 22, 23, 24.75, 26, 27, 28.5, 30, 31.5, 33.1, 35, 37, 39.25, 41.5, 44.25, 46.75, 49.9, 52, 54.5, 56.5, 58.5, 60, 61.75, 63.5]

    centile_50_weight = [15, 16, 17, 18, 19, 20.25, 21.5, 22.9, 24.5, 26, 27.5, 29, 30.75, 32.5, 34.25, 36, 38, 40.25, 43, 45.25, 48, 51, 53.75, 56.25, 59, 61, 63, 65, 67, 68.5, 70]

    centile_75_weight = [16.5, 17.5, 18.75, 20, 21.25, 22.5, 24.5, 26, 27.75, 29.9, 31.5, 33.25, 35.5, 37.25, 39.9, 41.9, 44.75, 47, 50, 53, 55.75, 59, 62, 64.75, 67, 69.25, 71.25, 73.1, 74.9, 76.5, 78]

    centile_90_weight = [18, 19.25, 20.75, 22, 23.5, 25.5, 27.5, 29.5, 32, 34.25, 36.75, 38.75, 41.25, 44, 46.75, 49.75, 52.5, 55.1, 58.6, 61.9, 65, 68.5, 71, 73.75, 76, 78.25, 80, 82, 83.25, 84.9, 86]

    centile_97_weight = [20, 21.5, 23, 24.9, 26.75, 29.75, 32.1, 34.9, 37.5, 40.5, 43.5, 46.25, 49.5, 52.5, 56, 59, 62.75, 66, 69.75, 73.1, 76.5, 80, 82.75, 85, 87, 89, 90.5, 92.1, 93.5, 94.75, 96]

    def frame_init(self, weight_in, age_in, Mode, Repeats):
        plt.figure(figsize=(6, 9))
        plt.plot(self.centiles_age, self.centile_3_weight, label='Centile 3', color='black')
        plt.plot(self.centiles_age, self.centile_10_weight, label='Centile 10', color='black', linestyle='--')
        plt.plot(self.centiles_age, self.centile_25_weight, label='Centile 25', color='black', linestyle=':')
        plt.plot(self.centiles_age, self.centile_50_weight, label='Centile 50', color='black', linestyle='solid')
        plt.plot(self.centiles_age, self.centile_75_weight, label='Centile 75', color='black', linestyle=':')
        plt.plot(self.centiles_age, self.centile_90_weight, label='Centile 90', color='black', linestyle='--')
        plt.plot(self.centiles_age, self.centile_97_weight, label='Centile 97', color='black', linestyle='solid')
        if (Mode == 1):
            plt.scatter(weight_in, age_in, label='Single Point', color='red', s=5)
        if (Mode == 2):
            for i in range(Repeats):
                plt.scatter(weight_in[i], age_in[i], label='Multi Points', color='red', s=5)
        if (Mode == 3):
            plt.plot(age_in, weight_in, label='Curve', color='red', linestyle=':')

        plt.text(self.centiles_age[-1], self.centile_3_weight[-1], ' c3', verticalalignment='bottom')
        plt.text(self.centiles_age[-1], self.centile_10_weight[-1], ' c10', verticalalignment='bottom')
        plt.text(self.centiles_age[-1], self.centile_25_weight[-1], ' c25', verticalalignment='bottom')
        plt.text(self.centiles_age[-1], self.centile_50_weight[-1], ' c50', verticalalignment='bottom')
        plt.text(self.centiles_age[-1], self.centile_75_weight[-1], ' c75', verticalalignment='bottom')
        plt.text(self.centiles_age[-1], self.centile_90_weight[-1], ' c90', verticalalignment='bottom')
        plt.text(self.centiles_age[-1], self.centile_97_weight[-1], ' c97', verticalalignment='bottom')

        plt.title('Centile grid')
        plt.xlabel('Age (years)')
        plt.ylabel('Weight (kg)')

        plt.xticks(self.diagram_ages)
        plt.xlim(3, 18)
        plt.ylim(10, 100)
        plt.yticks(self.diagram_weights)

        plt.grid(True)

        fig = plt.gcf()
        fig.tight_layout()
        fig.savefig('percentile_grid.png')
