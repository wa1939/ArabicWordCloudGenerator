import pandas as pd
from wordcloud import WordCloud
import arabic_reshaper
from bidi.algorithm import get_display
import random

# Function to manually remove specific words
def remove_specific_words(text, words_to_remove):
    for word in words_to_remove:
        text = text.replace(f' {word} ', ' ')
    return text

# Load the Excel file containing the behaviors
try:
    df = pd.read_excel('C:/Users/walghamdi/Desktop/Arabiccloude/thesorcefile.xlsx', engine='openpyxl')
except Exception as e:
    print(f"Error loading the Excel file: {e}")
    raise

# Combine all the text from the 'النص المراد تحليله' column
try:
    text = ' '.join(df['النص المراد تحليله'].astype(str).tolist())
except KeyError as e:
    print(f"Column 'النص المراد تحليله' not found in the Excel file: {e}")
    raise

# Manually specify words to remove
words_to_remove = ["و", "في", "على", "من", "او", "أو","بشكل","طلب","مع","خلال","بين","الذي","عدم","ذلك","و ","التأكيد","القطاع","جدا","المكاتب","لكن","ما","الى","بالنسبة","شي","ولكن","العمل","المكان","مكان","لا","يوجد","المكتب","يؤدي"]

# Remove these specific words from the text
text = remove_specific_words(text, words_to_remove)

# Reshape Arabic text for proper display
reshaped_text = arabic_reshaper.reshape(text)
bidi_text = get_display(reshaped_text)

# Define the color function using Elm colors
def color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    colors = ["#808285", "#2A6EBB", "#952D98", "#44C8F5", "#722EA5", "#1E1656"]
    return random.choice(colors)

# Generate the word cloud with custom colors and a transparent background
try:
    wordcloud = WordCloud(font_path='C:/Users/walghamdi/Desktop/Arabiccloude/DIN Next LT Arabic Regular.ttf',
                          width=800, height=800, 
                          background_color=None, mode='RGBA',
                          color_func=color_func).generate(bidi_text)
except Exception as e:
    print(f"Error generating word cloud: {e}")
    raise

# Save the word cloud image with a transparent background
try:
    wordcloud.to_file('C:/Users/walghamdi/Desktop/Arabiccloude/arabic_wordcloud.png')
    print("Word cloud image saved successfully!")
except Exception as e:
    print(f"Error saving word cloud image: {e}")
