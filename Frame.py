import matplotlib.pyplot as plt

class Frame:
    def frame_init(self, weight_in, age_in, Mode, Repeats, Diagram):
        # -------------------- OLAF for boys 3 - 18 (age to weight)----------------------------------------------------
        if Diagram == 1:
            diagram_x = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
            diagram_y = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]

            centile_x = [3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, 10.5, 11, 11.5, 12, 12.5, 13, 13.5, 14, 14.5, 15, 15.5, 16, 16.5, 17, 17.5, 18]
            centile_3_y = [12, 13, 14, 14.5, 15, 16, 17, 18, 18.5, 19, 20.5, 21.5, 22.5, 23.5, 24.5, 26, 27, 28, 30, 31.5, 33.5, 35, 38, 40, 43, 45, 47, 49.5, 51, 52.5, 54]

            centile_10_y = [13, 13.75, 14.75, 15.5, 16, 17, 18, 19, 20.25, 21.25, 22.5, 23.5, 24.75, 25.75, 27, 28, 29.75, 31.25, 33, 35, 37, 39.75, 42, 44.75, 47, 49.25, 51.5, 53.5, 55.25, 57, 58.25]

            centile_25_y = [13.75, 14.75, 15.75, 16.5, 17.25, 18.5, 19.5, 20.5, 22, 23, 24.75, 26, 27, 28.5, 30, 31.5, 33.1, 35, 37, 39.25, 41.5, 44.25, 46.75, 49.9, 52, 54.5, 56.5, 58.5, 60, 61.75, 63.5]

            centile_50_y = [15, 16, 17, 18, 19, 20.25, 21.5, 22.9, 24.5, 26, 27.5, 29, 30.75, 32.5, 34.25, 36, 38, 40.25, 43, 45.25, 48, 51, 53.75, 56.25, 59, 61, 63, 65, 67, 68.5, 70]

            centile_75_y = [16.5, 17.5, 18.75, 20, 21.25, 22.5, 24.5, 26, 27.75, 29.9, 31.5, 33.25, 35.5, 37.25, 39.9, 41.9, 44.75, 47, 50, 53, 55.75, 59, 62, 64.75, 67, 69.25, 71.25, 73.1, 74.9, 76.5, 78]

            centile_90_y = [18, 19.25, 20.75, 22, 23.5, 25.5, 27.5, 29.5, 32, 34.25, 36.75, 38.75, 41.25, 44, 46.75, 49.75, 52.5, 55.1, 58.6, 61.9, 65, 68.5, 71, 73.75, 76, 78.25, 80, 82, 83.25, 84.9, 86]

            centile_97_y = [20, 21.5, 23, 24.9, 26.75, 29.75, 32.1, 34.9, 37.5, 40.5, 43.5, 46.25, 49.5, 52.5, 56, 59, 62.75, 66, 69.75, 73.1, 76.5, 80, 82.75, 85, 87, 89, 90.5, 92.1, 93.5, 94.75, 96]

            diagram_x_text = 'Age (years)'
            diagram_y_text = 'Weight (kg)'

        # -------------------------OLA for boys 3 - 18 (age to weight)----------------------------------------------------------
        if Diagram == 2:
            diagram_x = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
            diagram_y = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80]

            centile_x = [3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, 10.5, 11, 11.5, 12, 12.5, 13, 13.5, 14, 14.5, 15, 15.5, 16, 16.5, 17, 17.5, 18]
            centile_3_y = [11.95, 12.4, 13.1, 14, 14.6, 15.2, 16, 16.9, 17.8, 18.8, 19.9, 20.7, 21.8, 23, 24, 25.2, 26.5, 28.1, 30, 32, 34.3, 36.2, 38.2, 39.7, 41, 42, 42.8, 43.4, 43.9, 44.1, 44.4]

            centile_10_y = [12.6, 13.2, 14, 14.9, 15.7, 16.5, 17.3, 18.1, 19.2, 20.1, 21.5, 22.6, 23.9, 25.4, 26.4, 27.8, 29.7, 31.2, 33.2, 35.6, 37.8, 39.9, 41.7, 43, 44.5, 45.2, 46, 46.6, 47, 47.4, 47.6]

            centile_25_y = [13.5, 14.2, 15.1, 16, 17, 17.9, 18.9, 20, 21, 22, 23.7, 25, 26.5, 27.9, 29.4, 31, 33, 35, 37.2, 39.5, 42, 43.7, 45.6, 47, 48.1, 49.1, 49.7, 50.4, 50.8, 51.1, 51.2]

            centile_50_y = [14.5, 15.5, 16.6, 17.5, 18.6, 19.8, 20.9, 22, 23.5, 24.9, 26.7, 28, 29.9, 31.6, 33.3, 35.5, 38, 40.2, 42.7, 45.1, 47.3, 49.5, 51, 52.4, 53.7, 54.2, 54.9, 55.5, 55.9, 56.1, 56.2]

            centile_75_y = [15.9, 17, 18.1, 19.5, 20.6, 22, 23.5, 25, 26.9, 28.4, 30.4, 32, 34.5, 36.5, 38.9, 41.5, 44, 47, 49.5, 52, 54.4, 56.3, 57.8, 59, 60, 60.5, 61, 61.6, 62, 62.1, 62.2]

            centile_90_y = [17.5, 19, 20.1, 21.9, 23.3, 25, 26.7, 28.4, 30.4, 32.5, 35, 37, 39.5, 42.4, 45.2, 48, 51.5, 54.5, 57.2, 60, 62, 64, 65.4, 66.1, 67.1, 67.8, 68.1, 68.4, 68.9, 69.1, 69.2]

            centile_97_y = [19.5, 21, 22.8, 24.6, 26.5, 28.5, 30.5, 32.5, 35.2, 38, 40.5, 43.8, 47, 50, 53.2, 57, 60.4, 64, 67, 69.5, 71.7, 73.2, 74.5, 75.3, 76, 76.5, 76.9, 77.2, 77.5, 77.8, 77.9]

            diagram_x_text = 'Age (years)'
            diagram_y_text = 'Weight (kg)'

        plt.figure(figsize=(6, 9))
        plt.plot(centile_x, centile_3_y, label='Centile 3', color='black')
        plt.plot(centile_x, centile_10_y, label='Centile 10', color='black', linestyle='--')
        plt.plot(centile_x, centile_25_y, label='Centile 25', color='black', linestyle=':')
        plt.plot(centile_x, centile_50_y, label='Centile 50', color='black', linestyle='solid')
        plt.plot(centile_x, centile_75_y, label='Centile 75', color='black', linestyle=':')
        plt.plot(centile_x, centile_90_y, label='Centile 90', color='black', linestyle='--')
        plt.plot(centile_x, centile_97_y, label='Centile 97', color='black', linestyle='solid')
        if Mode == 1:
            plt.scatter(weight_in, age_in, label='Single Point', color='red', s=5)
        if Mode == 2:
            for i in range(Repeats):
                plt.scatter(weight_in[i], age_in[i], label='Multi Points', color='red', s=5)
        if Mode == 3:
            plt.plot(age_in, weight_in, label='Curve', color='red', linestyle=':')

        plt.text(centile_x[-1], centile_3_y[-1], ' c3', verticalalignment='bottom')
        plt.text(centile_x[-1], centile_10_y[-1], ' c10', verticalalignment='bottom')
        plt.text(centile_x[-1], centile_25_y[-1], ' c25', verticalalignment='bottom')
        plt.text(centile_x[-1], centile_50_y[-1], ' c50', verticalalignment='bottom')
        plt.text(centile_x[-1], centile_75_y[-1], ' c75', verticalalignment='bottom')
        plt.text(centile_x[-1], centile_90_y[-1], ' c90', verticalalignment='bottom')
        plt.text(centile_x[-1], centile_97_y[-1], ' c97', verticalalignment='bottom')

        plt.title('Centile grid')
        plt.xlabel(diagram_x_text)
        plt.ylabel(diagram_y_text)

        plt.xticks(diagram_x)
        plt.xlim(diagram_x[0], diagram_x[-1])
        plt.ylim(diagram_y[0], diagram_y[-1])
        plt.yticks(diagram_y)

        plt.grid(True)

        fig = plt.gcf()
        fig.tight_layout()
        fig.savefig('percentile_grid.png')
