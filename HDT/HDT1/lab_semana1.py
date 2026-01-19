import cv2
import numpy as np
import matplotlib.pyplot as plt

def show_wrong_rgb_img(img, title="Imagen", cmap=None):
    # esta funcion es para mostrar que es lo que pasa si no se hace la correccion
    # de los canales de color de BGR a RGB
    plt.figure(figsize=(6, 6))
    plt.title(title)
    plt.imshow(img, cmap=cmap)
    plt.axis('off')
    plt.show()

def show_img(img, title="Imagen", cmap=None):
    plt.figure(figsize=(6, 6))
    plt.title(title)
    # TODO: Matplotlib espera RGB, OpenCV carga BGR.
    # Verifica si la imagen tiene 3 canales y conviértela para visualización correcta.
    if len(img.shape) == 3 and cmap is None:
        img_show = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    else:
        img_show = img
    
    plt.imshow(img_show, cmap=cmap)
    plt.axis('off')
    plt.show()

def manual_contrast_brightness(image, alpha, beta):
    """
    Aplica g(x) = alpha * f(x) + beta de forma segura.
    Args:
        image: numpy array uint8
        alpha: float (contraste)
        beta: float (brillo)
    Returns:
        numpy array uint8
    """
    # RETO 1: Implementar pipeline seguro
    # 1. Convertir a float32 y normalizar a [0, 1]
    # 2. Aplicar fórmula matemática vectorizada (Sin bucles for)
    # 3. Aplicar np.clip para evitar valores fuera de rango
    # 4. Des-normalizar (x255) y castear a uint8
    
    # TODO: Escribir código aquí
    processed_img = np.zeros_like(image) # Placeholder
    return processed_img

def manual_gamma_correction(image, gamma):
    """
    Aplica V_out = V_in ^ gamma
    """
    # RETO 2: Implementar corrección Gamma
    # Recordar: La operación potencia es costosa. 
    # Usar Look-Up Table (LUT) es una optimización común, pero aquí usa matemáticas directas en float.
    
    # normalizacion de float
    img_float = image.astype(np.float32) / 255.0
    
    # correccion con el valor gamma usnado potencia, usando numpy para no iterar sobre cada uno
    corrected_power = np.power(img_float, gamma)

    # arreglar clipping, de igual forma usando numpy para evitar iterar
    # y tner valores fuera de rango
    correcteed_clipping = np.clip(corrected_power, 0 , 1)

    # desnomalizar para regresar a uint 8 para que se pueda mostrar la imagen
    gamm_img = (correcteed_clipping * 255.00).astype(np.uint8)

    return gamm_img

def hsv_segmentation(image):
    """
    Segmentar un objeto de color específico (ej. verde o rojo)
    """
    # 1. Convertir a HSV
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    # RETO 3: Definir rangos para un color.
    # OJO: En OpenCV Hue es [0, 179].
    # Ejemplo: Si buscas verde, H está alrededor de 60 (en escala 0-179).
    
    # TODO: Definir lower_bound y upper_bound (np.array)
    lower_bound = np.array([0, 0, 0]) 
    upper_bound = np.array([0, 0, 0])
    
    # Crear máscara
    mask = cv2.inRange(hsv, lower_bound, upper_bound)
    
    # Aplicar máscara a la imagen original (bitwise_and)
    result = cv2.bitwise_and(image, image, mask=mask)
    return result

# --- BLOQUE PRINCIPAL ---
if __name__ == "__main__":
    # Cargar imagen (Asegúrate de tener una imagen 'sample.jpg')
    img = cv2.imread('cat.jpg')
    
    if img is None:
        print("Error: No se encontró la imagen.")
    else:
        # 1. Prueba de Contraste
        #contrast_img = manual_contrast_brightness(img, 1.5, 20)
        #show_img(contrast_img, "Contraste Alto (Manual)")
        
        # 2. Prueba de Gamma
        gamma_img = manual_gamma_correction(img, 2) # Aclarar sombras
        show_img(gamma_img, "Corrección Gamma 2")
        
        # 3. Segmentación
        #seg_img = hsv_segmentation(img)
        #show_img(seg_img, "Segmentación HSV")


        # 4. para la pregunta post practica acerca de que pasa si no se corrigen los canales de color
        wrong_rgb_img = manual_gamma_correction(img, 2)
        show_wrong_rgb_img(wrong_rgb_img, "Imagen sin ajustar los canales de color")