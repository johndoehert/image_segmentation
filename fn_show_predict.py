def plot_predict(array_list, color_map = 'nipy_spectral'):
    '''
    Plots and a slice with all available annotations
    '''
    fig = plt.figure(figsize=(20,16), dpi=100)

    plt.subplot(1,3,1)
    plt.imshow(array_list[0], cmap='bone')
    plt.title('Original Image')
    plt.axis('off')
             
    plt.subplot(1,3,2)
    plt.imshow(array_list[1], alpha=0.5, cmap=color_map)
    plt.title('True Mask')
    plt.axis('off')
    
    plt.subplot(1,3,3)
    plt.imshow(array_list[1], alpha=0.5, cmap=color_map)
    plt.title('Predicted Mask')
    plt.axis('off')
    
    plt.show()
