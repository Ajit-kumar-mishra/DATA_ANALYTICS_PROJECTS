import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Create a figure with subplots
fig, axs = plt.subplots(2, 4, figsize=(15, 8))  # 2 rows, 4 columns

# Manually load and display each image in the corresponding subplot
img1 = mpimg.imread('Visualization_Charts/Distribution_of_Sales_Amount.png')
axs[0, 0].imshow(img1)
axs[0, 0].axis('off')  # Hide the axes
axs[0, 0].set_title('Chart 1')

img2 = mpimg.imread('Visualization_Charts/Sales_Amount_by_Category.png')
axs[0, 1].imshow(img2)
axs[0, 1].axis('off')  # Hide the axes
axs[0, 1].set_title('Chart 2')

img3 = mpimg.imread('Visualization_Charts/Sales_Amount_Over_Time.png')
axs[0, 2].imshow(img3)
axs[0, 2].axis('off')  # Hide the axes
axs[0, 2].set_title('Chart 3')

img4 = mpimg.imread('Visualization_Charts/Total_Sales_by_Category.png')
axs[0, 3].imshow(img4)
axs[0, 3].axis('off')  # Hide the axes
axs[0, 3].set_title('Chart 4')

img5 = mpimg.imread('Visualization_Charts/Total_Sales_by_Month.png')
axs[1, 0].imshow(img5)
axs[1, 0].axis('off')  # Hide the axes
axs[1, 0].set_title('Chart 5')

img6 = mpimg.imread('Visualization_Charts/Total_Sales_by_Region.png')
axs[1, 1].imshow(img6)
axs[1, 1].axis('off')  # Hide the axes
axs[1, 1].set_title('Chart 6')

img7 = mpimg.imread('Visualization_Charts/Unit_sold_over_time.png')
axs[1, 2].imshow(img7)
axs[1, 2].axis('off')  # Hide the axes
axs[1, 2].set_title('Chart 7')

# Save the figure to a file
plt.tight_layout()  # Adjust layout to prevent overlap
plt.savefig('Merged_Charts.png')  # Save to a file
plt.show()  # Display the figure
