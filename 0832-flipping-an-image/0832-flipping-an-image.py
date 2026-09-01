class Solution(object):
    def flipAndInvertImage(self, image):
        for row in image:
            row.reverse()

        for i in range(len(image)):
            for j in range(len(image[i])):
                if image[i][j]==1:
                    image[i][j]=0

                else:
                     image[i][j]=1

        return image



        



